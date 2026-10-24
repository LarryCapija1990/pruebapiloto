from playwright.sync_api import sync_playwright
from pathlib import Path
import json
root=Path(__file__).resolve().parents[1]/'evidencias';root.mkdir(exist_ok=True)
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox','--enable-unsafe-swiftshader','--use-gl=angle','--use-angle=swiftshader'])
 page=b.new_page(viewport={'width':1440,'height':900},device_scale_factor=1)
 page.on('console',lambda m: print('console',m.type,m.text) if m.type in ['error','warning'] else None)
 page.on('pageerror',lambda e: print('ERROR',e))
 page.goto('http://127.0.0.1:4173'); page.wait_for_function('window.__F4?.state.ready')
 for v in [0,.25,.4,.5,.6,.7,.75,.9,.95,1]:
  page.evaluate('(v)=>window.__F4.go(v)',v);page.wait_for_timeout(180)
  page.screenshot(path=str(root/f'preliminar-{round(v*100):03}.png'))
 print(page.evaluate('window.__F4.state'))
 print('GPU ms',page.evaluate('window.__F4.benchmark()'))
 b.close()
