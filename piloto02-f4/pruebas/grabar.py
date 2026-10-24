#!/usr/bin/env python3
"""Grabación real del navegador vía CDP. No sintetiza frames de la transición."""
from pathlib import Path
from playwright.sync_api import sync_playwright
from tempfile import TemporaryDirectory
import base64,json,subprocess,os

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'evidencias';OUT.mkdir(exist_ok=True)
with TemporaryDirectory(prefix='f4-video-') as tmp,sync_playwright() as pw:
    tmp=Path(tmp)
    b=pw.chromium.launch(executable_path=os.environ.get('F4_CHROMIUM','/usr/bin/chromium'),headless=True,
        args=['--no-sandbox','--enable-unsafe-swiftshader','--use-gl=angle','--use-angle=swiftshader'])
    ctx=b.new_context(viewport={'width':1280,'height':800},device_scale_factor=1)
    page=ctx.new_page();page.goto(os.environ.get('F4_URL','http://127.0.0.1:4173'),wait_until='networkidle')
    page.wait_for_function('window.__F4?.state.ready')
    client=ctx.new_cdp_session(page);frames=[]
    def frame(event):
        n=len(frames);path=tmp/f'frame-{n:05}.jpg';path.write_bytes(base64.b64decode(event['data']))
        frames.append({'file':path.name,'timestamp':event['metadata']['timestamp']})
        client.send('Page.screencastFrameAck',{'sessionId':event['sessionId']})
    client.on('Page.screencastFrame',frame)
    client.send('Page.startScreencast',{'format':'jpeg','quality':92,'maxWidth':1280,'maxHeight':800,'everyNthFrame':1})
    page.wait_for_timeout(1100)
    # Only the scroll position is changed; the application renders its own states.
    observed=page.evaluate('''async()=>{
      const states=[],pauses=[0,.25,.4,.5,.6,.7,.75,.9,.95,1,.95,.9,.75,.7,.6,.5,.4,.25,0];
      let from=0;
      for(const to of pauses){
        const count=Math.max(1,Math.round(Math.abs(to-from)/.005));
        for(let i=1;i<=count;i++){
          window.__F4.go(from+(to-from)*i/count);
          await new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)));
        }
        await new Promise(r=>setTimeout(r,to===0||to===1?900:180));
        states.push({requested:to,actual:window.__F4.state.progress,timestamp:performance.now()});from=to;
      }
      return states;
    }''')
    page.wait_for_timeout(900);client.send('Page.stopScreencast');ctx.close();b.close()
    if len(frames)<40:raise RuntimeError(f'Grabación insuficiente: {len(frames)} frames')
    concat=[]
    for i,f in enumerate(frames):
        concat.append(f"file '{f['file']}'")
        if i+1<len(frames):concat.append(f"duration {max(.001,frames[i+1]['timestamp']-f['timestamp']):.6f}")
    concat.append(f"file '{frames[-1]['file']}'")
    (tmp/'frames.txt').write_text('\n'.join(concat)+'\n')
    subprocess.run(['ffmpeg','-hide_banner','-loglevel','warning','-y','-f','concat','-safe','0','-i',str(tmp/'frames.txt'),
        '-vf','fps=30,format=yuv420p','-c:v','libx264','-crf','19','-preset','medium','-movflags','+faststart',str(OUT/'F4_CP01_ida_y_vuelta.mp4')],check=True)
    record={'method':'CDP Page.startScreencast, JPEG 92; MP4 H.264 a 30 fps conservando timestamps de captura. Duplicación de frames para cadencia, sin interpolación artificial.',
        'viewport':[1280,800],'browser_frames':len(frames),'duration_seconds':frames[-1]['timestamp']-frames[0]['timestamp'],
        'observed_route':observed,'software_renderer':'Chromium SwiftShader','note':'Captura del navegador de prueba; no demuestra 30 FPS de render ni rendimiento en un dispositivo físico.'}
    (OUT/'registro-grabacion.json').write_text(json.dumps(record,indent=2,ensure_ascii=False)+'\n')
    print(json.dumps(record,ensure_ascii=False))
