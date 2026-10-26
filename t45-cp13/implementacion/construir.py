"""Build offline HTML. Python standard library only; original F4 is embedded byte for byte."""
from pathlib import Path
import base64,json,hashlib,zipfile
ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/'NV_SCOTT_T45_M2_CP10_v1.0'
with zipfile.ZipFile(SOURCE/'base_F4/F4_CP03_v1.2_INTACTO.zip') as z:
 name=next(n for n in z.namelist() if n.endswith('ABRIR_PILOTO_F4.html'))
 f4=z.read(name).decode('utf-8')
def data(p):
 mime='image/jpeg' if p.suffix=='.jpg' else 'image/png'
 return 'data:'+mime+';base64,'+base64.b64encode(p.read_bytes()).decode()
images={n:data(SOURCE/p) for n,p in {'salute':'originales/salute.jpg','innervision':'recursos_F4/innervision-original.jpg','space':'recursos_F4/space.png','stars':'recursos_F4/stars.png','symbol':'recursos_F4/symbol.png'}.items()}
images['field']=data(ROOT/'assets/campos-cuerpo.png')
payload=json.dumps({'f4':f4,'images':images},ensure_ascii=False).replace('</','<\\/')
html=(ROOT/'implementacion/index.template.html').read_text().replace('__PACKAGE__',payload).replace('__MODULE__',(ROOT/'implementacion/ritmo.js').read_text()+'\n'+(ROOT/'implementacion/cuerpo.js').read_text()+'\n'+(ROOT/'implementacion/t45.js').read_text())
out=ROOT/'ABRIR_T34_T45_CP13.html';out.write_text(html)
print(out,len(out.read_bytes()),'bytes')
(ROOT/'INTEGRIDAD_BASE.json').write_text(json.dumps({'f4_embedded_sha256':hashlib.sha256(f4.encode()).hexdigest(),'original_standalone_sha256':'e478759325b4ad84a7156507961d72be514cb0be5ee8e3fd732d60d2c7ede1c0','exact_original':hashlib.sha256(f4.encode()).hexdigest()=='e478759325b4ad84a7156507961d72be514cb0be5ee8e3fd732d60d2c7ede1c0'},indent=2))
