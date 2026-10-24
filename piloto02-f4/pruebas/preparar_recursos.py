#!/usr/bin/env python3
"""Recrea recursos runtime desde CP05 y los originales de CP04, sin modificar fuentes."""
from pathlib import Path
from PIL import Image
import numpy as np
import shutil,json,hashlib

r=Path(__file__).resolve().parents[1]
c=r/'fuentes/NV_SCOTT_PILOTO02_F3_CP05'
a=r/'prototipo/assets';a.mkdir(exist_ok=True)
files={
 'thunder-scene.png':c/'capas/C03_SIN_RAYO_RGB.png',
 'space.png':c/'capas/ESPACIO_BASE_RGB.png',
 'stars.png':c/'capas/ESTRELLAS_RGBA.png',
 'symbol.png':c/'capas/SIGNO_ORIGINAL_RGBA.png',
 'lightning.png':c/'capas/C03_RAYO_ORIGINAL_RGBA.png',
 'thunder-original.jpg':r/'fuentes/NV_SCOTT_PILOTO02_F3_CP04/originales/thunder.jpg',
 'innervision-original.jpg':r/'fuentes/NV_SCOTT_PILOTO02_F3_CP04/originales/innervision.jpg',
}
manifest=[]
for name,p in files.items():
 shutil.copy2(p,a/name)
 manifest.append({'runtime':name,'source':str(p.relative_to(r)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
field=Image.open(c/'mascaras/CAMPO_APARICION_ESPACIO.png').convert('L')
sky=Image.open(c/'mascaras/CIELO_OSCURO_INICIAL.png').convert('L')
Image.merge('RGB',(field,sky,Image.new('L',field.size))).save(a/'reveal-field.png')
manifest.append({'runtime':'reveal-field.png','channels':{'R':'fuentes/NV_SCOTT_PILOTO02_F3_CP05/mascaras/CAMPO_APARICION_ESPACIO.png','G':'fuentes/NV_SCOTT_PILOTO02_F3_CP05/mascaras/CIELO_OSCURO_INICIAL.png','B':'0'},'operation':'Empaquetado sin remuestreo, 1066×600'})
states=[]
for pct in range(20,81,10):
 im=np.array(Image.open(c/f'estados/p{pct:03}_RAYO_EJE_RGBA.png'))
 alpha=im[:,:,3];ys,xs=np.where(alpha>12);top=int(ys.min());bottom=int(ys.max());points=[]
 for t in np.linspace(0,1,16):
  y=bottom-(bottom-top)*t;weights=alpha[round(y)].astype(float)
  points.append([round(float((np.arange(1066)*weights).sum()/weights.sum()),4),round(float(y),4)])
 states.append({'progress':pct/100,'points':points})
(a/'line-geometry.json').write_text(json.dumps(states,indent=2)+'\n')
manifest.append({'runtime':'line-geometry.json','sources':'fuentes/NV_SCOTT_PILOTO02_F3_CP05/estados/p020…p080_RAYO_EJE_RGBA.png','operation':'16 centroides de alfa por fila por geometría, umbral de caja alfa>12; Catmull–Rom en app.js'})
(a/'PROVENIENCIA.json').write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+'\n')
print('8 imágenes runtime y geometría generadas. Masters sin modificar.')
