"""Check solid body topology in the packed fields; GPU point probes are separate."""
from pathlib import Path
from PIL import Image
import numpy as np,json
from scipy.ndimage import binary_fill_holes,label
R=Path(__file__).resolve().parents[1]
a=np.asarray(Image.open(R/'assets/campos-cuerpo.png')).astype(float)
f=(a[:,:,0]*256+a[:,:,1])/65535*1024-512;ds,dt=np.split(f,2,axis=0)
rows=[]
for q in np.linspace(.35,.39,41):
 t=np.clip((q-.325)/(.365-.325),0,1);m=t*t*(3-2*t)
 mask=(1-m)*ds+m*dt+10*np.sin(np.pi*m)>=0
 holes=int(np.count_nonzero(binary_fill_holes(mask)&~mask));_,n=label(mask)
 rows.append({'q':round(float(q),4),'holes':holes,'components':n})
report={'method':'Decode packed SDF and evaluate its distance-morph formula at 41 progress values .350–.390. Count holes and components in body alpha >= .5; distinct from actual GPU point probes.','checks':rows,'passed':sum(x['holes']==0 and x['components']==1 for x in rows),'failed':sum(x['holes']!=0 or x['components']!=1 for x in rows)}
(R/'evidencias/TOPOLOGIA_CP12.json').write_text(json.dumps(report,indent=2));print(report['passed'],'solid states;',report['failed'],'failures')
