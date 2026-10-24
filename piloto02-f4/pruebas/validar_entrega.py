#!/usr/bin/env python3
"""Extrae el ZIP ligero y prueba su arranque en otra carpeta y puerto libres."""
from pathlib import Path
from tempfile import TemporaryDirectory
from zipfile import ZipFile
from playwright.sync_api import sync_playwright
import json,subprocess,socket,time,urllib.request,os,sys,base64,hashlib

root=Path(__file__).resolve().parents[1]
archive=Path(sys.argv[1])
with TemporaryDirectory(prefix='f4-entrega-') as tmp:
 tmp=Path(tmp)
 with ZipFile(archive) as z:
  assert z.testzip() is None
  for n in z.namelist():assert (tmp/n).resolve().is_relative_to(tmp)
  z.extractall(tmp)
 servers=list(tmp.rglob('server.py'));assert len(servers)==1
 with socket.socket() as s:s.bind(('127.0.0.1',0));port=s.getsockname()[1]
 proc=subprocess.Popen([sys.executable,str(servers[0]),'--port',str(port)],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL,cwd=tmp)
 try:
  url=f'http://127.0.0.1:{port}'
  for _ in range(100):
   try:
    with urllib.request.urlopen(url,timeout=1) as response:assert response.status==200
    break
   except OSError:time.sleep(.1)
  else:raise RuntimeError('El servidor extraído no inicia')
  with sync_playwright() as pw:
   b=pw.chromium.launch(executable_path=os.environ.get('F4_CHROMIUM','/usr/bin/chromium'),headless=True,args=['--no-sandbox','--enable-unsafe-swiftshader','--use-gl=angle','--use-angle=swiftshader'])
   page=b.new_page(viewport={'width':1280,'height':800});errors=[]
   page.on('pageerror',lambda e:errors.append(str(e)))
   page.on('console',lambda m:errors.append(m.text) if m.type=='error' else None)
   page.goto(url,wait_until='networkidle');page.wait_for_function('window.__F4?.state.ready')
   hashes=[]
   for p in [0,.6,.3,.6,1]:
    page.evaluate('(p)=>window.__F4.go(p)',p);page.wait_for_function('(p)=>Math.abs(window.__F4.state.progress-p)<.001',arg=p)
    page.evaluate('()=>new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))')
    encoded=page.evaluate("document.querySelector('canvas').toDataURL().split(',')[1]")
    hashes.append(hashlib.sha256(base64.b64decode(encoded)).hexdigest())
   result={'archive':archive.name,'zip_crc_ok':True,'clean_extraction_startup':True,'independent_directory_and_port':True,'route':[0,60,30,60,100],'same_pixels_at_60':hashes[1]==hashes[3],'distinct_endpoints':hashes[0]!=hashes[-1],'console_and_page_errors':errors,'assets_loaded':page.evaluate('window.__F4.metrics.assets')}
   b.close();assert result['same_pixels_at_60'] and result['distinct_endpoints'] and not errors and result['assets_loaded']==8
 finally:
  proc.terminate();proc.wait(timeout=10)
(root/'evidencias/validacion-entrega.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
print(json.dumps(result,ensure_ascii=False))
