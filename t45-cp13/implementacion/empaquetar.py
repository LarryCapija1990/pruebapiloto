from pathlib import Path
import hashlib,zipfile,json
R=Path(__file__).resolve().parents[1];D=R.parent/'descargas';D.mkdir(exist_ok=True)
LIMIT=32*1024*1024
# The tree is the entire isolated CP10 + CP13 delivery, not the historic 210 MB F4 archive.
files=sorted(p for p in R.rglob('*') if p.is_file() and p.name!='MANIFIESTO.sha256' and '__pycache__' not in p.parts)
assert all(p.stat().st_size<LIMIT for p in files)
(R/'MANIFIESTO.sha256').write_text(''.join(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+p.relative_to(R).as_posix()+'\n' for p in files))
def write_zip(name,entries):
 dest=D/name
 with zipfile.ZipFile(dest,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
  for path,data in entries:
   i=zipfile.ZipInfo(path,(2026,10,26,0,0,0));i.compress_type=zipfile.ZIP_DEFLATED;i.external_attr=0o100644<<16;z.writestr(i,data,compresslevel=6)
 assert dest.stat().st_size<LIMIT,(dest,dest.stat().st_size)
 with zipfile.ZipFile(dest) as z:assert z.testzip() is None
 return {'file':name,'bytes':dest.stat().st_size,'sha256':hashlib.sha256(dest.read_bytes()).hexdigest()}
prefix='NV_SCOTT_T45_M2_CP13_v1.0'
readme=(R/'LEEME.html').read_text().replace('<p><a href="REVISION_SECUENCIAL.html">Ver capturas de ida y vuelta y comparación F4</a></p>','<p>Las fuentes, capturas y pruebas están en el ZIP FUENTES_Y_EVIDENCIAS del mismo checkpoint CP13. Esta carpeta contiene la versión local autocontenida.</p>')
local=write_zip(prefix+'_LOCAL.zip',[(prefix+'/ABRIR_T34_T45_CP13.html',(R/'ABRIR_T34_T45_CP13.html').read_bytes()),(prefix+'/LEEME_PRIMERO.html',readme.encode()),(prefix+'/LEEME.txt',('Extrae el ZIP completo. Abre LEEME_PRIMERO.html o ABRIR_T34_T45_CP13.html con Chrome o Edge. No necesita Python ni conexión. No abrir desde dentro del ZIP.\nF4 intacto; T45 para revisión, sin aprobación creativa.\nSi un equipo corporativo bloquea HTML/WebGL local, consulta las instrucciones con servidor en el paquete de fuentes.').encode())])
full=write_zip(prefix+'_FUENTES_Y_EVIDENCIAS.zip',[(prefix+'/'+p.relative_to(R).as_posix(),p.read_bytes()) for p in sorted(R.rglob('*')) if p.is_file() and '__pycache__' not in p.parts])
result={'checkpoint':prefix,'max_file_bytes':max(p.stat().st_size for p in files),'manifest_entries':len(files),'packages':[local,full]};
# Outside the package avoids a self-referential ZIP hash.
(D/(prefix+'_DESCARGAS.json')).write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2))
