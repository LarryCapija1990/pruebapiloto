"""Offline regression, original F4 comparison, deterministic T45, evidence and timing."""
from pathlib import Path
import json,hashlib,base64,time,statistics,io,zipfile
from PIL import Image,ImageChops
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'evidencias';OUT.mkdir(exist_ok=True)
html=(ROOT/'ABRIR_T34_T45_CP11.html').read_text()
with zipfile.ZipFile(ROOT/'NV_SCOTT_T45_M2_CP10_v1.0/base_F4/F4_CP03_v1.2_INTACTO.zip') as z:f4=z.read(next(n for n in z.namelist() if n.endswith('ABRIR_PILOTO_F4.html'))).decode()
report={'html_sha256_tested':hashlib.sha256(html.encode()).hexdigest(),'checks':[],'errors':[],'console_errors':[],'requests':[],'profiles':{},'native_file':None,'creative_approval':False,'device':'Headless Chromium / Linux / SwiftShader; mobile emulated'}
def check(name,ok,detail=None):
 report['checks'].append({'name':name,'passed':bool(ok),'detail':detail});print(('PASS ' if ok else 'FAIL ')+name,flush=True)
def png(page,expr):return base64.b64decode(page.evaluate(expr+'.toDataURL().split(",")[1]'))
def sha(b):return hashlib.sha256(b).hexdigest()
def image(page,expr):return Image.open(io.BytesIO(png(page,expr))).convert('RGB')
def wait(page):page.evaluate('()=>new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))')
def go(page,q):
 page.evaluate('(q)=>__T45.go(q)',q);page.wait_for_function('(q)=>Math.abs(__T45.state.q-q)<.0005',arg=q,timeout=60000);wait(page)
def f4go(page,p):page.evaluate('(p)=>{__F4.go(p);__F4.benchmark()}',p);wait(page)
def save(page,name):
 im=Image.open(io.BytesIO(page.screenshot())).convert('RGB');im.save(OUT/name,quality=79)
def watch(page,label):
 page.on('pageerror',lambda e:report['errors'].append({'profile':label,'error':str(e)}))
 page.on('console',lambda m:report['console_errors'].append({'profile':label,'text':m.text}) if m.type=='error' else None)
 page.on('request',lambda r:report['requests'].append(r.url) if r.url.startswith(('http:','https:')) else None)
with sync_playwright() as pw:
 b=pw.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox','--enable-unsafe-swiftshader','--use-gl=angle','--use-angle=swiftshader'])
 for label,w,h,dpr in [('escritorio',1440,900,1),('grande',1920,1080,1),('movil',390,844,2),('horizontal',844,390,1)]:
  context=b.new_context(viewport={'width':w,'height':h},device_scale_factor=dpr,has_touch=label=='movil',is_mobile=label=='movil',offline=True)
  page=context.new_page();watch(page,label)
  if label=='escritorio':
   try:page.goto((ROOT/'ABRIR_T34_T45_CP11.html').as_uri());report['native_file']='opened'
   except Exception as e:report['native_file']=str(e).split('\n')[0]
   page.close();page=context.new_page();watch(page,label)
  page.set_content(html,wait_until='load');page.wait_for_function('window.__T45?.state.ready',timeout=90000);page.wait_for_timeout(500)
  base=context.new_page();watch(base,label+'/baseline');base.set_content(f4,wait_until='load');base.wait_for_function('window.__F4?.state.ready',timeout=90000)
  comparisons=[]
  for p in [0,.2,.4,.6,.8,1]:
   f4go(base,p);page.evaluate('(p)=>__T45.goT34(p)',p);wait(page)
   page.wait_for_function('(p)=>Math.abs(document.querySelector("iframe").contentWindow.__F4.state.progress-p)<.001',arg=p)
   page.evaluate('document.querySelector("iframe").contentWindow.__F4.benchmark()')
   before=png(base,'document.querySelector("canvas")');after=png(page,'document.querySelector("iframe").contentDocument.querySelector("canvas")')
   eq=before==after;comparisons.append({'p':p,'before_sha256':sha(before),'after_sha256':sha(after),'exact':eq})
   check(f'{label}: T34 exacto {p}',eq)
   if label=='escritorio':
    im1=Image.open(io.BytesIO(before)).convert('RGB');im2=Image.open(io.BytesIO(after)).convert('RGB');im1.thumbnail((640,400));im2.thumbnail((640,400));out=Image.new('RGB',(im1.width*2,im1.height));out.paste(im1,(0,0));out.paste(im2,(im1.width,0));out.save(OUT/f'T34_ANTES_DESPUES_{int(p*100):03}.jpg',quality=82)
  # q0 exact framebuffer compare, no replacement of F4 endpoint.
  endpoint=png(page,'document.querySelector("iframe").contentDocument.querySelector("canvas")')
  page.evaluate('__T45.render(0)');check(f'{label}: enlace q0 = F4 p1',png(page,'document.querySelector("#t45")')==endpoint)
  check(f'{label}: dominio T34 conservado',page.evaluate('__T45.state.firstLength')==5.5*h)
  for q in [0,.12,.28,.36,.40,.42,.44,.48,.52,.56,.60,.64,.70,.80,.94,1]:
   if q==0:page.evaluate('__T45.goT34(1)');wait(page)
   else:go(page,q)
   save(page,f'{label}_IDA_{int(q*100):03}.jpg')
  hashes={}
  for q in [.42,.52,.64]:
   go(page,q);a=png(page,'document.querySelector("#t45")');actual=page.evaluate('__T45.state.q');go(page,.9);go(page,q);back=png(page,'document.querySelector("#t45")');page.evaluate('(q)=>__T45.render(q)',actual);direct=png(page,'document.querySelector("#t45")');check(f'{label}: ida/vuelta/directo {q}',a==back==direct,{'actual_q':actual,'sha256':sha(a)});hashes[str(q)]=sha(a)
  for q in [.94,.80,.70,.64,.60,.56,.52,.48,.44,.42,.40,.36,.28,.12,0]:
   if q:go(page,q)
   else:page.evaluate('__T45.goT34(1)');wait(page)
   save(page,f'{label}_VUELTA_{int(q*100):03}.jpg')
  go(page,.5);before=png(page,'document.querySelector("#t45")');n=page.evaluate('__T45.stats.renders');page.wait_for_timeout(5000);check(f'{label}: parada 5 segundos',png(page,'document.querySelector("#t45")')==before and page.evaluate('__T45.stats.renders')==n)
  for q in [.5,.8]:
   go(page,q);page.set_viewport_size({'width':w-30,'height':h-20});page.wait_for_timeout(600);actual=page.evaluate('__T45.state.q');check(f'{label}: resize conserva q={q}',abs(actual-q)<.001,actual);page.set_viewport_size({'width':w,'height':h});page.wait_for_timeout(600)
  go(page,.5);page.locator('#motion').click();wait(page);check(f'{label}: movimiento reducido manual',page.evaluate('__T45.state.reduced'));save(page,f'{label}_REDUCIDO_050.jpg');go(page,1);save(page,f'{label}_REDUCIDO_100.jpg');page.locator('#motion').click();wait(page)
  # Keyboard slider action and on-screen bounds.
  go(page,.5);page.locator('#scrub').focus();old=page.evaluate('__T45.state.q');page.keyboard.press('ArrowRight');wait(page);check(f'{label}: teclado control',page.evaluate('__T45.state.q')>old)
  check(f'{label}: controles visibles',page.locator('#foot').evaluate('(e)=>{const r=e.getBoundingClientRect();return r.top>=0&&r.bottom<=innerHeight+1}'))
  timings=page.evaluate('()=>Array.from({length:100},(_,i)=>__T45.benchmark(.18+.82*(i%50)/49))');timings.sort()
  memory=page.evaluate('performance.memory?{usedJSHeapSize:performance.memory.usedJSHeapSize,totalJSHeapSize:performance.memory.totalJSHeapSize,jsHeapSizeLimit:performance.memory.jsHeapSizeLimit}:null')
  report['profiles'][label]={'viewport':[w,h],'DPR':dpr,'T34':comparisons,'timing_ms':{'samples':100,'median':statistics.median(timings),'p95':timings[94],'max':max(timings)},'memory_JS_only':memory,'reversibility_hashes':hashes,'stats':page.evaluate('({assets:__T45.stats.assets,errors:__T45.stats.errors})')}
  check(f'{label}: geometría cierre sin reapertura',page.evaluate('()=>[.42,.44,.52,.64,1].every(q=>{const g=__T45.geometry(q);return g.closed&&Math.hypot(g.points[0][0]-g.points.at(-1)[0],g.points[0][1]-g.points.at(-1)[1])<.00001})'))
  (OUT/'RESULTADOS_PARCIALES.json').write_text(json.dumps(report,indent=2,ensure_ascii=False))
  context.close()
 # OS reduced preference and WebGL loss fallback in separate contexts.
 c=b.new_context(offline=True,reduced_motion='reduce');page=c.new_page();watch(page,'prefers-reduced');page.set_content(html);page.wait_for_function('window.__T45?.state.ready',timeout=90000);check('Preferencia SO reducida',page.evaluate('__T45.state.reduced'));c.close()
 c=b.new_context(offline=True);c.add_init_script("const original=HTMLCanvasElement.prototype.getContext;HTMLCanvasElement.prototype.getContext=function(t,...a){return t==='webgl'?null:original.call(this,t,...a)}")
 page=c.new_page();page.set_content(html);page.wait_for_function('document.querySelector("#fallback")?.complete',timeout=40000);check('Fallo WebGL: portada y mensaje útil',page.locator('#status').is_visible() and 'WebGL' in page.locator('#status').inner_text());c.close()
 b.close()
check('Offline: cero peticiones HTTP/HTTPS',not report['requests']);check('Sin errores JS normales',not report['errors'],report['errors']);check('Sin errores consola normales',not report['console_errors'],report['console_errors'])
report['passed']=sum(x['passed'] for x in report['checks']);report['failed']=sum(not x['passed'] for x in report['checks']);(OUT/'RESULTADOS.json').write_text(json.dumps(report,indent=2,ensure_ascii=False))
print('TOTAL',report['passed'],'passed',report['failed'],'failed')
