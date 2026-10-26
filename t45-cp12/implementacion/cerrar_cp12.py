from pathlib import Path
from PIL import Image,ImageDraw
import hashlib,json,zipfile
R=Path(__file__).resolve().parents[1];E=R/'evidencias';j=json.loads((E/'RESULTADOS_CP12.json').read_text());assert j['failed']==0
k=json.loads((E/'TOPOLOGIA_CP12.json').read_text());assert k['failed']==0
f4=R.parent/'piloto02-f4';n=0
if f4.exists():
 for line in (f4/'MANIFIESTO_F4.sha256').read_text().splitlines():
  expected,rel=line.split('  ',1);assert hashlib.sha256((f4/rel).read_bytes()).hexdigest()==expected,rel;n+=1
(E/'F4_INTACTO.json').write_text(json.dumps({'verified_existing_F4_manifest_files':n,'embedded_F4_sha256':json.loads((R/'INTEGRIDAD_BASE.json').read_text())['f4_embedded_sha256'],'changes_to_F4':False},indent=2))
# A standalone gallery is evidence, never an asset of the running prototype.
head='<!doctype html><html lang="es"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>CP12 · Revisión</title><style>body{background:#101116;color:#eee8dc;font:16px Arial;margin:24px}a{color:#efc28a}img{max-width:100%;height:auto}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:15px}figure{margin:0}figcaption{padding:8px}h2{margin-top:40px}</style><h1>CP12 · prueba de ritmo rápido</h1><p>32–39 %: encendido, cambio del cuerpo y apagado. Retirada desde 35 %. Capturas reales, sin uso de fotogramas en el motor.</p><p><a href="ABRIR_T34_T45_CP12.html">Abrir prototipo</a></p>'
parts=[head]
for label in ['escritorio','movil','grande','horizontal']:
 for direction in ['COMPARACION','IDA','VUELTA']:
  files=sorted(E.glob(label+'_'+direction+'_*.jpg'),reverse=direction=='VUELTA')
  if not files:continue
  parts.append(f'<h2>{label} · {direction}</h2><div class="grid">')
  for f in files:
   q=int(f.stem.rsplit('_',1)[1])/10;parts.append(f'<figure><a href="evidencias/{f.name}"><img loading="lazy" src="evidencias/{f.name}" alt="{label} {direction} {q}%"></a><figcaption>{q:g} % · {direction}</figcaption></figure>')
  parts.append('</div>')
(R/'REVISION_CP12.html').write_text('\n'.join(parts))
qs=[.32,.335,.35,.365,.375,.39];out=Image.new('RGB',(960,326*3),'#101116');d=ImageDraw.Draw(out)
for i,q in enumerate(qs):
 p=E/f'escritorio_IDA_{round(q*1000):04}.jpg';im=Image.open(p);im.thumbnail((480,300));x=i%2*480;y=i//2*326;out.paste(im,(x,y));d.text((x+10,y+303),f'CP12 / {q*100:g} % / para revision',fill='#efc28a')
out.save(E/'RESUMEN_CP12.jpg',quality=86)
rows=[]
for label,p in j['profiles'].items():
 t=p['rapid_segment_ms'];e=p['texture_entry'];rows.append(f"|{label}|{t['median']:.2f}|{t['p95']:.2f}|{t['max']:.2f}|{e['q']*100:.1f} %|")
report=f'''# CP12 v1.0 · Informe de la revisión rápida

26 de octubre de 2026. Se conserva M2 y se revisa su ritmo, sin atribuir aprobación al usuario.

## Cambio concreto

El cambio de símbolo a tinta se comprime a **32–39 %: 7 puntos porcentuales locales**. Encendido 32–33,5 %, deformación de cuerpo 32,5–36,5 % y apagado 35–39 %, solapados. La retirada empieza al 35 %, durante el apagado. El símbolo original se mantiene antes del cambio; después no hay capa de eje ni contorno hueco construido por separado.

Se reemplazó la correspondencia poligonal de CP11 por dos campos de distancia, del cuerpo luminoso y de una máscara extraída del JPG del as. El campo de partida se suaviza para impedir aristas de cálculo durante la mezcla; el borde de llegada procede de la máscara raster auténtica con suavizado menor de un píxel fuente. Conserva asimetrías y ondulaciones, sin imponer una pica simétrica. El detalle ornamental sigue siendo el JPG intacto.

El muestreo fotográfico comienza solo al bajar a 2,8 píxeles CSS por píxel fuente y se completa a 2,0. Este umbral depende del viewport: no se impone un macro pixelado durante un tramo fijo. La foto final, mano, cartas, marco y letras se conservan como un plano original único.

## Pruebas ejecutadas

**{j['passed']} comprobaciones de navegador correctas y {k['passed']} estados de topología sólidos: {j['passed']+k['passed']} controles, 0 fallos.** Viewports: 1440×900, 1920×1080, 390×844 DPR2 (emulado) y 844×390.

- 24 comparaciones T34 con CP11: exactamente los mismos píxeles en p=0,.2,.4,.6,.8,1. q0 de T45 coincide con el framebuffer F4 final en los cuatro perfiles. La fuente F4 embebida conserva su SHA256 original; {n} archivos del histórico F4 verificados sin cambios.
- Inversión en q=.333,.351,.378 en todos los perfiles: mismos PNG al llegar, retroceder y evaluar directamente. Tres contextos nuevos arrancan directamente dentro del tramo y repiten el mismo estado al invertir.
- Parada de cinco segundos en .351: imagen y contador de renders inmóviles. Todo se calcula desde q, sin reloj de animación.
- Análisis de 41 estados del campo entre 35–39 % (paso de 0,1 punto porcentual): un componente y ningún hueco. Es evaluación del campo codificado; se separa de los sondeos reales de GPU.
- Centro de pica opaco al acabar el cambio, alfa cero en las posiciones superior e inferior del eje anterior; sin error WebGL en esas comprobaciones.
- Comparación de esquina de fondo entre .320 y .334: sin iluminación global durante el encendido. El halo es local; el soporte cambia después de manera persistente, no como flash de pantalla.
- Resize en .351 y .8 mantiene q; controles de teclado, visibilidad de controles y movimiento reducido manual comprobados.
- Carga offline sin peticiones HTTP/HTTPS, sin errores JS ni consola en los recorridos normales.

La inspección visual se hizo en las capturas del tramo, incluido 35 % tras suavizar una arista detectada en una primera construcción. No se afirma una aprobación creativa ni un estudio de percepción. Las comparaciones antes/después al mismo q y las secuencias se consultan en `REVISION_CP12.html`.

## Rendimiento medido y límites

Chromium headless/Linux/SwiftShader, no GPU ni teléfono físicos. 60 muestras por perfil dentro del tramo rápido, con lectura de un píxel para forzar el dibujado. No equivalen a FPS de pantalla.

|Perfil|Mediana ms|p95 ms|Máximo ms|Primera entrada de textura original|
|---|---:|---:|---:|---:|
'''+'\n'.join(rows)+'''

El nuevo cuerpo necesita un segundo contexto WebGL de 1066×600 y reutiliza su canvas; F4 no se altera. El navegador por software puede sufrir picos. No se certifica fluidez de equipo físico ni calidad cinematográfica definitiva. La fuente de 600 px sigue limitando el ornamento, aunque se retrasa su presentación ampliada.

La materialización del soporte y el descubrimiento del contexto conservan el mecanismo del piloto; su frente de máscara todavía puede percibirse y sigue sujeto a revisión. La aproximación inicial conserva el relevo de capas 12–18 % de CP11. Este encargo se centró en el cambio de cuerpo y su ritmo, sin rediseñar el resto de la escena.

La política de este entorno bloqueó file:// en CP11; CP12 se probó como documento offline sin red, no como apertura nativa de archivo. Se incluye alternativa HTTP local. Móvil emulado; no se ha ensayado lector de pantalla físico ni memoria/temperatura de GPU. El fallback y la arquitectura accesible existentes se conservan, sin repetir aquí todas las pruebas históricas de fallo de WebGL.

## Reproducibilidad y entrega

`python implementacion/construir.py` reconstruye el HTML usando campos ya incluidos, con biblioteca estándar. `preparar_cuerpo.py` reproduce campos/máscara y requiere Pillow, NumPy y SciPy. `probar_cp12.py` requiere Playwright, Pillow y Chromium; genera resultados y capturas en `evidencias/`.

Se conserva `REFERENCIA_CP11.html` para comparación y el paquete CP10 con su F4 original. Los ZIP son independientes y menores de 32 MiB; el paquete de fuentes es acumulativo de esta revisión y su referencia, no del histórico F4 de 210 MB, que permanece en su tag original del repositorio. No se ha modificado Nero’s Vice.
'''
(R/'INFORME_CP12.md').write_text(report)
(R/'VERSION.json').write_text(json.dumps({'checkpoint':'CP12','version':'1.0','morph_interval':[.32,.39],'interval_percentage_points':7,'withdrawal_start':.35,'F4_unchanged':True,'creative_approval':False,'html_sha256':j['html_sha256']},indent=2))
print('Report and gallery generated')
