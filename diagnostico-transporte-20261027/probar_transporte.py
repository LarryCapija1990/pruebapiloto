"""No set_content, base64 returns or screenshots. Log only wire metadata and hashes."""
from pathlib import Path
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from functools import partial
from urllib.parse import urlsplit
import threading,json,hashlib,os
from playwright.sync_api import sync_playwright
os.environ.pop('DEBUGP',None)
R=Path(__file__).resolve().parent;bundle=R/'CP13_VISTA_HTTP';approved=R.parent/'t45-cp13/ABRIR_T34_T45_CP13.html';BUDGET=262144
report={'original_error':{'message':'decoded message length too large: found 4554464 bytes, limit 4194304','source':'reported by user when opening chat or preview','exact_original_call':'not observable: client trace not available','reproduced':False},'retry':'Page.goto(local HTTP URL), browser-side PNG digest; no large data returned','wire_scope':'Playwright Python–Node connection after initialization; not the Codex client/API transport','budget_bytes':BUDGET,'messages':[],'checks':[],'browser_errors':[],'http_errors':[]}
def check(n,ok,detail=None):report['checks'].append({'name':n,'passed':bool(ok),'details':detail});print(('PASS ' if ok else 'FAIL ')+n,flush=True)
class Handler(SimpleHTTPRequestHandler):
 def translate_path(self,path):
  if urlsplit(path).path=='/accepted/index.html':return str(approved)
  return super().translate_path(path)
 def log_message(self,*a):pass
 def send_error(self,code,message=None,explain=None):report['http_errors'].append({'status':code,'path':self.path[:160]});return super().send_error(code,message,explain)
server=ThreadingHTTPServer(('127.0.0.1',0),partial(Handler,directory=str(bundle)));thread=threading.Thread(target=server.serve_forever,daemon=True);thread.start();url=f'http://127.0.0.1:{server.server_address[1]}'
def digest(p,kind):
 return p.evaluate('''async(kind)=>{const c=kind==='T34'?document.getElementById('base').contentDocument.getElementById('scene'):document.getElementById('t45');const blob=await new Promise(r=>c.toBlob(r,'image/png'));const bytes=await blob.arrayBuffer();const sha=[...new Uint8Array(await crypto.subtle.digest('SHA-256',bytes))].map(v=>v.toString(16).padStart(2,'0')).join('');return {sha256:sha,png_bytes:blob.size,width:c.width,height:c.height}}''',kind)
def wait(p):p.evaluate('()=>new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))')
try:
 with sync_playwright() as pw:
  transport=pw._impl_obj._connection._transport;send=transport.send;receive=transport.deserialize_message
  def audit_send(message):
   size=len(json.dumps(message).encode('utf-8'));method=message.get('method');params=message.get('params',{});entry={'direction':'send','method':method,'bytes':size,'parameter_names':list(params)}
   if method=='goto':entry['url']=params.get('url')
   report['messages'].append(entry)
   if size>BUDGET:raise RuntimeError(f'Preflight blocked {method}: {size} bytes, budget {BUDGET}')
   return send(message)
  def audit_receive(data):
   size=len(data.encode('utf8') if isinstance(data,str) else data)
   if size>BUDGET:raise RuntimeError(f'Receive budget exceeded: {size} bytes, budget {BUDGET}')
   message=receive(data);report['messages'].append({'direction':'receive','method':message.get('method'),'reply_to':message.get('id'),'bytes':size});return message
  transport.send=audit_send;transport.deserialize_message=audit_receive
  b=pw.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox','--enable-unsafe-swiftshader','--use-gl=angle','--use-angle=swiftshader'])
  for label,w,h,dpr in [('desktop',1440,900,1),('mobile_emulated',390,844,2)]:
   c=b.new_context(viewport={'width':w,'height':h},device_scale_factor=dpr,is_mobile=label.startswith('mobile'))
   pages=[]
   for endpoint in ['/index.html','/accepted/index.html']:
    p=c.new_page();p.on('pageerror',lambda e:report['browser_errors'].append(str(e)[:200]));response=p.goto(url+endpoint);check(label+' HTTP '+endpoint,response.status==200);p.wait_for_function('window.__T45?.state.ready',timeout=90000);wait(p);pages.append(p)
   for kind,values in [('T34',[0,.5,1]),('T45',[.35,.64,1])]:
    for v in values:
     results=[]
     for p in pages:
      if kind=='T34':p.evaluate('(v)=>{const f=document.getElementById("base").contentWindow.__F4;f.go(v);f.benchmark()}',v);wait(p)
      else:p.evaluate('(v)=>{__T45.go(v)}',v);p.wait_for_function('(v)=>Math.abs(__T45.state.q-v)<.001',arg=v);wait(p);p.evaluate('(v)=>__T45.render(v)',v)
      results.append(digest(p,kind))
     check(f'{label} same pixels {kind} {v}',results[0]['sha256']==results[1]['sha256'],{'externalized':results[0],'accepted':results[1]})
   p=pages[0];p.evaluate('__T45.go(.351)');p.wait_for_function('Math.abs(__T45.state.q-.351)<.001');wait(p);a=digest(p,'T45');p.evaluate('__T45.go(.8)');wait(p);p.evaluate('__T45.go(.351)');wait(p);check(label+' reversible',digest(p,'T45')['sha256']==a['sha256'])
   a=digest(p,'T45');p.wait_for_timeout(1500);check(label+' paused',digest(p,'T45')['sha256']==a['sha256']);c.close()
  b.close()
 check('No setContent or screenshot wire calls',not any(x.get('method') in ['setContent','screenshot'] for x in report['messages']))
 check('No browser JS errors',not report['browser_errors'],report['browser_errors']);check('No HTTP errors',not report['http_errors'],report['http_errors'])
except Exception as e:
 report['test_exception']={'type':type(e).__name__,'message':str(e)[:220]};check('Safe retry completed',False,report['test_exception'])
finally:
 server.shutdown();server.server_close();report['max_send_bytes']=max((m['bytes'] for m in report['messages'] if m['direction']=='send'),default=0);report['max_receive_bytes']=max((m['bytes'] for m in report['messages'] if m['direction']=='receive'),default=0);report['passed']=sum(c['passed'] for c in report['checks']);report['failed']=sum(not c['passed'] for c in report['checks']);(R/'PRUEBA_TRANSPORTE.json').write_text(json.dumps(report,indent=2));print(json.dumps({k:report[k] for k in ['passed','failed','max_send_bytes','max_receive_bytes']}))
