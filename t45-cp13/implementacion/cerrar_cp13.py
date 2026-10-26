from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[1];E=R/'evidencias';b=json.loads((E/'NAVEGADOR.json').read_text());m=json.loads((E/'MODELO.json').read_text());assert b['failed']==m['failed']==0
assert b['html_sha256']==hashlib.sha256((R/'ABRIR_T34_T45_CP13.html').read_bytes()).hexdigest()
# Keep the complete final run through its summary, excluding trailing bytes from a cancelled development run.
log=E/'NAVEGADOR.log';data=log.read_bytes();marker=f"TOTAL {b['passed']} PASS {b['failed']} FAIL".encode();at=data.find(marker)
if at>=0:log.write_bytes(data[:at+len(marker)]+b'\n')
base=R.parent/'t45-cp12';frozen=[]
if base.exists():
 for path in ['implementacion/cuerpo.js','assets/campos-cuerpo.png','assets/pica-mascara-original.png']:
  a=(R/path).read_bytes();old=(base/path).read_bytes();assert a==old;frozen.append({'path':path,'sha256':hashlib.sha256(a).hexdigest()})
 old=(base/'implementacion/t45.js').read_text().split('function lengths()')[0];new=(R/'implementacion/t45.js').read_text().split('function lengths()')[0];assert old==new;frozen.append({'path':'t45.js rendering prefix through finish()','sha256':hashlib.sha256(new.encode()).hexdigest()})
(E/'RENDER_CONGELADO.json').write_text(json.dumps({'accepted_visual_baseline':'CP12 v1.0','frozen':frozen,'F4_embedded_byte_identical':json.loads((R/'INTEGRIDAD_BASE.json').read_text())['exact_original']},indent=2))
# Distance chart, evidence only. Never read by prototype.
parts=[55,440,55,20,99,286,165];short=[55,220,55,20,99,143,165];colors=['#777f8e','#e6ad61','#777f8e','#eee5d0','#777f8e','#e6ad61','#777f8e'];scale=900/1120
svg=['<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="300" viewBox="0 0 1100 300"><rect width="1100" height="300" fill="#101116"/><g font-family="Arial" fill="#eee8dc"><text x="30" y="34" font-size="22">CP13 · Misma imagen, menos scroll</text><text x="30" y="60" font-size="14">Abstracto a la mitad; acercamientos, revelaciones y parada sin distancia añadida.</text>']
for label,y,data,total in [('CP12',100,parts,1120),('CP13',165,short,757)]:
 svg.append(f'<text x="30" y="{y+21}" font-size="16">{label}</text>');x=105
 for v,c in zip(data,colors):svg.append(f'<rect x="{x}" y="{y}" width="{v*scale}" height="30" fill="{c}" stroke="#101116"/>');x+=v*scale
 svg.append(f'<text x="{x+12}" y="{y+21}" font-size="15">{total}vh</text>')
svg+=['<text x="105" y="235" font-size="14" fill="#e6ad61">Naranja: transformación abstracta</text><text x="430" y="235" font-size="14" fill="#a4adbd">Gris: entrada/revelación</text><text x="700" y="235" font-size="14">Claro: parada Innervision</text><text x="105" y="272" font-size="18">−363vh · −32,4 % del recorrido total · sin nuevas pausas</text></g></svg>'];(E/'DISTRIBUCION_CP13.svg').write_text(''.join(svg))
files=sorted(E.glob('*.jpg'));gallery=['<!doctype html><html lang="es"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>CP13 · Evidencias</title><style>body{background:#101116;color:#eee8dc;font:16px Arial;padding:24px}a{color:#efc28a}img{max-width:100%;height:auto}figure{margin:24px 0}</style><h1>CP13 · Ajuste de ritmo</h1><p><a href="ABRIR_T34_T45_CP13.html">Abrir versión nueva</a> · <a href="REFERENCIA_CP12.html">Abrir CP12 anterior</a></p><img src="evidencias/DISTRIBUCION_CP13.svg" alt="Las bandas abstractas ocupan la mitad y el total pasa de 1120 a 757vh">']
for f in files:gallery.append(f'<figure><img loading="lazy" src="evidencias/{f.name}" alt="{f.stem}"><figcaption>{f.stem}</figcaption></figure>')
(R/'REVISION_CP13.html').write_text('\n'.join(gallery))
total=b['passed']+m['passed']
text=f'''# CP13 v1.0 · Informe de ajuste de ritmo

26 de octubre de 2026. El usuario acepta la apariencia CP12 de Thunder → Innervision → Salute. Se conserva como referencia visual. CP13 se entrega como **primera prueba de distribución de scroll**.

## Resultado

**{total} comprobaciones correctas, 0 fallos**: {m['passed']} del modelo de distancia y {b['passed']} de navegador. HTML comprobado: SHA256 `{b['html_sha256']}`.

|Banda|Distancia anterior|Distancia CP13|
|---|---:|---:|
|T34 abstracta, p .10–.90|440vh|220vh|
|T45 abstracta, q .18–.70|286vh|143vh|
|Parada explícita en Innervision|20vh|20vh|
|Recorrido total efectivo|1120vh|757vh|

Se eliminan 363vh (32,4 %). No se trasladan a esperas, aproximaciones ni revelaciones. La entrada documental de T34 sigue siendo 55vh y su llegada a Innervision 55vh; T45 mantiene 99vh de acercamiento y 165vh de revelación final. El contenedor mide 857svh, incluida la pantalla que permanece visible.

El mapa nuevo convierte distancia física a los mismos p/q del render CP12. Las rampas de entrada/salida ocupan el 10 % de cada banda abstracta; la velocidad vuelve a la original en ambos extremos y llega a 2,25× en el centro. Su densidad de distancia es positiva, con integral exacta del 50 %. No hay discontinuidad ni velocidad infinita al invertir el mapa.

## Imagen congelada

El código de geometría, cámara, material, composición y dibujo de T45 hasta `finish()` es byte a byte el de CP12. El shader del cuerpo y los campos/máscaras también. F4 se incorpora desde el mismo ZIP original, sin cambiar su código. La duración exterior de T34 sí se modifica, de acuerdo con el nuevo encargo; no se confunde esa redistribución con un cambio de imagen.

La comparación de navegador fija las mismas posiciones visuales en ambos motores: p=0,.10,.35,.65,.90,1 para T34 y q=.18,.32,.35,.39,.64,.80,1 para T45. **Todas las comparaciones de canvas coinciden exactamente** en 1440×900, 1920×1080, 390×844 DPR2 y 844×390. Son 52 coincidencias de imágenes. Los JPEG son evidencia cómoda de revisar; la igualdad se comprueba sobre PNG sin pérdida.

Por separado, las pruebas de navegación usan scroll real, con tolerancia .001 por el redondeo de scroll a píxeles enteros. No se afirma que el mismo píxel de scroll represente el mismo fotograma que antes: precisamente cambia esa relación. Los porcentajes de los controles siguen siendo referencias visuales de CP12.

## Comprobaciones funcionales

- Modelo: dos bandas exactamente a la mitad, distancias exteriores intactas, monotonía en 10.001 puntos por transición, inversa con error menor de 1e-10, velocidad acotada y derivadas de entrada/salida coincidentes.
- Altura real del documento y distancias calculadas: 7,57 pantallas efectivas en los cuatro perfiles, dentro del redondeo de píxel. Se corrigió durante la prueba un desbordamiento de un píxel del texto accesible oculto, anclándolo al origen; no cambia su contenido ni su apariencia.
- Inversión del scroll en T34 .35/.86 y T45 .351/.66: se recuperan los mismos PNG, sin historial de dirección.
- Parada sin deriva dentro de la transformación, sin nuevos renders durante dos segundos de espera. No se añaden temporizadores de animación.
- Parada de Innervision en el centro de los 20vh: T34 final, T45 todavía en cero y sin arranque automático.
- Resize en ambas transiciones conserva el progreso; teclado y movimiento reducido manual comprobados en cada viewport.
- Offline: cero peticiones HTTP/HTTPS; sin errores JavaScript ni consola en la ejecución normal.

El único ajuste CSS adicional es la posición de elementos accesibles ocultos para evitar que incrementen la altura real. En la composición visible solo cambian el identificador de checkpoint y el estado editorial «imagen aceptada · ajuste de ritmo para revisión».

## Límites de la verificación

Chromium headless en Linux con SwiftShader. Móvil emulado; no se certifican FPS, latencia, memoria GPU ni fluidez física. No se repiten los benchmarks de composición de CP12 porque el render permanece idéntico; los límites de ese entorno siguen siendo aplicables. Esta prueba verifica la redistribución y la identidad de imagen, no una nueva producción visual.

La apertura nativa file:// quedó bloqueada por la política en versiones anteriores; se carga el HTML como documento offline para las pruebas, no se afirma haber verificado doble clic bajo esa política. Se incluyen instrucciones para archivo local ordinario y alternativa HTTP local.

## Reproducir

`python implementacion/construir.py` reconstruye el HTML usando recursos incluidos. `node implementacion/probar_modelo.cjs` prueba el modelo. `python implementacion/probar_cp13.py` ejecuta comparación, navegación y capturas; necesita Playwright, Pillow y Chromium `/usr/bin/chromium`.

`evidencias/MODELO.json`, `NAVEGADOR.json`, `NAVEGADOR.log` y `RENDER_CONGELADO.json` registran resultados. `REVISION_CP13.html` muestra la distribución y las comparaciones. `REFERENCIA_CP12.html` conserva la versión visual aceptada anterior. No se modifica Nero’s Vice ni se añaden otros álbumes.
'''
(R/'INFORME_CP13.md').write_text(text)
(R/'VERSION.json').write_text(json.dumps({'checkpoint':'CP13','version':'1.0','type':'scroll rhythm adjustment only','visual_baseline':'CP12 v1.0 accepted by user','visual_render_unchanged':True,'rhythm_pending_review':True,'abstract_ranges':{'T34':[.10,.90],'T45':[.18,.70]},'abstract_distance_factor':.5,'effective_vh_before':1120,'effective_vh_after':757,'hold_vh':20,'checks_passed':total,'checks_failed':0,'html_sha256':b['html_sha256']},indent=2))
print(total,'checks passed; report and gallery written')
