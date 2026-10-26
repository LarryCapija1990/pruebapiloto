from pathlib import Path
from PIL import Image,ImageDraw
R=Path(__file__).resolve().parents[1]
Q=[0,12,28,36,40,42,44,48,52,56,60,64,70,80,94,100]
css='body{background:#101116;color:#eee8dc;font:16px/1.5 Arial;margin:24px}a{color:#f1bc7e}img{max-width:100%;height:auto}figure{margin:0}section{margin:40px 0}h2{font-weight:400}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:16px}figcaption{padding:8px;font-size:13px}'
out=['<!doctype html><html lang="es"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>CP11 · evidencia secuencial</title><style>'+css+'</style><h1>CP11 · Ida y vuelta</h1><p>Capturas reales del prototipo, no fotogramas usados para renderizarlo. Ordena la revisión por q: 0 → 100 y 100 → 0. El HTML interactivo permite todos los estados intermedios.</p><p><a href="ABRIR_T34_T45_CP11.html">Abrir prototipo</a> · <a href="CAMBIOS_Y_LIMITES.md">Límites conocidos</a></p>']
for label in ['escritorio','grande','movil','horizontal']:
 for direction in ['IDA','VUELTA']:
  out.append(f'<section><h2>{label} · {direction}</h2><div class="grid">')
  for q in Q if direction=='IDA' else reversed(Q):
   p=f'evidencias/{label}_{direction}_{q:03}.jpg'
   # .0/.94 .36 etc always present except reverse lacks final100: report honestly, no duplicate file.
   if not (R/p).exists():continue
   out.append(f'<figure><a href="{p}"><img loading="lazy" src="{p}" alt="{label} {direction} q={q} %"></a><figcaption>{direction} · q={q} %</figcaption></figure>')
  out.append('</div></section>')
out.append('<section><h2>F4 · comparación antes / después</h2><p>Izquierda: F4 original del ZIP CP10. Derecha: mismo motor intacto dentro del nuevo piloto. Comparaciones exactas de píxeles registradas en RESULTADOS.json; estas versiones JPEG sirven para inspección.</p><div class="grid">')
for q in [0,20,40,60,80,100]:
 p=f'evidencias/T34_ANTES_DESPUES_{q:03}.jpg';out.append(f'<figure><img loading="lazy" src="{p}" alt="T34 antes y después {q} %"><figcaption>T34 · p={q} %</figcaption></figure>')
out.append('</div></section></html>');(R/'REVISION_SECUENCIAL.html').write_text('\n'.join(out))
# Contact sheet desktop keyframes, compact enough for direct review on GitHub.
qs=[0,12,28,42,52,64,80,100];tilew,tileh=480,326
im=Image.new('RGB',(tilew*2,tileh*4),'#101116');draw=ImageDraw.Draw(im)
for i,q in enumerate(qs):
 p=R/f'evidencias/escritorio_IDA_{q:03}.jpg'
 if not p.exists():continue
 a=Image.open(p);a.thumbnail((480,300));x=(i%2)*tilew;y=(i//2)*tileh;im.paste(a,(x,y));draw.text((x+10,y+302),f'T45 / q {q}% / CP11 para revision',fill='#efc086')
im.save(R/'evidencias/RESUMEN_CP11.jpg',quality=85)
