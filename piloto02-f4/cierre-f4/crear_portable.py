#!/usr/bin/env python3
"""Empaqueta el renderer aprobado sin modificarlo: HTML local sin servidor.

Solo adapta importación y carga de recursos. Los píxeles se comparan en navegador
con el runtime HTTP y con CP02, no se presupone equivalencia por construcción.
"""
from pathlib import Path
from zipfile import ZipFile,ZipInfo,ZIP_DEFLATED
import base64,json,hashlib,sys

ROOT=Path(__file__).resolve().parents[1]
REPO=ROOT.parent
APP=ROOT/'prototipo'
OUT=REPO/'descargas'
OUT.mkdir(exist_ok=True)
NAME='NV_SCOTT_PILOTO02_F4_CP03_v1.2_LOCAL'

def js_string(text):
    return json.dumps(text,ensure_ascii=True).replace('<','\\u003c')

images={}
for file in ['thunder-scene.png','space.png','stars.png','symbol.png','reveal-field.png','lightning.png','thunder-original.jpg','innervision-original.jpg']:
    p=APP/'assets'/file
    mime='image/jpeg' if file.endswith('.jpg') else 'image/png'
    images[file]='data:'+mime+';base64,'+base64.b64encode(p.read_bytes()).decode('ascii')
motif=(APP/'motif.js').read_text().replace('export function ','function ')
prefix='const createMotif=(()=>{\n'+motif+'\nreturn createMotif;})();\n'
prefix+='const EMBEDDED_IMAGES='+json.dumps(images,separators=(',',':'))+';\n'
script=(APP/'app.js').read_text()
assert script.count("import { createMotif } from './motif.js';")==1
script=script.replace("import { createMotif } from './motif.js';",prefix)
changes={
    'img.src = `assets/${name}`;':'img.src = EMBEDDED_IMAGES[name];',
    "fetch('scene.frag')":'Promise.resolve(new Response('+js_string((APP/'scene.frag').read_text())+'))',
    "fetch('assets/line-geometry.json')":'Promise.resolve(new Response('+js_string((APP/'assets/line-geometry.json').read_text())+'))',
    'a.href = `assets/${src}`;':'a.href = EMBEDDED_IMAGES[src]; a.download=src;',
}
for old,new in changes.items():
    assert script.count(old)==1,old
    script=script.replace(old,new)
assert '</script' not in script.lower()
html=(APP/'index.html').read_text()
assert html.count('<link rel="stylesheet" href="style.css">')==1
html=html.replace('<link rel="stylesheet" href="style.css">','<style>\n'+(APP/'style.css').read_text()+'\n</style>')
html=html.replace('<script type="module" src="app.js"></script>','<script type="module">\n'+script+'\n</script>')
html=html.replace('Este prototipo requiere JavaScript. Los originales están disponibles en assets/thunder-original.jpg y assets/innervision-original.jpg.','Activa JavaScript en Chrome o Edge para visualizar el piloto local. No requiere servidor ni Python.')
guide='''<!doctype html><html lang="es"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Cómo ver el piloto F4</title><style>body{max-width:760px;margin:50px auto;padding:0 24px;font:18px/1.65 system-ui;background:#0b0e15;color:#f0ece4}a{color:#f0c391}h1{font-family:Georgia,serif;font-weight:normal}li{margin:18px 0}</style><h1>Ver el piloto F4</h1><p>Thunder and Lightning → Innervision. Aprobada creativamente para este piloto.</p><ol><li>Extrae todos los archivos del ZIP en una carpeta nueva. En Windows: clic derecho sobre el ZIP → «Extraer todo».</li><li>Haz doble clic en <b>ABRIR_PILOTO_F4.html</b>. Si no se abre en un navegador, clic derecho → «Abrir con» → Chrome o Edge.</li><li>Mueve la rueda del ratón o desliza. El control «Recorrido» permite parar en cualquier punto y regresar. «Reducir movimiento» fija la cámara.</li></ol><p><a href="ABRIR_PILOTO_F4.html">Abrir el piloto ahora</a></p><p>No necesitas instalar Python, usar VS Code, abrir una terminal ni mantener una conexión a Internet. Todos los recursos están dentro del HTML. El navegador necesita JavaScript y WebGL habilitados.</p><p>Cabecera esperada: <b>F4 / CP03 · CIERRE ESTABLE</b>. La geometría y el movimiento son los de CP02 aprobada; CP03 solo documenta y empaqueta su cierre.</p><p>Si aparece un problema, abre el archivo en Chrome o Edge actualizado. Si la ventana solo permite previsualizar un archivo, ábrelo con el navegador completo; algunos visores móviles no ejecutan JavaScript. Para asistencia, conserva el mensaje de error que aparezca en pantalla.</p></html>'''
readme='''PILOTO 02 — CIERRE F4 / CP03 v1.2

1. Extrae TODO el ZIP en una carpeta nueva.
2. Haz doble clic en ABRIR_PILOTO_F4.html y ábrelo en Chrome o Edge.
3. Usa scroll o el control Recorrido. Puedes regresar y detenerte en cualquier punto.

No necesitas Python, terminal, VS Code, servidor ni conexión a Internet.
También puedes abrir LEEME_PRIMERO.html para ver la guía ilustrada por pasos.
No abras el piloto dentro del ZIP ni desde un visor móvil que no ejecute JavaScript.

La versión CP02 fue aprobada creativamente por el usuario para este piloto.
CP03 congela ese movimiento y registra las pruebas de cierre. No incluye otros álbumes.
El código fuente y la documentación completa se conservan en:
https://github.com/LarryCapija1990/pruebapiloto
Checkpoint acumulativo recuperable:
https://github.com/LarryCapija1990/pruebapiloto/archive/refs/tags/piloto02-f4-cierre-v1.2.zip
'''
files={'ABRIR_PILOTO_F4.html':html.encode('utf-8'),'LEEME_PRIMERO.html':guide.encode('utf-8'),'LEEME.txt':readme.encode('utf-8')}
artifact=OUT/(NAME+'.zip')
with ZipFile(artifact,'w',compression=ZIP_DEFLATED,compresslevel=9) as z:
    for name,data in files.items():
        info=ZipInfo(NAME+'/'+name,date_time=(2026,10,24,0,0,0))
        info.compress_type=ZIP_DEFLATED;info.external_attr=0o100644<<16
        z.writestr(info,data,compress_type=ZIP_DEFLATED,compresslevel=9)
with ZipFile(artifact) as z:assert z.testzip() is None
record={'artifact':str(artifact.relative_to(REPO)),'bytes':artifact.stat().st_size,'sha256':hashlib.sha256(artifact.read_bytes()).hexdigest(),
    'files':{name:{'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()} for name,data in files.items()},
    'source_hashes':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(APP.rglob('*')) if p.is_file() and '__pycache__' not in p.parts},
    'derivation':'CSS, módulo de motivo, shader, geometría y ocho imágenes embebidos; solo se adapta la carga, se conserva el algoritmo aprobado. Validar píxeles con verificar_cierre.py.',
    'python':sys.version.split()[0]}
record_path=ROOT/'cierre-f4/PORTABLE.json';record_path.write_text(json.dumps(record,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'artifact':record['artifact'],'bytes':record['bytes'],'sha256':record['sha256']}))
