#!/usr/bin/env python3
"""Vídeo simultáneo CP01/CP02 del navegador, con idéntico scroll absoluto."""
from herramientas import HERE,ARGS,comparison_server
from playwright.sync_api import sync_playwright
from tempfile import TemporaryDirectory
from pathlib import Path
import base64,subprocess,json,os

OUT=HERE/'evidencias';OUT.mkdir(exist_ok=True)
with comparison_server() as url,TemporaryDirectory(prefix='cp02-frames-') as tmp,sync_playwright() as pw:
    tmp=Path(tmp)
    browser=pw.chromium.launch(executable_path=os.environ.get('F4_CHROMIUM','/usr/bin/chromium'),headless=True,args=ARGS)
    ctx=browser.new_context(viewport={'width':1280,'height':500},device_scale_factor=1)
    page=ctx.new_page();errors=[]
    page.on('pageerror',lambda e:errors.append(str(e)))
    page.goto(url,wait_until='networkidle');page.wait_for_function('window.bothReady()')
    client=ctx.new_cdp_session(page);frames=[]
    def receive(e):
        path=tmp/f'frame-{len(frames):05}.jpg';path.write_bytes(base64.b64decode(e['data']))
        frames.append({'file':path.name,'timestamp':e['metadata']['timestamp']})
        client.send('Page.screencastFrameAck',{'sessionId':e['sessionId']})
    client.on('Page.screencastFrame',receive)
    client.send('Page.startScreencast',{'format':'jpeg','quality':95,'maxWidth':1280,'maxHeight':500,'everyNthFrame':1})
    page.wait_for_timeout(700)
    route=page.evaluate('''async()=>{
      const states=[];let from=0;
      for(const to of [0,.25,.5,.62,.75,.82,.9,1,.9,.75,.5,.25,0]){
        const count=Math.max(1,Math.round(Math.abs(to-from)/.01));
        for(let i=1;i<=count;i++){
          window.both(from+(to-from)*i/count);
          await new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)));
        }
        await new Promise(r=>setTimeout(r,[.25,.5,.75,.9].includes(to)?700:300));
        states.push({requested:to,before:document.getElementById('antes').contentWindow.__F4.state.progress,after:document.getElementById('despues').contentWindow.__F4.state.progress});from=to;
      }
      return states;
    }''')
    page.wait_for_timeout(500);client.send('Page.stopScreencast');ctx.close();browser.close()
    assert len(frames)>40 and not errors
    assert all(abs(s['before']-s['requested'])<.001 and abs(s['after']-s['requested'])<.001 for s in route)
    lines=[]
    for i,f in enumerate(frames):
        lines.append(f"file '{f['file']}'")
        if i+1<len(frames):lines.append(f"duration {max(.001,frames[i+1]['timestamp']-f['timestamp']):.6f}")
    lines.append(f"file '{frames[-1]['file']}'");(tmp/'frames.txt').write_text('\n'.join(lines)+'\n')
    subprocess.run(['ffmpeg','-hide_banner','-loglevel','warning','-y','-f','concat','-safe','0','-i',str(tmp/'frames.txt'),
        '-vf','scale=in_range=pc:out_range=tv,format=yuv420p,fps=30','-c:v','libx264','-crf','20','-preset','veryfast','-color_range','tv','-pix_fmt','yuv420p','-movflags','+faststart',str(OUT/'F4_CP02_ANTES_DESPUES.mp4')],check=True)
    result={'method':'CDP captura real del navegador; scroll absoluto sincronizado, dos runtimes independientes','before':'CP01 commit 81a9dfbb757c5cc2b1011c0314587cb9b9d661ee','after':'CP02 v1.1','viewport':[1280,500],'panel_viewports':[640,400],'captured_frames':len(frames),'capture_duration_seconds':frames[-1]['timestamp']-frames[0]['timestamp'],'route':route,'page_errors':errors,'note':'MP4 a 30 fps mediante duplicación según timestamps; sin interpolación artificial. SwiftShader y captura limitan la cadencia; no es una medición de FPS físicos.'}
    (OUT/'registro-video-comparativo.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
    print(json.dumps(result,ensure_ascii=False))
