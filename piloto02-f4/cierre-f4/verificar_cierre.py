#!/usr/bin/env python3
"""Verifica congelación CP02 y equivalencia real del HTML portable sin red."""
from pathlib import Path
from tempfile import TemporaryDirectory
from zipfile import ZipFile
from playwright.sync_api import sync_playwright
import subprocess,socket,urllib.request,time,hashlib,json,os,sys,base64

ROOT=Path(__file__).resolve().parents[1];REPO=ROOT.parent;OUT=ROOT/'cierre-f4/evidencias';OUT.mkdir(exist_ok=True)
APPROVED='2c680f925e801ca45f2904deb49a9953c7dd6634'
ARTIFACT=REPO/'descargas/NV_SCOTT_PILOTO02_F4_CP03_v1.2_LOCAL.zip'
report={'approved_commit':APPROVED,'checks':[],'frozen_files':[],'console':[],'page_errors':[],'failed_requests':[],'portable_http_requests':[],'profiles':{},'environment_blocks':[],'portable_load_methods':{}}
def check(name,ok,details=None):
    report['checks'].append({'name':name,'passed':bool(ok),'details':details});print(('PASS ' if ok else 'FAIL ')+name,flush=True)
def go(page,v):
    page.evaluate('(v)=>window.__F4.go(v)',v);page.wait_for_function('(v)=>Math.abs(window.__F4.state.progress-v)<.001',arg=v)
    page.evaluate('()=>new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))')
def fingerprint(page):
    data=page.evaluate("document.querySelector('canvas').toDataURL().split(',')[1]")
    return hashlib.sha256(base64.b64decode(data)).hexdigest()
def watch(page,label):
    page.on('console',lambda m:report['console'].append({'label':label,'type':m.type,'text':m.text}) if m.type in ['error','warning'] else None)
    page.on('pageerror',lambda e:report['page_errors'].append({'label':label,'error':str(e)}))
    def failed(r):
        entry={'label':label,'url':r.url,'failure':r.failure}
        if r.url.startswith('file:') and r.failure=='net::ERR_BLOCKED_BY_ADMINISTRATOR':report['environment_blocks'].append(entry)
        else:report['failed_requests'].append(entry)
    page.on('requestfailed',failed)

with TemporaryDirectory(prefix='f4-cierre-') as work:
    work=Path(work)
    approved=work/'aprobada';current=work/'actual'
    lock=json.loads((ROOT/'cierre-f4/CONGELACION_CP02.json').read_text())
    assert lock['approved_commit']==APPROVED
    for name,expected_hash in lock['files'].items():
        rel=Path(name)
        data=(ROOT/'cierre-f4/base-cp02/index.html').read_bytes() if name=='index.html' else (ROOT/'prototipo'/rel).read_bytes()
        assert hashlib.sha256(data).hexdigest()==expected_hash,name
        dest=approved/rel;dest.parent.mkdir(exist_ok=True,parents=True);dest.write_bytes(data)
        now=(ROOT/'prototipo'/rel).read_bytes();target=current/rel;target.parent.mkdir(exist_ok=True,parents=True);target.write_bytes(now)
        same=hashlib.sha256(now).hexdigest()==hashlib.sha256(data).hexdigest()
        report['frozen_files'].append({'path':str(rel),'sha256_approved':hashlib.sha256(data).hexdigest(),'sha256_current':hashlib.sha256(now).hexdigest(),'identical':same})
        if rel.as_posix()!='index.html':check('Congelado: '+str(rel),same)
    check('Único cambio de presentación en runtime: texto de aprobación',all(x['identical'] for x in report['frozen_files'] if x['path']!='index.html'))
    with ZipFile(ARTIFACT) as z:
        check('ZIP local: CRC válido',z.testzip() is None)
        for name in z.namelist():assert (work/'portable'/name).resolve().is_relative_to(work/'portable')
        z.extractall(work/'portable')
    portable=list((work/'portable').rglob('ABRIR_PILOTO_F4.html'));assert len(portable)==1
    with socket.socket() as s:s.bind(('127.0.0.1',0));port=s.getsockname()[1]
    proc=subprocess.Popen([sys.executable,'-m','http.server',str(port),'--bind','127.0.0.1','--directory',str(work)],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    url=f'http://127.0.0.1:{port}'
    try:
        for _ in range(100):
            try:
                with urllib.request.urlopen(url,timeout=1):break
            except OSError:time.sleep(.1)
        else:raise RuntimeError('No inicia el servidor de comparación')
        with sync_playwright() as pw:
            b=pw.chromium.launch(executable_path=os.environ.get('F4_CHROMIUM','/usr/bin/chromium'),headless=True,args=['--no-sandbox','--enable-unsafe-swiftshader','--use-gl=angle','--use-angle=swiftshader'])
            for profile,w,h,dpr in [('escritorio',1440,900,1),('movil',390,844,2)]:
                online=b.new_context(viewport={'width':w,'height':h},device_scale_factor=dpr,has_touch=profile=='movil',is_mobile=profile=='movil')
                offline=b.new_context(viewport={'width':w,'height':h},device_scale_factor=dpr,has_touch=profile=='movil',is_mobile=profile=='movil',offline=True)
                pages={}
                for label,path in [('cp02',url+'/aprobada/'),('http',url+'/actual/'),('portable',portable[0].as_uri())]:
                    page=(offline if label=='portable' else online).new_page();watch(page,profile+'/'+label)
                    if label=='portable':page.on('request',lambda req:report['portable_http_requests'].append(req.url) if req.url.startswith(('http://','https://')) else None)
                    if label=='portable':
                        try:
                            page.goto(path,wait_until='load');report['portable_load_methods'][profile]='native file:// navigation, offline'
                        except Exception as error:
                            if 'ERR_BLOCKED_BY_ADMINISTRATOR' not in str(error):raise
                            page.close();page=offline.new_page();watch(page,profile+'/'+label)
                            page.on('request',lambda req:report['portable_http_requests'].append(req.url) if req.url.startswith(('http://','https://')) else None)
                            page.set_content(portable[0].read_text(),wait_until='load')
                            report['portable_load_methods'][profile]='Extracted HTML loaded through page.set_content in an offline context; native file:// blocked by administrator. Not a native file navigation test.'
                    else:page.goto(path,wait_until='load')
                    page.wait_for_function('window.__F4?.state.ready');pages[label]=page
                    check(profile+'/'+label+': carga 8 imágenes',page.evaluate('window.__F4.metrics.assets===8'))
                profile_data={'viewport':[w,h],'device_scale_factor':dpr,'pixel_hashes':[]}
                for v in [0,.25,.4,.5,.6,.7,.75,.82,.86,.9,.95,1]:
                    hashes={}
                    for label,page in pages.items():go(page,v);hashes[label]=fingerprint(page)
                    check(f'{profile} {v*100:g}%: CP02 = HTTP = portable',len(set(hashes.values()))==1,hashes)
                    profile_data['pixel_hashes'].append({'progress':v,'hashes':hashes})
                    if v in [0,.25,.5,.75,.9,1]:pages['portable'].screenshot(path=str(OUT/f'portable-{profile}-p{round(v*100):03}.png'))
                p=pages['portable'];values=[]
                for v in [0,.6,.3,.6,1]:go(p,v);values.append(fingerprint(p))
                check(profile+': portable 0→60→30→60→100 reversible',values[1]==values[3])
                go(p,.537);image=fingerprint(p);count=p.evaluate('window.__F4.metrics.renders');p.wait_for_timeout(600)
                check(profile+': portable pausa sin cambio ni renders',image==fingerprint(p) and count==p.evaluate('window.__F4.metrics.renders'))
                for page in pages.values():page.locator('#motion').click();page.wait_for_timeout(100)
                for v in [0,.5,1]:
                    hashes=[]
                    for page in pages.values():go(page,v);hashes.append(fingerprint(page))
                    check(f'{profile} reducido {v*100:g}%: CP02 = HTTP = portable',len(set(hashes))==1)
                p.screenshot(path=str(OUT/f'portable-{profile}-reducido.png'))
                check(profile+': portable muestra aprobación',p.locator('.review').inner_text()=='Aprobada creativamente · Piloto 02')
                report['profiles'][profile]=profile_data;online.close();offline.close()
            b.close()
    finally:proc.terminate();proc.wait(timeout=10)
check('Portable sin conexión: ninguna petición HTTP/HTTPS',not report['portable_http_requests'],report['portable_http_requests'])
check('Sin errores de consola, JavaScript ni cargas fallidas',not report['console'] and not report['page_errors'] and not report['failed_requests'],{'console':report['console'],'js':report['page_errors'],'failed':report['failed_requests']})
report['summary']={'passed':sum(x['passed'] for x in report['checks']),'failed':sum(not x['passed'] for x in report['checks']),'creative_approval':'Usuario: aprobada creativamente para este piloto','physical_mobile_tested':False,'native_file_navigation':'See environment_blocks; offline content is verified separately.'}
(OUT/'verificacion-cierre.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n')
print(json.dumps(report['summary'],ensure_ascii=False));raise SystemExit(1 if report['summary']['failed'] else 0)
