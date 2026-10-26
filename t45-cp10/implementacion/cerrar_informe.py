from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[1];E=R/'evidencias'
a=json.loads((E/'RESULTADOS.json').read_text());b=json.loads((E/'INTERACCION.json').read_text());c=json.loads((E/'CARGA_DIRECTA.json').read_text());assert not (a['failed'] or b['failed'] or c['failed'])
total=a['passed']+b['passed']+c['passed'];images=len(list(E.glob('*.jpg')));htmlsha=hashlib.sha256((R/'ABRIR_T34_T45_CP11.html').read_bytes()).hexdigest();assert b['html_sha256_tested']==c['html_sha256_tested']==htmlsha
rows=[]
for label in ['escritorio','grande','movil','horizontal']:
 old=a['profiles'][label]['timing_ms'];new=b['final_performance'][label];rows.append(f"|{label}|{new['median_ms']:.2f}|{new['p95_ms']:.2f}|{new['max_ms']:.2f}|{old['p95']:.2f}|{new['JS_heap_only_approximate']/1e6:.1f}|")
text=f'''# Informe de ejecución · CP11 v1.0

26 de octubre de 2026. T45 M2 implementada para revisión; **sin aprobación creativa de la nueva animación**. F4 mantiene su aprobación y todos sus archivos.

## Resultado funcional

**{total} comprobaciones correctas, 0 fallos en las ejecuciones finales**: {a['passed']} de regresión, {b['passed']} de interacción/equivalencia final y {c['passed']} de carga directa en contextos nuevos. Hay {images} capturas JPEG reales: ocho hitos, todos los puntos finos del checklist, ida/vuelta, movimiento reducido y seis comparaciones T34 antes/después. El JPEG solo es formato de entrega de evidencia; las comparaciones se hicieron sobre PNG sin pérdida.

La batería principal de 77 se ejecutó antes de dos ajustes acotados finales: excluir del foco el iframe cubierto y reutilizar el buffer fotográfico de máscara. `REVISION_ACCESIBILIDAD.json` conserva las sustituciones exactas y el hash anterior. Las 36 comprobaciones posteriores verificaron el HTML final, reconstrucción exacta de la versión de regresión, gestos, ausencia de cruces, fidelidad final, foco y equivalencia de píxeles en cuatro viewports y siete estados (42,52,64,65,67,69,100 %). Diferencia máxima observada: **1 nivel por canal**, dentro de la tolerancia CP10; corresponde al buffer/composición de alfa, no a una nueva geometría. Las seis cargas directas finales comparan los hashes de 42,52,64 % con los de ida/vuelta anteriores en escritorio y móvil.

HTML final SHA256: `{htmlsha}`.

## Pruebas ejecutadas

- T34 p=0,.2,.4,.6,.8,1 en 1440×900 DPR1, 1920×1080 DPR1, 390×844 DPR2 y 844×390 DPR1: **24 coincidencias exactas**, incluido color y encuadre. El dominio original se mantiene en 550vh efectivos. La navegación de continuación es una adición exterior documentada.
- T45 q0 frente a F4 p1: mismo framebuffer, sin cambio de tamaño/exposición/borde en los cuatro perfiles.
- Capturas q=0,.12,.28,.36,.40,.42,.44,.48,.52,.56,.60,.64,.70,.80,.94,1 y recorrido inverso.
- Ida → vuelta → evaluación directa de q=.42,.52,.64: resultado consistente por perfil. Además, arranque nuevo offline en cada uno de esos tres valores, escritorio/móvil, sin recorrer previamente la transformación.
- Pausa de cinco segundos en q=.5: imagen idéntica y contador de renders sin incremento en cuatro perfiles.
- Resize q=.5 y .8: conserva el progreso dentro de .001, sin saltar de hito.
- Preferencia del sistema de movimiento reducido y botón manual; portadas fijas y controles por hitos. Se documenta como variante separada.
- Deslizador por teclado, controles dentro de pantalla, foco visible por CSS, iframe cubierto inerte y excluido del árbol accesible durante T45; reactivación al volver a T34. No se ensayó un lector de pantalla físico.
- Dos gestos táctiles nativos CDP en sentidos contrarios y rueda dentro del iframe: avanzan/retroceden el recorrido. Son emulación, no un teléfono físico.
- 101 poses de contorno: sin auto-intersecciones estrictas. Extremos coincidentes desde 42 %, sin reapertura posterior. No se rellena la silueta abierta.
- Salute final coincide exactamente con el JPG original sometido solo a su matriz uniforme de cámara; no es una reconstrucción de cartas, dedos o letras.
- Offline: **0 peticiones HTTP/HTTPS**, sin errores JS ni consola en uso normal. Fallo deliberado de WebGL: portada y mensaje útil, con enlace a Salute original. El fallo deliberado se separó de los errores normales.
- Integridad: 403 hashes de F4 sin cambios; 22 entradas del manifiesto CP10 verificadas; CRC del paquete de entrada y base correctos; original documental de Innervision idéntico al embebido en F4. Los ZIP finales se comprueban por CRC y tamaño al construir.

Apertura nativa en este entorno: `{a['native_file']}`. Se respetó ese bloqueo y se abrió el HTML con `set_content` en un contexto completamente offline. **Esta prueba no certifica navegación nativa file:// bajo la política corporativa**. El HTML no exige servidor en un navegador ordinario que permita ficheros locales; se incluye alternativa HTTP local.

## Rendimiento medido

Chromium headless en Linux con SwiftShader forzado; los cuatro perfiles son ventanas/emulación. 100 muestras por perfil, mismo barrido q=.18–1 repetido dos veces. Medición síncrona de dibujado Canvas más lectura de un píxel para forzar realización. No mide FPS de pantalla, latencia total de entrada, memoria GPU, temperatura ni dispositivo móvil real.

|Perfil|Mediana final ms|p95 final ms|Máximo final ms|p95 antes de optimizar ms|Heap JS aproximado MB|
|---|---:|---:|---:|---:|---:|
'''+'\n'.join(rows)+'''

La optimización elimina dos canvas temporales y copias del canvas principal en el tramo de soporte. Reduce el p95 medido, pero persisten picos importantes y el máximo de móvil empeora en este ensayo. **El objetivo de fluidez no queda validado**; no se afirma rendimiento de 30/60 FPS ni estabilidad temporal de hardware. Los dos ensayos ocurrieron en momentos distintos del mismo entorno y no constituyen un benchmark controlado entre dispositivos. El heap es una estimación de la API del navegador, con páginas de comparación abiertas, no memoria total de la aplicación.

## Fallos corregidos y límites abiertos

Se corrigieron una carrera al capturar el cierre F4, una restauración diferida de scroll después de resize que podía anular una orden nueva, y el acceso por Tab a controles cubiertos. El buffer de material se hizo reutilizable tras medir sus picos. En desarrollo también se corrigió una aserción de foco que estaba comprobando T34 tras la prueba de rueda, en vez de entrar primero en T45.

Los límites visuales siguen abiertos y se detallan en `CAMBIOS_Y_LIMITES.md`: contorno manual con posibles facetas, ornamento de baja resolución al ampliarlo, tipografía que puede conservarse hasta el relevo de capas 12–18 %, y frente de material 64–70 % que puede revelar contexto antes de que entre exclusivamente por retirada. No se declaran creativamente resueltos. No hay humo, flash, nueva iconografía ni generación de mano/pica usados para ocultarlos.

El entregable es una prueba reversible para revisión, no una certificación de calidad cinematográfica definitiva ni una publicación de Nero’s Vice.

## Repetición y fuentes de evidencia

- `python implementacion/construir.py`: reconstruye el HTML; solo biblioteca estándar.
- `python implementacion/probar.py`: regresión completa sobre el HTML actual; requiere Pillow, Playwright y Chromium.
- `python implementacion/probar_interaccion.py`: interacción, geometría y comparación final con la versión anterior reconstruida. Requiere los JSON de evidencia incluidos.
- `python implementacion/probar_carga_directa.py`: seis arranques en contextos nuevos, comparados con hashes de ida/vuelta.
- `python implementacion/crear_galeria.py`: índice offline y hoja de contacto.
- `python implementacion/empaquetar.py`: genera manifiesto y dos ZIP menores de 32 MiB; resultados y hashes en `descargas/*_DESCARGAS.json` del repositorio.

`evidencias/RESULTADOS.json`, `INTERACCION.json`, `CARGA_DIRECTA.json` y sus logs permiten verificar números y metodología. Las capturas se consultan en `REVISION_SECUENCIAL.html`. Ninguna captura secuencial se usa para ejecutar la transformación.
'''
(R/'INFORME_PRUEBAS.md').write_text(text)
(R/'CIERRE_TECNICO.json').write_text(json.dumps({'checkpoint':'CP11 v1.0','status':'review candidate, not creatively approved','functional_checks_passed':total,'functional_checks_failed':0,'F4_files_unchanged':403,'evidence_images':images,'html_sha256':htmlsha,'performance_approved':False,'visual_limitations_open':True,'native_file_policy_blocked':True},indent=2))
print('Report written:',total,'checks;',images,'images')
