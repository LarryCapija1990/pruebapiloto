from pathlib import Path
import json,base64,hashlib,statistics,io
from PIL import Image,ImageChops
from playwright.sync_api import sync_playwright
R=Path(__file__).resolve().parents[1];html=(R/'ABRIR_T34_T45_CP11.html').read_text();out={'html_sha256_tested':hashlib.sha256(html.encode()).hexdigest(),'checks':[],'source':'same self-contained HTML, offline','device':'Chromium CDP mobile emulation'}
def check(n,ok,d=None):out['checks'].append({'name':n,'passed':bool(ok),'detail':d});print(('PASS ' if ok else 'FAIL ')+n,flush=True)
with sync_playwright() as pw:
 b=pw.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox','--enable-unsafe-swiftshader','--use-gl=angle','--use-angle=swiftshader']);c=b.new_context(offline=True,viewport={'width':390,'height':844},device_scale_factor=2,is_mobile=True,has_touch=True);page=c.new_page();page.set_content(html);page.wait_for_function('window.__T45?.state.ready',timeout=90000);page.wait_for_timeout(1000)
 page.evaluate('__T45.go(.42)');page.wait_for_function('Math.abs(__T45.state.q-.42)<.001');cdp=c.new_cdp_session(page)
 for direction in ['up','down']:
  before=page.evaluate('__T45.state.q');start,end=(580,260) if direction=='up' else (260,580)
  cdp.send('Input.dispatchTouchEvent',{'type':'touchStart','touchPoints':[{'x':190,'y':start}]})
  for i in range(1,13):
   cdp.send('Input.dispatchTouchEvent',{'type':'touchMove','touchPoints':[{'x':190,'y':start+(end-start)*i/12}]});page.wait_for_timeout(25)
  cdp.send('Input.dispatchTouchEvent',{'type':'touchEnd','touchPoints':[]});page.wait_for_timeout(1200);after=page.evaluate('__T45.state.q');check('Gesto táctil '+direction,after>before if direction=='up' else after<before,{'before':before,'after':after})
 page.evaluate('__T45.goT34(.9)');page.wait_for_function('Math.abs(__T45.state.p-.9)<.001');before=page.evaluate('scrollY');page.mouse.move(190,420);page.mouse.wheel(0,300);page.wait_for_timeout(1200);check('Rueda dentro iframe se propaga al recorrido',page.evaluate('scrollY')>before)
 # Geometry finite and no self-intersection of contour in every percent, excluding adjacent edges.
 data=page.evaluate('()=>Array.from({length:101},(_,i)=>({q:i/100,...__T45.geometry(i/100)}))')
 def cross(a,b,c):return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
 crossings=[]
 for g in data:
  ps=g['points'];segs=list(zip(ps,ps[1:]))
  for i,(a,bb) in enumerate(segs):
   for j,(cc,d) in enumerate(segs[i+2:],i+2):
    if g['closed'] and i==0 and j==len(segs)-1:continue
    if cross(a,bb,cc)*cross(a,bb,d)<-1e-7 and cross(cc,d,a)*cross(cc,d,bb)<-1e-7:crossings.append({'q':g['q'],'segments':[i,j]})
 check('Contorno sin auto-intersecciones, 101 poses',not crossings,crossings[:10])
 # Documentary Salute: exact same 2D image transform as intact JPG, no reconstructed features.
 page.evaluate('__T45.render(1)')
 actual=page.evaluate('C.toDataURL()')
 reference=page.evaluate('''()=>{const t=document.createElement('canvas');t.width=C.width;t.height=C.height;const x=t.getContext('2d');x.setTransform(t.width/w,0,0,t.height/h,0,0);x.fillStyle='#080a0f';x.fillRect(0,0,w,h);const a=__T45.camera(1);x.translate(w/2,a.cy);x.scale(a.photoScale,a.photoScale);x.translate(-a.center[0],-a.center[1]);x.drawImage(images.salute,0,0);return t.toDataURL()}''')
 check('Salute final = JPG intacto en matriz de cámara',actual==reference,{'sha256_png':hashlib.sha256(base64.b64decode(actual.split(',')[1])).hexdigest()})
 # Accessibility patch is deliberately the only post-regression change.
 page.evaluate('__T45.go(1)');page.wait_for_function('__T45.state.q>.999');
 check('F4 cubierto queda fuera del foco en T45',page.locator('#base').evaluate('(e)=>e.inert&&e.getAttribute("aria-hidden")==="true"'))
 page.evaluate('__T45.goT34(.8)');page.wait_for_function('Math.abs(__T45.state.p-.8)<.001');check('F4 recupera controles en su tramo',page.locator('#base').evaluate('(e)=>!e.inert&&e.getAttribute("aria-hidden")==="false"'))
 c.close()
 change=json.loads((R/'evidencias/REVISION_ACCESIBILIDAD.json').read_text())
 oldhtml=html
 for patch in reversed(change.get('performance_patch',{}).get('replacements',[])):oldhtml=oldhtml.replace(patch['after'],patch['before'])
 oldhtml=oldhtml.replace(change['replace_after'],change['replace_before'])
 check('Reconstrucción exacta de versión de regresión',hashlib.sha256(oldhtml.encode()).hexdigest()==change['full_regression_html_sha256'])
 for label,w,h,dpr in [('escritorio',1440,900,1),('grande',1920,1080,1),('movil',390,844,2),('horizontal',844,390,1)]:
  c=b.new_context(offline=True,viewport={'width':w,'height':h},device_scale_factor=dpr)
  pages=[]
  for source in [oldhtml,html]:
   p=c.new_page();p.set_content(source);p.wait_for_function('window.__T45?.state.ready',timeout=90000);p.wait_for_timeout(600);pages.append(p)
  for q in [.42,.52,.64,.65,.67,.69,1]:
   values=[]
   for p in pages:
    p.evaluate('(q)=>__T45.go(q)',q);p.wait_for_function('(q)=>Math.abs(__T45.state.q-q)<.001',arg=q);p.evaluate('()=>new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))');values.append(p.evaluate('C.toDataURL()'))
   a,bim=[Image.open(io.BytesIO(base64.b64decode(v.split(',')[1]))).convert('RGB') for v in values];delta=max(v[1] for v in ImageChops.difference(a,bim).getextrema());check(f'{label}: equivalencia final q={q}',delta<=1,{'max_channel_delta':delta})
  samples=pages[1].evaluate('()=>Array.from({length:100},(_,i)=>__T45.benchmark(.18+.82*(i%50)/49))');samples.sort();out.setdefault('final_performance',{})[label]={'samples':100,'median_ms':statistics.median(samples),'p95_ms':samples[94],'max_ms':max(samples),'JS_heap_only_approximate':pages[1].evaluate('performance.memory?performance.memory.usedJSHeapSize:null')};
  c.close()
 b.close()

out['passed']=sum(x['passed'] for x in out['checks']);out['failed']=sum(not x['passed'] for x in out['checks']);(R/'evidencias/INTERACCION.json').write_text(json.dumps(out,indent=2,ensure_ascii=False))
