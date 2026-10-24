#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
from PIL import Image
import json,hashlib

root=Path(__file__).resolve().parents[1]
cp=root/'fuentes/NV_SCOTT_PILOTO02_F3_CP05'
manifest=json.loads((cp/'documentacion/MANIFIESTO_CP05.json').read_text())
errors=[]
for record in manifest:
 p=cp/record['archivo']
 if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=record['sha256']:errors.append(record['archivo'])
for folder in ['capas','mascaras','documentacion','estados','escenarios','fotogramas']:
 if not (cp/folder).is_dir():errors.append(folder)
originals={}
for name in ['thunder','innervision']:
 p=root/f'fuentes/NV_SCOTT_PILOTO02_F3_CP04/originales/{name}.jpg'
 originals[name]={'size':list(Image.open(p).size),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
runtime=json.loads((root/'prototipo/assets/PROVENIENCIA.json').read_text())
for record in runtime:
 if 'sha256' in record:
  p=root/'prototipo/assets'/record['runtime']
  if hashlib.sha256(p.read_bytes()).hexdigest()!=record['sha256']:errors.append('runtime/'+record['runtime'])
result={'cp05_manifest_entries':len(manifest),'errors':errors,'originals':originals,'source_files':len([p for p in (root/'fuentes').rglob('*') if p.is_file()]),'cp05_reference_frames':len(list((cp/'fotogramas').glob('*.png')))}
(root/'evidencias/integridad-fuentes.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
print(json.dumps(result,ensure_ascii=False))
raise SystemExit(1 if errors else 0)
