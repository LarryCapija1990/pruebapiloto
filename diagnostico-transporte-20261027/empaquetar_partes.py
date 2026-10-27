from pathlib import Path
import zipfile,hashlib,json,math
R=Path(__file__).resolve().parent;root=R/'CP13_VISTA_HTTP';dest=R.parent/'descargas'
files=sorted(p for p in root.rglob('*') if p.is_file() and p.name!='CHECKSUMS.sha256')
(root/'CHECKSUMS.sha256').write_text(''.join(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+p.relative_to(root).as_posix()+'\n' for p in files))
groups=[[],[]];sizes=[0,0]
for p in sorted((root/'assets').iterdir(),key=lambda p:p.stat().st_size,reverse=True):
 i=0 if sizes[0]<=sizes[1] else 1;groups[i].append(p);sizes[i]+=p.stat().st_size
for p in root.rglob('*'):
 if p.is_file() and p.parent!=root/'assets':groups[0].append(p)
results=[]
for i,group in enumerate(groups,1):
 p=dest/f'NV_SCOTT_CP13_VISTA_HTTP_PARTE_{i:02}_v1.0.zip'
 with zipfile.ZipFile(p,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
  for f in sorted(group):z.write(f,'CP13_VISTA_HTTP/'+f.relative_to(root).as_posix())
 with zipfile.ZipFile(p) as z:assert z.testzip() is None
 n=p.stat().st_size;expanded=4*math.ceil(n/3);assert expanded<3500000
 results.append({'file':p.name,'bytes':n,'base64_size_if_encoded_bytes':expanded,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
(R/'DESCARGA.json').write_text(json.dumps({'parts':results,'extract_both_into_same_root':True,'image_reencoding':False},indent=2));print(json.dumps(results,indent=2))
