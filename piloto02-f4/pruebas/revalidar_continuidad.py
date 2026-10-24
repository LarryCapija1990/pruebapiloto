#!/usr/bin/env python3
"""Repite las comprobaciones de imagen con remuestreo de alta calidad explícito.

La ejecución completa anterior ya validó los flujos. Se conserva su registro y se
actualizan únicamente las tres comprobaciones de continuidad realmente repetidas.
"""
from pathlib import Path
from playwright.sync_api import sync_playwright
from PIL import Image
import numpy as np
import json,io,base64,hashlib,os,shutil

root=Path(__file__).resolve().parents[1];out=root/'evidencias'
old=json.loads((out/'resultados-pruebas.json').read_text())
shutil.copy2(out/'resultados-pruebas.json',out/'diagnostico-tercera-ejecucion.json')
checks=[];diffs=[];joins=[]
def check(name,ok,details):checks.append({'name':name,'passed':bool(ok),'details':details});print(('PASS ' if ok else 'FAIL ')+name,flush=True)
with sync_playwright() as pw:
 b=pw.chromium.launch(executable_path=os.environ.get('F4_CHROMIUM','/usr/bin/chromium'),headless=True,args=['--no-sandbox','--enable-unsafe-swiftshader','--use-gl=angle','--use-angle=swiftshader'])
 page=b.new_page(viewport={'width':1440,'height':900},device_scale_factor=1)
 page.goto(os.environ.get('F4_URL','http://127.0.0.1:4173'),wait_until='networkidle');page.wait_for_function('window.__F4?.state.ready')
 def sample(v):
  page.evaluate('(v)=>window.__F4.go(v)',v);page.wait_for_function('(v)=>Math.abs(window.__F4.state.progress-v)<.001',arg=v)
  page.evaluate('()=>new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))')
  data=page.evaluate('''()=>{const c=document.createElement('canvas');c.width=320;c.height=180;const x=c.getContext('2d');x.imageSmoothingQuality='high';x.drawImage(document.querySelector('canvas'),0,0,320,180);return c.toDataURL().split(',')[1]}''')
  return np.array(Image.open(io.BytesIO(base64.b64decode(data))).convert('RGB'),dtype=float)
 hashes=[];previous=None
 for i in range(201):
  a=sample(i/200);hashes.append(hashlib.sha256(a.tobytes()).hexdigest())
  if previous is not None:diffs.append({'to_percent':i/2,'mean_abs_rgb_255':float(np.mean(abs(a-previous)))})
  previous=a
 check('Continuidad: 201 estados distintos en todo el recorrido',len(set(hashes))==201,{'unique':len(set(hashes)),'hashes':hashes})
 check('Continuidad: ningún salto >15/255 en promedio a pasos de 0.5%',max(x['mean_abs_rgb_255'] for x in diffs)<15,{'maximum':max(diffs,key=lambda x:x['mean_abs_rgb_255'])})
 for center in [.1,.4,.5,.6,.65,.7,.8,.9,.95,.99]:
  trio=[sample(v) for v in [center-.001,center,center+.001]]
  joins.append({'percent':center*100,'left_diff':float(np.mean(abs(trio[1]-trio[0]))),'right_diff':float(np.mean(abs(trio[2]-trio[1])))})
 check('Empalmes: sin discontinuidad >5/255 a ambos lados ±0.1%',all(max(j['left_diff'],j['right_diff'])<5 for j in joins),joins)
 b.close()
result={'sampling':'RGB 320×180, Canvas2D imageSmoothingQuality=high; por defecto low produjo alias de grano y métricas falsas de salto. Contraste de diagnóstico a 39.9→40%: low=6.1016, high=1.9894, Pillow bicúbico=1.9545 /255.','checks':checks,'continuity':diffs,'joins':joins}
(out/'revalidacion-continuidad.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
by_name={c['name']:c for c in checks}
old['checks']=[by_name.get(c['name'],c) for c in old['checks']]
old['profiles']['escritorio']['continuity']=diffs
old['verification_runs']=['ejecucion-pruebas.log: flujos, capturas, reversibilidad, movimiento reducido, fallos de carga y WebGL','revalidacion-continuidad.json: 201 posiciones y 10 empalmes repetidos con filtrado de imagen correcto']
old['summary']['passed']=sum(c['passed'] for c in old['checks']);old['summary']['failed']=sum(not c['passed'] for c in old['checks'])
(out/'resultados-pruebas.json').write_text(json.dumps(old,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(old['summary'],ensure_ascii=False));raise SystemExit(0 if all(c['passed'] for c in checks) else 1)
