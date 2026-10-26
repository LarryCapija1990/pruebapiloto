from pathlib import Path
import hashlib,json,base64
from playwright.sync_api import sync_playwright
R=Path(__file__).resolve().parents[1];html=(R/'ABRIR_T34_T45_CP11.html').read_text();previous=json.loads((R/'evidencias/RESULTADOS.json').read_text());checks=[]
with sync_playwright() as pw:
 b=pw.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox','--enable-unsafe-swiftshader','--use-gl=angle','--use-angle=swiftshader'])
 for label,w,h,dpr in [('escritorio',1440,900,1),('movil',390,844,2)]:
  for q in [.42,.52,.64]:
   c=b.new_context(offline=True,viewport={'width':w,'height':h},device_scale_factor=dpr,is_mobile=label=='movil');p=c.new_page();p.set_content(html);p.wait_for_function('window.__T45?.state.ready',timeout=90000);p.evaluate('(q)=>__T45.go(q)',q);p.wait_for_function('(q)=>Math.abs(__T45.state.q-q)<.001',arg=q);p.evaluate('()=>new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))');png=p.evaluate('C.toDataURL().split(",")[1]');actual=hashlib.sha256(base64.b64decode(png)).hexdigest();expected=previous['profiles'][label]['reversibility_hashes'][str(q)];ok=actual==expected;checks.append({'profile':label,'q':q,'passed':ok,'sha256':actual,'expected':expected});print(('PASS' if ok else 'FAIL'),label,'arranque nuevo q',q,flush=True);c.close()
 b.close()
(R/'evidencias/CARGA_DIRECTA.json').write_text(json.dumps({'html_sha256_tested':hashlib.sha256(html.encode()).hexdigest(),'method':'Fresh browser context and new document per progress; first requested T45 pose after resource readiness, compared against forward/reverse PNG hash. Offline.','checks':checks,'passed':sum(c['passed'] for c in checks),'failed':sum(not c['passed'] for c in checks)},indent=2))
