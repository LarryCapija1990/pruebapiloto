from pathlib import Path
from tempfile import TemporaryDirectory
from contextlib import contextmanager
import shutil,socket,subprocess,sys,time,urllib.request

ROOT=Path(__file__).resolve().parents[1]
HERE=Path(__file__).resolve().parent
ARGS=['--no-sandbox','--enable-unsafe-swiftshader','--use-gl=angle','--use-angle=swiftshader']

@contextmanager
def comparison_server():
    """CP01 exactly preserved code + identical image assets; CP02 current code."""
    with TemporaryDirectory(prefix='f4-cp02-comparacion-') as tmp:
        tmp=Path(tmp)
        for name in ['antes','despues']:shutil.copytree(ROOT/'prototipo',tmp/name)
        for name in ['app.js','scene.frag','index.html','style.css']:
            shutil.copy2(HERE/'base-cp01'/name,tmp/'antes'/name)
        (tmp/'index.html').write_text('''<!doctype html><html lang="es"><meta charset="utf-8"><title>CP01 / CP02 · Motivo central</title><style>*{box-sizing:border-box}body{margin:0;background:#0a0c12;color:#eee;font:13px Arial}header{height:42px;display:flex;justify-content:space-between;align-items:center;padding:0 18px}.panels{display:grid;grid-template-columns:1fr 1fr}.label{height:28px;text-align:center;letter-spacing:.12em;font-size:11px;padding:7px;background:#141824}iframe{display:block;width:100%;height:400px;border:0}footer{height:30px;text-align:center;padding:7px;color:#c6bcae}</style><header><span>PILOTO 02 · F4 · CORRECCIÓN DEL MOTIVO CENTRAL</span><output id="p">0 %</output></header><div class="panels"><div><div class="label">ANTES · CP01</div><iframe id="antes" src="antes/"></iframe></div><div><div class="label">DESPUÉS · CP02</div><iframe id="despues" src="despues/"></iframe></div></div><footer>Scroll sincronizado · curvas, grosor y luz del motivo · pendiente de revisión visual</footer><script>window.both=p=>{for(const id of ['antes','despues'])document.getElementById(id).contentWindow.__F4.go(p);document.getElementById('p').textContent=Math.round(p*100)+' %';};window.bothReady=()=>['antes','despues'].every(id=>document.getElementById(id).contentWindow.__F4?.state.ready);</script></html>''')
        with socket.socket() as s:s.bind(('127.0.0.1',0));port=s.getsockname()[1]
        proc=subprocess.Popen([sys.executable,'-m','http.server',str(port),'--bind','127.0.0.1','--directory',str(tmp)],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
        url=f'http://127.0.0.1:{port}'
        try:
            for _ in range(100):
                try:
                    with urllib.request.urlopen(url,timeout=1) as response:assert response.status==200
                    break
                except OSError:time.sleep(.1)
            else:raise RuntimeError('No inicia el servidor comparativo')
            yield url
        finally:proc.terminate();proc.wait(timeout=10)
