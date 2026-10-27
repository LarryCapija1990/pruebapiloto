"""Externalize, never recompress, inline CP13 resources. Accepted source is read-only."""
from pathlib import Path
import re,json,base64,hashlib,shutil
R=Path(__file__).resolve().parent;source=R.parent/'t45-cp13/ABRIR_T34_T45_CP13.html';out=R/'CP13_VISTA_HTTP';(out/'assets').mkdir(parents=True,exist_ok=True);(out/'f4').mkdir(exist_ok=True)
s=source.read_text();match=re.search(r'<script>const PACKAGE=(.*?);</script>',s,re.S);assert match
package=json.loads(match.group(1));resources={};uses=[]
def externalize(uri,prefix,role):
 header,data=uri.split(',',1);raw=base64.b64decode(data,validate=True);digest=hashlib.sha256(raw).hexdigest();ext='.jpg' if 'image/jpeg' in header else '.png';name=digest+ext
 path=out/'assets'/name
 if not path.exists():path.write_bytes(raw)
 assert path.read_bytes()==raw
 resources[name]={'path':'assets/'+name,'bytes':len(raw),'sha256':digest,'reencoded':False};uses.append({'role':role,'sha256':digest})
 return prefix+name
f4=package['f4'];pattern=r'data:image/[a-zA-Z0-9.+-]+;base64,[A-Za-z0-9+/=]+'
f4small=re.sub(pattern,lambda m:externalize(m.group(0),'../assets/','F4 image'),f4)
(out/'f4/index.html').write_text(f4small)
small={'f4':'','images':{name:externalize(uri,'assets/',name) for name,uri in package['images'].items()}}
s=s[:match.start(1)]+json.dumps(small,ensure_ascii=False)+s[match.end(1):]
old='initBody();frame.srcdoc=PACKAGE.f4;';new="initBody();frame.src='f4/index.html';";assert s.count(old)==1;s=s.replace(old,new)
guard="if(location.protocol==='file:'){$('status').textContent='Esta copia necesita un servidor local. Ejecuta INICIAR_WINDOWS.bat o INICIAR_MAC_LINUX.command; también puedes usar Live Server de Visual Studio Code.';}else "
assert s.count('init().catch(e=>')==1;s=s.replace('init().catch(e=>',guard+'init().catch(e=>')
assert 'data:image/' not in s and 'data:image/' not in f4small
(out/'index.html').write_text(s)
report={'original_checkpoint':'CP13 v1.0','original_html_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'original_entry_bytes':source.stat().st_size,'externalized_entry_bytes':(out/'index.html').stat().st_size,'original_F4_html_bytes':len(f4.encode()),'externalized_F4_html_bytes':len(f4small.encode()),'unique_resources':list(resources.values()),'resource_uses':uses,'only_runtime_loading_change':{'before':old,'after':new},'file_open_guard':'Opening directly via file:// shows instructions instead of attempting cross-file iframe access','animation_code_changes':False,'original_modified':False}
(R/'EXTERNALIZACION.json').write_text(json.dumps(report,indent=2))
print(json.dumps({k:v for k,v in report.items() if k.endswith('_bytes')},indent=2));print('Resources preserved byte for byte:',len(resources))
