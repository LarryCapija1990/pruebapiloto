#!/usr/bin/env python3
from pathlib import Path
from zipfile import ZipFile
import hashlib,json,subprocess,sys

ROOT=Path(__file__).resolve().parents[1];HERE=ROOT/'cierre-f4';OUT=HERE/'evidencias';APP=ROOT/'prototipo'
lock=json.loads((HERE/'CONGELACION_CP02.json').read_text())
sha=lambda data:hashlib.sha256(data).hexdigest()
actual={str(p.relative_to(APP)) for p in APP.rglob('*') if p.is_file() and '__pycache__' not in p.parts}
assert actual==set(lock['files']),'Cambió la lista de archivos del runtime'
for name,digest in lock['files'].items():
    if name!='index.html':assert sha((APP/name).read_bytes())==digest,name
base=(HERE/'base-cp02/index.html').read_text()
assert sha((HERE/'base-cp02/index.html').read_bytes())==lock['files']['index.html']
expected=base.replace('Piloto 02: transición reversible de Thunder and Lightning a Innervision. F4 CP01, pendiente de revisión visual.','Piloto 02: Thunder and Lightning a Innervision. Cierre F4 estable; versión CP02 aprobada creativamente para este piloto.')
expected=expected.replace('F4 / CP02 · AJUSTE DEL RAYO','F4 / CP03 · CIERRE ESTABLE').replace('CP05 · Prototipo pendiente de revisión visual','Aprobada creativamente · Piloto 02')
assert (APP/'index.html').read_text()==expected,'Cambios de presentación fuera de los tres textos autorizados'
cp=ROOT/'fuentes/NV_SCOTT_PILOTO02_F3_CP05';manifest=json.loads((cp/'documentacion/MANIFIESTO_CP05.json').read_text())
for record in manifest:assert sha((cp/record['archivo']).read_bytes())==record['sha256'],record['archivo']
archive=ROOT.parent/'descargas/NV_SCOTT_PILOTO02_F4_CP03_v1.2_LOCAL.zip'
before=sha(archive.read_bytes())
run=subprocess.run([sys.executable,str(HERE/'crear_portable.py')],capture_output=True,text=True,check=True)
after=sha(archive.read_bytes());assert before==after,'El ZIP no se reconstruye idéntico en este entorno'
portable=json.loads((HERE/'PORTABLE.json').read_text());assert after==portable['sha256']
with ZipFile(archive) as z:
    assert z.testzip() is None
    for name,record in portable['files'].items():
        path='NV_SCOTT_PILOTO02_F4_CP03_v1.2_LOCAL/'+name
        assert sha(z.read(path))==record['sha256'],name
result={'approved_commit':lock['approved_commit'],'frozen_runtime_files_unchanged':len(lock['files'])-1,'index_changes':'Exactamente tres textos de aprobación/versión; sin cambios de estructura','cp05_hashes_verified':len(manifest),'portable_zip_crc':True,'rebuild_identical_in_this_environment':before==after,'portable_sha256':after,'portable_html_sha256':portable['files']['ABRIR_PILOTO_F4.html']['sha256'],'source_files_preserved':len([p for p in (ROOT/'fuentes').rglob('*') if p.is_file()])}
(OUT/'integridad-y-reconstruccion.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
print(json.dumps(result,ensure_ascii=False))
