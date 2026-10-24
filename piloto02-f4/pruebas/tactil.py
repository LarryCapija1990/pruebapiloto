#!/usr/bin/env python3
from pathlib import Path
from playwright.sync_api import sync_playwright
import json,os

root=Path(__file__).resolve().parents[1]
out=Path(os.environ.get('F4_OUT',root/'evidencias'));out.mkdir(exist_ok=True,parents=True)
with sync_playwright() as pw:
 b=pw.chromium.launch(executable_path=os.environ.get('F4_CHROMIUM','/usr/bin/chromium'),headless=True,args=['--no-sandbox','--enable-unsafe-swiftshader','--use-gl=angle','--use-angle=swiftshader'])
 ctx=b.new_context(viewport={'width':390,'height':844},has_touch=True,is_mobile=True,device_scale_factor=2)
 page=ctx.new_page();page.goto(os.environ.get('F4_URL','http://127.0.0.1:4173'));page.wait_for_function('window.__F4?.state.ready')
 cdp=ctx.new_cdp_session(page)
 before=page.evaluate('window.__F4.state.progress')
 cdp.send('Input.dispatchTouchEvent',{'type':'touchStart','touchPoints':[{'x':195,'y':640}]})
 for y in range(620,219,-40):
  cdp.send('Input.dispatchTouchEvent',{'type':'touchMove','touchPoints':[{'x':195,'y':y}]});page.wait_for_timeout(30)
 cdp.send('Input.dispatchTouchEvent',{'type':'touchEnd','touchPoints':[]})
 page.wait_for_function('window.__F4.state.progress>.02');page.wait_for_timeout(500)
 after=page.evaluate('window.__F4.state.progress')
 checks=[{'name':'Gesto táctil CDP desplaza scroll y transformación','passed':after>before+.02,'before':before,'after':after}]
 # A real pointer input on the range, rather than setting its value in JavaScript.
 r=page.locator('#scrub').bounding_box();page.touchscreen.tap(r['x']+r['width']*.62,r['y']+r['height']/2)
 page.wait_for_function('Math.abs(window.__F4.state.progress-.62)<.04')
 actual=page.evaluate('window.__F4.state.progress')
 checks.append({'name':'Toque en control de recorrido alcanza posición','passed':abs(actual-.62)<.04,'actual':actual})
 page.screenshot(path=str(out/'movil-control-tactil.png'))
 b.close()
result={'checks':checks,'scope':'Input.dispatchTouchEvent y touchscreen.tap en Chromium emulado; no teléfono físico.'}
(out/'resultados-tactiles.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
print(json.dumps(result,ensure_ascii=False));raise SystemExit(0 if all(x['passed'] for x in checks) else 1)
