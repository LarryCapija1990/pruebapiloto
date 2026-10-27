"""Local same-origin viewer, Python standard library only."""
from pathlib import Path
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from functools import partial
import argparse,webbrowser,hashlib
p=argparse.ArgumentParser();p.add_argument('--sin-abrir',action='store_true');a=p.parse_args()
root=Path(__file__).resolve().parent
manifest=root/'CHECKSUMS.sha256'
if not manifest.exists():raise SystemExit('Falta CHECKSUMS.sha256. Extrae ambas partes ZIP en la misma carpeta.')
for line in manifest.read_text().splitlines():
 expected,name=line.split('  ',1);f=root/name
 if not f.is_file() or hashlib.sha256(f.read_bytes()).hexdigest()!=expected:raise SystemExit('Faltan recursos o una parte está incompleta. Extrae de nuevo ambos ZIP en la misma carpeta raíz.')
with ThreadingHTTPServer(('127.0.0.1',0),partial(SimpleHTTPRequestHandler,directory=str(root))) as s:
 url=f'http://127.0.0.1:{s.server_address[1]}/index.html';print('Vista local CP13: '+url,flush=True);print('Cierra con Ctrl+C. Conserva esta ventana abierta.',flush=True)
 if not a.sin_abrir:webbrowser.open(url)
 try:s.serve_forever()
 except KeyboardInterrupt:pass
