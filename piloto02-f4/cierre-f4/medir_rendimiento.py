#!/usr/bin/env python3
"""Mide entrada→dibujo GPU completado sin captura de pantalla ni animación nueva."""
from pathlib import Path
from tempfile import TemporaryDirectory
from zipfile import ZipFile
from playwright.sync_api import sync_playwright
import json,os,statistics,math,time

ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'cierre-f4/evidencias'
ZIP=ROOT.parent/'descargas/NV_SCOTT_PILOTO02_F4_CP03_v1.2_LOCAL.zip'
def describe(values):
    vals=sorted(values)
    return {'count':len(vals),'median_ms':statistics.median(vals),'p95_ms':vals[math.ceil(len(vals)*.95)-1],'max_ms':max(vals),'over_100ms':sum(x>100 for x in vals),'over_250ms':sum(x>250 for x in vals)}
result={'method':'Secuencia de 200 cambios absolutos de scroll 0→100→0; espera al estado y gl.finish. Sin capturas ni vídeo durante el muestreo. Percentil por rango más cercano.','renderer_scope':'Chromium headless, SwiftShader forzado; no hardware de móvil físico ni certificación 30/60 FPS.','portable_load':'HTML extraído, page.set_content en contexto offline; file:// bloqueado por la política del entorno, ver verificacion-cierre.json.','profiles':{},'checks':[]}
with TemporaryDirectory(prefix='f4-perf-') as tmp,ZipFile(ZIP) as z,sync_playwright() as pw:
    z.extractall(tmp);html=next(Path(tmp).rglob('ABRIR_PILOTO_F4.html')).read_text()
    b=pw.chromium.launch(executable_path=os.environ.get('F4_CHROMIUM','/usr/bin/chromium'),headless=True,args=['--no-sandbox','--enable-unsafe-swiftshader','--use-gl=angle','--use-angle=swiftshader'])
    result['browser']=b.version
    for label,w,h,dpr in [('escritorio',1440,900,1),('movil_emulado',390,844,2)]:
        ctx=b.new_context(viewport={'width':w,'height':h},device_scale_factor=dpr,offline=True,has_touch=label!='escritorio',is_mobile=label!='escritorio');page=ctx.new_page()
        start=time.perf_counter();page.set_content(html,wait_until='load');page.wait_for_function('window.__F4?.state.ready');load_ms=(time.perf_counter()-start)*1000
        data=page.evaluate('''async()=>{
          const canvas=document.querySelector('canvas'),gl=canvas.getContext('webgl');
          const ext=gl.getExtension('WEBGL_debug_renderer_info');
          const renderer=ext?gl.getParameter(ext.UNMASKED_RENDERER_WEBGL):gl.getParameter(gl.RENDERER);
          const heapBefore=performance.memory?.usedJSHeapSize??null;
          const samples=[],states=[];
          const positions=[...Array.from({length:100},(_,i)=>(i+1)/100),...Array.from({length:100},(_,i)=>(99-i)/100)];
          for(const value of positions){
            const begin=performance.now();window.__F4.go(value);
            await new Promise((resolve,reject)=>{
              const deadline=performance.now()+5000;
              const poll=()=>{
                if(Math.abs(window.__F4.state.progress-value)<.001)return resolve();
                if(performance.now()>deadline)return reject(new Error('Timeout de progreso '+value));
                requestAnimationFrame(poll);
              };requestAnimationFrame(poll);
            });
            gl.finish();samples.push(performance.now()-begin);states.push(window.__F4.state.progress);
          }
          return {samples,positions,states,renderer,gl_error:gl.getError(),context_losses:window.__F4.metrics.contextLosses,renders:window.__F4.metrics.renders,buffer:window.__F4.state.buffer,heapBefore,heapAfter:performance.memory?.usedJSHeapSize??null};
        }''')
        data.update(viewport=[w,h],device_scale_factor=dpr,ready_ms_in_memory=load_ms,response=describe(data['samples']))
        result['profiles'][label]=data
        ok=data['gl_error']==0 and data['context_losses']==0 and len(data['samples'])==200 and all(abs(a-e)<.001 for a,e in zip(data['states'],data['positions']))
        result['checks'].append({'name':label+': 200 cambios completados, sin error GL ni pérdida de contexto','passed':ok})
        print(label,json.dumps(data['response']),flush=True);ctx.close()
    b.close()
result['summary']={'passed':sum(c['passed'] for c in result['checks']),'failed':sum(not c['passed'] for c in result['checks']),'real_device_fps':'No medido','gpu_memory':'No perfilada; heap JS disponible por separado, no equivale a memoria total.'}
(OUT/'rendimiento.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
print(json.dumps(result['summary'],ensure_ascii=False));raise SystemExit(1 if result['summary']['failed'] else 0)
