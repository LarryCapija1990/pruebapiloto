from pathlib import Path
import json,base64,hashlib,io,statistics
from PIL import Image,ImageChops,ImageDraw
from playwright.sync_api import sync_playwright
R=Path(__file__).resolve().parents[1];E=R/'evidencias';html=(R/'ABRIR_T34_T45_CP12.html').read_text();old=(R/'REFERENCIA_CP11.html').read_text()
report={'html_sha256':hashlib.sha256(html.encode()).hexdigest(),'checks':[],'errors':[],'console':[],'network':[],'profiles':{},'native_file':'Not tested in CP12: managed browser blocked file:// in CP11. Offline DOM loading used; not a claim of native file navigation.','creative_approval':False}
def check(n,ok,d=None):report['checks'].append({'name':n,'passed':bool(ok),'details':d});print(('PASS ' if ok else 'FAIL ')+n,flush=True)
def wait(p):p.evaluate('()=>new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))')
def go(p,q):p.evaluate('(q)=>__T45.go(q)',q);p.wait_for_function('(q)=>Math.abs(__T45.state.q-q)<.0005',arg=q);wait(p)
def shot(p):return Image.open(io.BytesIO(p.screenshot())).convert('RGB')
def data(p,expr='C'):return base64.b64decode(p.evaluate(expr+'.toDataURL().split(",")[1]'))
def watch(p,label):
 p.on('pageerror',lambda e:report['errors'].append(label+': '+str(e)))
 p.on('console',lambda m:report['console'].append(label+': '+m.text) if m.type=='error' else None)
 p.on('request',lambda r:report['network'].append(r.url) if r.url.startswith(('http:','https:')) else None)
Q=[0,.18,.30,.32,.325,.33,.335,.34,.345,.35,.355,.36,.365,.37,.375,.38,.385,.39,.40,.42,.5,.6,.64,.7,.8,.94,1]
with sync_playwright() as pw:
 b=pw.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox','--enable-unsafe-swiftshader','--use-gl=angle','--use-angle=swiftshader'])
 for label,w,h,dpr in [('escritorio',1440,900,1),('grande',1920,1080,1),('movil',390,844,2),('horizontal',844,390,1)]:
  c=b.new_context(offline=True,viewport={'width':w,'height':h},device_scale_factor=dpr,is_mobile=label=='movil',has_touch=label=='movil');p=c.new_page();watch(p,label);p.set_content(html);p.wait_for_function('window.__T45?.state.ready',timeout=90000);wait(p)
  before=c.new_page();before.set_content(old);before.wait_for_function('window.__T45?.state.ready',timeout=90000);wait(before)
  for v in [0,.2,.4,.6,.8,1]:
   for page in [p,before]:
    page.evaluate('(v)=>__T45.goT34(v)',v);page.wait_for_function('(v)=>Math.abs(__T45.state.p-v)<.001',arg=v);wait(page);page.evaluate('frame.contentWindow.__F4.benchmark()')
   check(f'{label}: T34 idéntico p={v}',data(p,'frame.contentDocument.querySelector("canvas")')==data(before,'frame.contentDocument.querySelector("canvas")'))
  endpoint=data(p,'frame.contentDocument.querySelector("canvas")');p.evaluate('__T45.render(0)');check(f'{label}: q0 idéntico F4 p1',data(p)==endpoint)
  for v in Q:
   if v==0:p.evaluate('__T45.goT34(1)');wait(p)
   else:go(p,v)
   if label in ['escritorio','movil'] or v in [.32,.35,.365,.39,.64,1]:shot(p).save(E/f'{label}_IDA_{round(v*1000):04}.jpg',quality=83)
   if label in ['escritorio','movil'] and v in [.32,.35,.365,.39,.5,.64]:
    go(before,v);a=shot(before);z=shot(p);a.thumbnail((640,420));z.thumbnail((640,420));out=Image.new('RGB',(a.width*2,a.height+22),'#101116');out.paste(a,(0,22));out.paste(z,(a.width,22));dr=ImageDraw.Draw(out);dr.text((8,4),'CP11 ANTES',fill='white');dr.text((a.width+8,4),'CP12 DESPUES',fill='white');out.save(E/f'{label}_COMPARACION_{round(v*1000):04}.jpg',quality=85)
  go(p,.320);bg1=Image.open(io.BytesIO(data(p))).convert('RGB');go(p,.334);bg2=Image.open(io.BytesIO(data(p))).convert('RGB');delta=ImageChops.difference(bg1.crop((0,0,100,100)),bg2.crop((0,0,100,100))).getbbox();check(f'{label}: encendido no ilumina fondo de pantalla',delta is None)
  for v in [.333,.351,.378]:
   go(p,v);initial=data(p);actual=p.evaluate('__T45.state.q');go(p,.8);go(p,v);back=data(p);p.evaluate('(v)=>__T45.render(v)',actual);direct=data(p);check(f'{label}: inversión dentro del tramo q={v}',initial==back==direct,hashlib.sha256(initial).hexdigest())
  go(p,.351);a=data(p);count=p.evaluate('__T45.stats.renders');p.wait_for_timeout(5000);check(f'{label}: pausa 5s dentro del cambio',data(p)==a and p.evaluate('__T45.stats.renders')==count)
  for v in [.39,.375,.365,.355,.345,.335,.325,.32,.3]:
   go(p,v)
   if label in ['escritorio','movil']:shot(p).save(E/f'{label}_VUELTA_{round(v*1000):04}.jpg',quality=83)
  # Shader body: once the spade exists, its center is solid, no residual vertical axis.
  result=p.evaluate('''()=>{renderBody(.390);const gl=bodyGL;function sample(x,y){const a=new Uint8Array(4);gl.readPixels(x,599-y,1,1,gl.RGBA,gl.UNSIGNED_BYTE,a);return [...a]}return {center:sample(524,350),upperAxis:sample(524,120),lowerAxis:sample(524,535),error:gl.getError()}}''')
  check(f'{label}: pica sólida y sin eje residual',result['center'][3]>250 and result['upperAxis'][3]==0 and result['lowerAxis'][3]==0,result)
  check(f'{label}: GL sin error',result['error']==0)
  for v in [.351,.8]:
   go(p,v);p.set_viewport_size({'width':w-20,'height':h-20});p.wait_for_timeout(900);check(f'{label}: resize q={v}',abs(p.evaluate('__T45.state.q')-v)<.001);p.set_viewport_size({'width':w,'height':h});p.wait_for_timeout(900)
  go(p,.35);p.locator('#motion').click();wait(p);check(f'{label}: modo reducido',p.evaluate('__T45.state.reduced'));p.locator('#motion').click();wait(p)
  p.locator('#scrub').focus();v=p.evaluate('__T45.state.q');p.keyboard.press('ArrowRight');wait(p);check(f'{label}: teclado',p.evaluate('__T45.state.q')>v)
  check(f'{label}: controles a la vista',p.locator('#foot').evaluate('(e)=>e.getBoundingClientRect().bottom<=innerHeight+1'))
  # Readback timings are software measurements, not actual display FPS.
  t=p.evaluate('()=>Array.from({length:60},(_,i)=>__T45.benchmark(.30+.12*(i%30)/29))');t.sort();report['profiles'][label]={'viewport':[w,h],'dpr':dpr,'rapid_segment_ms':{'samples':60,'median':statistics.median(t),'p95':t[56],'max':max(t)},'texture_entry':p.evaluate('()=>{const out=[];for(let q=.39;q<1;q+=.001){const a=__T45.camera(q);if(a.photoScale<=2.8){out.push({q,source_pixel_css_size:a.photoScale});break}}return out[0]}')}
  c.close()
 # Cold load into three interior progress values, independently.
 for v in [.333,.351,.378]:
  c=b.new_context(offline=True,viewport={'width':1440,'height':900});p=c.new_page();p.set_content(html);p.wait_for_function('window.__T45?.state.ready',timeout=90000);go(p,v);a=data(p);go(p,.8);go(p,v);check(f'Arranque nuevo/interior {v}',data(p)==a);c.close()
 b.close()
check('Sin errores JavaScript',not report['errors'],report['errors']);check('Sin errores de consola',not report['console'],report['console']);check('Offline sin peticiones HTTP',not report['network']);report['passed']=sum(x['passed'] for x in report['checks']);report['failed']=sum(not x['passed'] for x in report['checks']);(E/'RESULTADOS_CP12.json').write_text(json.dumps(report,indent=2,ensure_ascii=False));print('TOTAL',report['passed'],'PASS',report['failed'],'FAIL')
