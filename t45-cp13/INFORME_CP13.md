# CP13 v1.0 · Informe de ajuste de ritmo

26 de octubre de 2026. El usuario acepta la apariencia CP12 de Thunder → Innervision → Salute. Se conserva como referencia visual. CP13 se entrega como **primera prueba de distribución de scroll**.

## Resultado

**143 comprobaciones correctas, 0 fallos**: 17 del modelo de distancia y 126 de navegador. HTML comprobado: SHA256 `7de81e83034fa8f17b3c02859d9f77ed998036a9ec8658e534e4b71c12636be7`.

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
