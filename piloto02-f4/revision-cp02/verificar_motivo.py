#!/usr/bin/env python3
"""Comparación real CP01/CP02: forma visible, regresiones y scroll reversible."""
from herramientas import ROOT,HERE,ARGS,comparison_server
from playwright.sync_api import sync_playwright
from PIL import Image,ImageDraw,ImageFont
import numpy as np
import os,json,io,base64,hashlib,math

OUT=HERE/'evidencias';OUT.mkdir(exist_ok=True)
result={'base_commit':'81a9dfbb757c5cc2b1011c0314587cb9b9d661ee','checks':[],'geometry':[],'console':[],'page_errors':[],'failed_requests':[],'captures':[],'scope':'Solo motivo central; escritorio y móvil emulado Chromium.'}
def check(name,ok,details=None):
    result['checks'].append({'name':name,'passed':bool(ok),'details':details});print(('PASS ' if ok else 'FAIL ')+name,flush=True)
def goto(page,v):
    page.evaluate('(v)=>window.__F4.go(v)',v);page.wait_for_function('(v)=>Math.abs(window.__F4.state.progress-v)<.001',arg=v)
    page.evaluate('()=>new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))')
def pixels(page):
    data=page.evaluate("document.querySelector('canvas').toDataURL().split(',')[1]")
    return np.array(Image.open(io.BytesIO(base64.b64decode(data))).convert('RGB'))
def deviation(a):
    a=np.array(a);d=a[-1]-a[0];off=np.abs(d[0]*(a[:,1]-a[0,1])-d[1]*(a[:,0]-a[0,0]))/np.linalg.norm(d)
    return float(off.max())

with comparison_server() as url,sync_playwright() as pw:
    browser=pw.chromium.launch(executable_path=os.environ.get('F4_CHROMIUM','/usr/bin/chromium'),headless=True,args=ARGS)
    for profile,w,h,dpr in [('escritorio',1440,900,1),('movil',390,844,2)]:
        ctx=browser.new_context(viewport={'width':w,'height':h},device_scale_factor=dpr,is_mobile=profile=='movil',has_touch=profile=='movil')
        pages={}
        for version in ['antes','despues']:
            page=ctx.new_page();pages[version]=page
            page.on('console',lambda m:result['console'].append({'type':m.type,'text':m.text}) if m.type in ['error','warning'] else None)
            page.on('pageerror',lambda e:result['page_errors'].append(str(e)))
            page.on('requestfailed',lambda r:result['failed_requests'].append(r.url))
            page.goto(url+'/'+version+'/',wait_until='networkidle');page.wait_for_function('window.__F4?.state.ready')
        before,after=pages['antes'],pages['despues']
        for v in [0,.25,.35,.5,.6,.62,.75,.82,.86,.9,1]:
            imgs={}
            for version,page in pages.items():
                goto(page,v);imgs[version]=pixels(page)
                if v in [0,.25,.35,.5,.6,.75,.82,.86,.9,1]:
                    dest=OUT/version;dest.mkdir(exist_ok=True)
                    path=dest/f'{profile}-p{round(v*100):03}.png';page.screenshot(path=str(path));result['captures'].append(str(path.relative_to(HERE)))
            diff=np.any(imgs['antes']!=imgs['despues'],axis=2)
            if v in [0,.9,1]:check(f'{profile}: original/escena al {v*100:g}% conserva sus píxeles',not diff.any(),{'changed_pixels':int(diff.sum())})
            else:
                # Shader camera unchanged; project a source-space bounding box for the motif.
                ih,iw=diff.shape;scale=max(w/1066,h/600);ratio=iw/w;cx=w*.5;cy=h*.5-12
                x0=max(0,math.floor((cx+(390-533)*scale)*ratio));x1=min(iw,math.ceil((cx+(665-533)*scale)*ratio))
                y0=max(0,math.floor((cy+(55-300)*scale)*ratio));y1=min(ih,math.ceil((cy+(580-300)*scale)*ratio))
                outside=diff.copy();outside[y0:y1,x0:x1]=False
                check(f'{profile} {v*100:g}%: fondo/cámara/estrellas fuera del motivo idénticos',not outside.any(),{'changed_outside':int(outside.sum()),'changed_inside':int(diff.sum())})
            if v in [.25,.5,.75,.9]:
                shape=after.evaluate('window.__F4.motif()');dev=deviation(shape['points'])
                result['geometry'].append({'profile':profile,'progress':v,'max_deviation_from_chord_px':dev,'straightening':shape['straightening'],'body_width_px':shape['bodyWidth'],'core_width_px':shape['coreWidth']})
                if v in [.5,.75]:check(f'{profile} {v*100:g}%: sigue curvo, no una recta',dev>(20 if v==.5 else 12),{'max_deviation_px':dev})
                if v==.9:check(f'{profile} 90%: converge al eje final',dev<.1,{'max_deviation_px':dev})
            if v in [.25,.5,.75,.9]:
                # A paired whole-viewport capture preserves framing, no image retouching.
                a=Image.open(OUT/'antes'/f'{profile}-p{round(v*100):03}.png').convert('RGB')
                b=Image.open(OUT/'despues'/f'{profile}-p{round(v*100):03}.png').convert('RGB')
                panel=Image.new('RGB',(a.width*2,a.height+50),'#0a0c12');panel.paste(a,(0,50));panel.paste(b,(a.width,50))
                draw=ImageDraw.Draw(panel);font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',20)
                draw.text((16,14),f'{v*100:g} % · ANTES CP01',font=font,fill='#e6c9a2');draw.text((a.width+16,14),f'{v*100:g} % · DESPUÉS CP02',font=font,fill='#e6c9a2')
                panel.save(OUT/f'comparativa-{profile}-p{round(v*100):03}.jpg',quality=95)
        values=[]
        for v in [0,.6,.3,.6,1]:goto(after,v);values.append(hashlib.sha256(pixels(after).tobytes()).hexdigest())
        check(profile+': 0→60→30→60→100 reversible, mismo 60%',values[1]==values[3])
        goto(after,.537);image=pixels(after);renders=after.evaluate('window.__F4.metrics.renders');after.wait_for_timeout(600)
        check(profile+': pausa sin pulsaciones, movimiento ni nuevos renders',np.array_equal(image,pixels(after)) and renders==after.evaluate('window.__F4.metrics.renders'))
        # The motion-reduced alternative must remain exactly the prior implementation.
        for page in pages.values():page.locator('#motion').click();page.wait_for_timeout(100)
        for v in [0,.25,.5,.75,.9,1]:
            goto(before,v);goto(after,v)
            check(f'{profile} reducido {v*100:g}%: imagen idéntica a CP01',np.array_equal(pixels(before),pixels(after)))
        if profile=='escritorio':
            after.locator('#motion').click();after.wait_for_timeout(100)
            hashes=[];diffs=[];previous=None
            for i in range(201):
                goto(after,i/200)
                data=after.evaluate('''()=>{const c=document.createElement('canvas');c.width=320;c.height=180;const x=c.getContext('2d');x.imageSmoothingQuality='high';x.drawImage(document.querySelector('canvas'),0,0,320,180);return c.toDataURL().split(',')[1]}''')
                a=np.array(Image.open(io.BytesIO(base64.b64decode(data))).convert('RGB'),dtype=float)
                hashes.append(hashlib.sha256(a.tobytes()).hexdigest())
                if previous is not None:diffs.append({'percent':i/2,'mean_abs_rgb_255':float(np.abs(a-previous).mean())})
                previous=a
            result['continuity']=diffs
            check('CP02 final: 201 estados distintos en 0–100%',len(set(hashes))==201,{'unique':len(set(hashes))})
            check('CP02 final: diferencias continuas, sin salto >15/255 cada 0.5%',max(x['mean_abs_rgb_255'] for x in diffs)<15,{'maximum':max(diffs,key=lambda x:x['mean_abs_rgb_255'])})
        ctx.close()
    browser.close()

check('Sin errores de consola, JS o carga en comparativas',not result['console'] and not result['page_errors'] and not result['failed_requests'],{'console':result['console'],'js':result['page_errors'],'requests':result['failed_requests']})
result['summary']={'passed':sum(c['passed'] for c in result['checks']),'failed':sum(not c['passed'] for c in result['checks']),'visual_approval':False}
(OUT/'resultado-motivo.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
print(json.dumps(result['summary'],ensure_ascii=False),flush=True)
raise SystemExit(1 if result['summary']['failed'] else 0)
