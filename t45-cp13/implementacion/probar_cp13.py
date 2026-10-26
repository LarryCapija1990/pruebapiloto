from pathlib import Path
import json,hashlib,base64,io,zipfile
from PIL import Image,ImageDraw
from playwright.sync_api import sync_playwright
R=Path(__file__).resolve().parents[1];E=R/'evidencias';html=(R/'ABRIR_T34_T45_CP13.html').read_text();old=(R/'REFERENCIA_CP12.html').read_text()
result={'html_sha256':hashlib.sha256(html.encode()).hexdigest(),'checks':[],'errors':[],'console':[],'network':[],'profiles':{},'visual_status':'CP12 appearance accepted by user; CP13 scroll rhythm awaiting review'}
def check(n,ok,d=None):result['checks'].append({'name':n,'passed':bool(ok),'details':d});print(('PASS ' if ok else 'FAIL ')+n,flush=True)
def wait(p):p.evaluate('()=>new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))')
def go(p,v,kind='T45'):
 p.evaluate('([v,kind])=>__T45[kind==="T34"?"goT34":"go"](v)',[v,kind]);p.wait_for_function('([v,k])=>Math.abs(__T45.state[k==="T34"?"p":"q"]-v)<.001',arg=[v,kind]);wait(p)
def png(p,expr='C'):return base64.b64decode(p.evaluate(expr+'.toDataURL().split(",")[1]'))
def image(p):return Image.open(io.BytesIO(p.screenshot())).convert('RGB')
def watch(p,label):
 p.on('pageerror',lambda e:result['errors'].append(label+': '+str(e)))
 p.on('console',lambda m:result['console'].append(label+': '+m.text) if m.type=='error' else None)
 p.on('request',lambda r:result['network'].append(r.url) if r.url.startswith(('http:','https:')) else None)
# Frozen rendering prefix: everything through finish(), before scroll coordination.
base=R.parent/'t45-cp12'
newjs=(R/'implementacion/t45.js').read_text();prefix=newjs[:newjs.index('function lengths()')]
if base.exists():
 oldjs=(base/'implementacion/t45.js').read_text();check('Renderer y cámara CP12 idénticos byte a byte',prefix==oldjs[:oldjs.index('function lengths()')])
 check('Shader de cuerpo CP12 idéntico byte a byte',(R/'implementacion/cuerpo.js').read_bytes()==(base/'implementacion/cuerpo.js').read_bytes())
 check('Máscaras y campos CP12 idénticos',all(p.read_bytes()==(base/'assets'/p.name).read_bytes() for p in (R/'assets').iterdir()))
with sync_playwright() as pw:
 b=pw.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox','--enable-unsafe-swiftshader','--use-gl=angle','--use-angle=swiftshader'])
 for label,w,h,dpr in [('escritorio',1440,900,1),('grande',1920,1080,1),('movil',390,844,2),('horizontal',844,390,1)]:
  c=b.new_context(offline=True,viewport={'width':w,'height':h},device_scale_factor=dpr,is_mobile=label=='movil',has_touch=label=='movil');p=c.new_page();watch(p,label);p.set_content(html);p.wait_for_function('window.__T45?.state.ready',timeout=90000);wait(p)
  before=c.new_page();before.set_content(old);before.wait_for_function('window.__T45?.state.ready',timeout=90000);wait(before)
  lengths=p.evaluate('({first:__T45.state.firstLength,second:__T45.state.secondLength,total:__T45.state.totalLength,actual:document.documentElement.scrollHeight-innerHeight})')
  check(label+': recorrido total reducido',abs(lengths['total']/h-7.57)<1e-9 and abs(lengths['actual']-lengths['total'])<1.1,lengths)
  for v in [0,.10,.35,.65,.90,1]:
   go(p,v,'T34');check(f'{label}: navegación T34 {v}',abs(p.evaluate('__T45.state.p')-v)<.001)
   # Explicit original visual progress in both unedited F4 renderers, apart from integer outer-scroll quantization.
   for page in [p,before]:page.evaluate('(v)=>{frame.contentWindow.__F4.go(v);frame.contentWindow.__F4.benchmark()}',v);wait(page)
   check(f'{label}: imagen T34 sin cambios {v}',png(p,'frame.contentDocument.querySelector("canvas")')==png(before,'frame.contentDocument.querySelector("canvas")'))
  for v in [.18,.32,.35,.39,.64,.80,1]:
   for page in [p,before]:
    go(page,v);page.evaluate('(v)=>__T45.render(v)',v)
   a=png(p);bdata=png(before);check(f'{label}: imagen T45 sin cambios {v}',a==bdata)
   if label in ['escritorio','movil'] and v in [.18,.35,.64,1]:
    im=image(p);im.save(E/f'{label}_CP13_{round(v*1000):04}.jpg',quality=83)
    if label=='escritorio' and v in [.35,.64]:
     ia=Image.open(io.BytesIO(bdata)).convert('RGB');ib=Image.open(io.BytesIO(a)).convert('RGB');ia.thumbnail((640,400));ib.thumbnail((640,400));z=Image.new('RGB',(ia.width*2,ia.height+22),'#101116');z.paste(ia,(0,22));z.paste(ib,(ia.width,22));d=ImageDraw.Draw(z);d.text((8,4),'CP12 / mismo progreso visual',fill='white');d.text((ia.width+8,4),'CP13 / mismo progreso visual',fill='white');z.save(E/f'COMPARACION_{round(v*1000):04}.jpg',quality=85)
  # Actual scroll, not a direct-render shortcut, through both accelerated routes in reverse.
  for kind,v in [('T34',.35),('T34',.86),('T45',.351),('T45',.66)]:
   go(p,v,kind);expr='frame.contentDocument.querySelector("canvas")' if kind=='T34' else 'C';a=png(p,expr);go(p,.97,kind);go(p,v,kind);check(f'{label}: scroll reversible {kind} {v}',png(p,expr)==a)
  go(p,.351);a=png(p);n=p.evaluate('__T45.stats.renders');p.wait_for_timeout(2000);check(label+': pausa sin deriva',a==png(p) and n==p.evaluate('__T45.stats.renders'))
  # Hold is the existing 20vh, not extra distance moved from compressed regions.
  p.evaluate('scrollTo(0,__T45.state.firstLength+.1*innerHeight)');wait(p);check(label+': parada Innervision',p.evaluate('C.hidden&&__T45.state.p===1&&__T45.state.q===0'))
  for kind,v in [('T34',.5),('T45',.351)]:
   go(p,v,kind);p.set_viewport_size({'width':w-20,'height':h-20});p.wait_for_timeout(800);check(f'{label}: resize conserva {kind}',abs(p.evaluate('__T45.state.'+('p' if kind=='T34' else 'q'))-v)<.001);p.set_viewport_size({'width':w,'height':h});p.wait_for_timeout(800)
  go(p,.35);p.locator('#scrub').focus();v=p.evaluate('__T45.state.q');p.keyboard.press('ArrowRight');wait(p);check(label+': control por teclado',p.evaluate('__T45.state.q')>v)
  p.locator('#motion').click();wait(p);check(label+': movimiento reducido',p.evaluate('__T45.state.reduced'));p.locator('#motion').click();wait(p)
  result['profiles'][label]={'viewport':[w,h],'DPR':dpr,'lengths':lengths};c.close()
 b.close()
check('Offline sin HTTP',not result['network']);check('Sin errores JavaScript',not result['errors'],result['errors']);check('Sin errores consola',not result['console'],result['console']);result['passed']=sum(x['passed'] for x in result['checks']);result['failed']=sum(not x['passed'] for x in result['checks']);(E/'NAVEGADOR.json').write_text(json.dumps(result,indent=2,ensure_ascii=False));print('TOTAL',result['passed'],'PASS',result['failed'],'FAIL')
