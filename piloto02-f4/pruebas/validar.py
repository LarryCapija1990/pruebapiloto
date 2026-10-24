#!/usr/bin/env python3
"""Pruebas funcionales reproducibles en Chromium. Requiere servidor en :4173."""
from pathlib import Path
from playwright.sync_api import sync_playwright
from PIL import Image
import numpy as np
import base64, hashlib, io, json, time, os

ROOT = Path(__file__).resolve().parents[1]
OUT = Path(os.environ.get('F4_OUT',ROOT/'evidencias'))
OUT.mkdir(exist_ok=True)
URL = os.environ.get('F4_URL','http://127.0.0.1:4173')
report = {'checkpoint':os.environ.get('F4_CHECKPOINT','F4 CP02 v1.1'),'checks':[], 'profiles':{}, 'console':[], 'page_errors':[], 'load_failures':[], 'http_errors':[]}
def check(name,ok,details=None):
    report['checks'].append({'name':name,'passed':bool(ok),'details':details})
    print(('PASS ' if ok else 'FAIL ')+name, flush=True)
def go(page,p):
    page.evaluate('(p)=>window.__F4.go(p)',p)
    page.wait_for_function('(p)=>Math.abs(window.__F4.state.progress-p)<.001',arg=p)
    page.evaluate('()=>new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))')
def wait_progress(page,p):
    page.wait_for_function('(p)=>Math.abs(window.__F4.state.progress-p)<.001',arg=p)
    page.evaluate('()=>new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))')
def canvas_bytes(page):
    return base64.b64decode(page.evaluate("document.querySelector('canvas').toDataURL('image/png').split(',')[1]"))
def fingerprint(page): return hashlib.sha256(canvas_bytes(page)).hexdigest()
def sample(page):
    encoded=page.evaluate('''()=>{
      const c=document.createElement('canvas');c.width=320;c.height=180;
      const ctx=c.getContext('2d');ctx.imageSmoothingQuality='high';
      ctx.drawImage(document.querySelector('canvas'),0,0,320,180);
      return c.toDataURL('image/png').split(',')[1];
    }''')
    return np.array(Image.open(io.BytesIO(base64.b64decode(encoded))).convert('RGB'),dtype=float)
def attach(page,profile):
    page.on('console',lambda m: report['console'].append({'profile':profile,'type':m.type,'text':m.text}) if m.type in ['error','warning'] else None)
    page.on('pageerror',lambda e: report['page_errors'].append({'profile':profile,'error':str(e)}))
    page.on('requestfailed',lambda r: report['load_failures'].append({'profile':profile,'url':r.url,'failure':r.failure}))
    page.on('response',lambda r: report['http_errors'].append({'profile':profile,'status':r.status,'url':r.url}) if r.status>=400 else None)
def controls(page):
    return page.evaluate('''() => ['motion','scrub','begin','end'].map(id=>{
      const e=document.getElementById(id),r=e.getBoundingClientRect();
      return {id,visible:r.width>0&&r.height>0&&r.x>=0&&r.y>=0&&r.right<=innerWidth&&r.bottom<=innerHeight,
        unobstructed:document.elementFromPoint(r.x+r.width/2,r.y+r.height/2)===e,rect:[r.x,r.y,r.width,r.height]};
    })''')

with sync_playwright() as pw:
    browser = pw.chromium.launch(executable_path=os.environ.get('F4_CHROMIUM','/usr/bin/chromium'),headless=True,
        args=['--no-sandbox','--enable-unsafe-swiftshader','--use-gl=angle','--use-angle=swiftshader'])
    report['browser']=browser.version
    for profile,w,h,dpr,touch in [('escritorio',1440,900,1,False),('movil',390,844,2,True),('movil-pequeno',320,568,2,True),('horizontal',844,390,1,True)]:
        ctx=browser.new_context(viewport={'width':w,'height':h},device_scale_factor=dpr,is_mobile=touch,has_touch=touch)
        page=ctx.new_page();attach(page,profile)
        page.goto(URL,wait_until='networkidle');page.wait_for_function('window.__F4?.state.ready')
        data={'viewport':[w,h],'device_scale_factor':dpr,'emulated_touch':touch,'screenshots':[]}
        check(profile+': 8 imágenes cargadas',page.evaluate('window.__F4.metrics.assets===8'))
        check(profile+': pantalla completa y sin desbordamiento horizontal',page.evaluate('document.documentElement.scrollWidth===innerWidth && Math.abs(document.getElementById("stage").clientHeight-innerHeight)<2'))
        checkpoints=[0,.25,.4,.45,.5,.55,.6,.65,.7,.75,.9,.925,.95,.975,.99,1] if profile in ['escritorio','movil'] else [0,.5,1]
        for p in checkpoints:
            go(page,p)
            control=controls(page)
            check(f'{profile} {p*100:g}%: controles visibles y accesibles',all(c['visible'] and c['unobstructed'] for c in control),control)
            name=f'{profile}-p{p*100:05.1f}.png'
            page.screenshot(path=str(OUT/name));data['screenshots'].append(name)
        # The required nonmonotonic route: same coordinates must restore identical pixels.
        values=[]
        for p in [0,.6,.3,.6,1]:
            go(page,p);values.append(fingerprint(page))
        check(profile+': 0→60→30→60→100, píxeles idénticos al volver al 60%',values[1]==values[3],{'hashes':values})
        # Stopping scroll must stop both pixels and render scheduling.
        go(page,.537)
        first=fingerprint(page);renders=page.evaluate('window.__F4.metrics.renders');page.wait_for_timeout(600)
        check(profile+': pausa en 53.7% sin cambio ni renders nuevos',first==fingerprint(page) and renders==page.evaluate('window.__F4.metrics.renders'))
        # Native wheel is independent of the test helper and range controls.
        go(page,0);page.mouse.move(w//2,h//2);page.mouse.wheel(0,320);page.wait_for_timeout(200)
        check(profile+': rueda cambia scroll y composición',page.evaluate('window.__F4.state.progress>0') and fingerprint(page)!=values[0])
        page.locator('#scrub').focus();page.keyboard.press('End');wait_progress(page,1)
        check(profile+': teclado End alcanza 100%',page.evaluate('window.__F4.state.progress>.999'))
        page.keyboard.press('Home');wait_progress(page,0)
        check(profile+': teclado Home alcanza 0%',page.evaluate('window.__F4.state.progress<.001'))
        page.keyboard.press('ArrowRight');page.wait_for_function('window.__F4.state.progress>0')
        check(profile+': teclado flecha incrementa',page.evaluate('window.__F4.state.progress>0'))
        started=time.perf_counter();page.locator('#end').click();wait_progress(page,1)
        data['destination_button_observed_ms']=(time.perf_counter()-started)*1000
        check(profile+': botón Innervision',page.evaluate('window.__F4.state.progress>.999'))
        page.locator('#begin').click();wait_progress(page,0)
        check(profile+': botón Thunder',page.evaluate('window.__F4.state.progress<.001'))
        # Verify geometry matches all documented terrain displacements.
        shifts=[]
        for p,expected in [(.3,0),(.4,29.12),(.5,98.56),(.6,181.44),(.7,250.88),(.8,280)]:
            go(page,p);actual=page.evaluate('window.__F4.state.terrainShift');shifts.append([p,expected,actual])
        check(profile+': ascenso coincide con CP05 ±0.25 px',all(abs(a-e)<.25 for _,e,a in shifts),shifts)
        page.locator('#motion').click();page.wait_for_timeout(120)
        go(page,.6)
        check(profile+': movimiento reducido manual fija terreno',page.evaluate('window.__F4.state.reduced&&window.__F4.state.terrainShift===0'))
        page.screenshot(path=str(OUT/f'{profile}-reducido-p060.png'))
        reduced1=fingerprint(page);page.wait_for_timeout(400)
        check(profile+': movimiento reducido estable en pausa',reduced1==fingerprint(page))
        page.locator('#motion').click();page.wait_for_timeout(100)
        check(profile+': modo normal recupera composición exacta',fingerprint(page)==values[1])
        data['runtime']=page.evaluate('({state:window.__F4.state,assets:window.__F4.metrics.assets,contextLosses:window.__F4.metrics.contextLosses})')
        if profile=='escritorio':
            # Entire route at 0.5% intervals; shader and camera must have no step states.
            hashes=[];diffs=[];previous=None
            for i in range(201):
                go(page,i/200);a=sample(page);hashes.append(hashlib.sha256(a.tobytes()).hexdigest())
                if previous is not None: diffs.append({'to_percent':i/2,'mean_abs_rgb_255':float(np.mean(abs(a-previous)))})
                previous=a
            check('Continuidad: 201 estados distintos en todo el recorrido',len(set(hashes))==201,{'unique':len(set(hashes))})
            check('Continuidad: ningún salto >15/255 en promedio a pasos de 0.5%',max(x['mean_abs_rgb_255'] for x in diffs)<15,{'maximum':max(diffs,key=lambda x:x['mean_abs_rgb_255'])})
            data['continuity']=diffs
            # Capture the joins at higher density and compare exact reversal.
            joins=[]
            for center in [.1,.4,.5,.6,.65,.7,.8,.9,.95,.99]:
                trio=[]
                for v in [center-.001,center,center+.001]:go(page,v);trio.append(sample(page))
                joins.append({'percent':center*100,'left_diff':float(np.mean(abs(trio[1]-trio[0]))),'right_diff':float(np.mean(abs(trio[2]-trio[1])))})
            check('Empalmes: sin discontinuidad >5/255 a ambos lados ±0.1%',all(max(j['left_diff'],j['right_diff'])<5 for j in joins),joins)
            gpu=[]
            for v in [.25,.4,.5,.6,.7,.9,.95]:
                go(page,v);gpu.extend(page.evaluate('Array.from({length:8},()=>window.__F4.benchmark())'))
            data['render_finish_ms']={'count':len(gpu),'median':float(np.median(gpu)),'p95':float(np.percentile(gpu,95)),'max':max(gpu),'note':'draw + gl.finish en SwiftShader; no equivale a FPS de hardware real'}
        report['profiles'][profile]=data;ctx.close()
    # Browser preference must be honored before first render, without clicking.
    ctx=browser.new_context(viewport={'width':390,'height':844},reduced_motion='reduce',has_touch=True,is_mobile=True)
    page=ctx.new_page();attach(page,'preferencia-reducida');page.goto(URL,wait_until='networkidle');page.wait_for_function('window.__F4?.state.ready')
    check('prefers-reduced-motion activa la alternativa desde el inicio',page.evaluate('window.__F4.state.reduced&&document.getElementById("motion").getAttribute("aria-pressed")==="true"'))
    for v in [0,.25,.5,.75,1]:
        go(page,v);page.screenshot(path=str(OUT/f'preferencia-reducida-p{round(v*100):03}.png'))
    check('Alternativa reducida alcanza portada final sin ascenso',page.evaluate('window.__F4.state.progress===1&&window.__F4.state.terrainShift===0'))
    ctx.close()
    # Error-path probes are deliberately separated from normal console counts.
    ctx=browser.new_context();page=ctx.new_page();page.route('**/assets/stars.png',lambda route:route.abort())
    page.goto(URL);page.locator('#error').wait_for(state='visible')
    check('Fallo de carga informa del recurso y ofrece reintento', 'stars.png' in page.locator('#error').inner_text() and page.locator('#error button').count()==1)
    page.screenshot(path=str(OUT/'fallo-carga-controlado.png'));ctx.close()
    ctx=browser.new_context();page=ctx.new_page()
    page.add_init_script("HTMLCanvasElement.prototype.getContext=function(){return null}")
    page.goto(URL);page.locator('#error').wait_for(state='visible')
    check('Sin WebGL: mensaje y enlaces a ambos originales',page.locator('#error a').count()==2 and page.locator('#scrub').is_disabled())
    ctx.close();browser.close()

check('Sin errores de JavaScript en flujos normales',not report['page_errors'],report['page_errors'])
check('Sin errores de consola en flujos normales',not [m for m in report['console'] if m['type']=='error'],report['console'])
check('Sin peticiones fallidas ni HTTP 4xx/5xx en flujos normales',not report['load_failures'] and not report['http_errors'],{'failed':report['load_failures'],'http':report['http_errors']})
report['summary']={'passed':sum(x['passed'] for x in report['checks']),'failed':sum(not x['passed'] for x in report['checks']),'visual_approval':False,'mobile_scope':'Emulación Chromium; no dispositivo físico ni Safari iOS.'}
(OUT/'resultados-pruebas.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report['summary'],ensure_ascii=False),flush=True)
raise SystemExit(1 if report['summary']['failed'] else 0)
