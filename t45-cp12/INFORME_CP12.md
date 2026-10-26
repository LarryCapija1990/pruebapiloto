# CP12 v1.0 · Informe de la revisión rápida

26 de octubre de 2026. Se conserva M2 y se revisa su ritmo, sin atribuir aprobación al usuario.

## Cambio concreto

El cambio de símbolo a tinta se comprime a **32–39 %: 7 puntos porcentuales locales**. Encendido 32–33,5 %, deformación de cuerpo 32,5–36,5 % y apagado 35–39 %, solapados. La retirada empieza al 35 %, durante el apagado. El símbolo original se mantiene antes del cambio; después no hay capa de eje ni contorno hueco construido por separado.

Se reemplazó la correspondencia poligonal de CP11 por dos campos de distancia, del cuerpo luminoso y de una máscara extraída del JPG del as. El campo de partida se suaviza para impedir aristas de cálculo durante la mezcla; el borde de llegada procede de la máscara raster auténtica con suavizado menor de un píxel fuente. Conserva asimetrías y ondulaciones, sin imponer una pica simétrica. El detalle ornamental sigue siendo el JPG intacto.

El muestreo fotográfico comienza solo al bajar a 2,8 píxeles CSS por píxel fuente y se completa a 2,0. Este umbral depende del viewport: no se impone un macro pixelado durante un tramo fijo. La foto final, mano, cartas, marco y letras se conservan como un plano original único.

## Pruebas ejecutadas

**82 comprobaciones de navegador correctas y 41 estados de topología sólidos: 123 controles, 0 fallos.** Viewports: 1440×900, 1920×1080, 390×844 DPR2 (emulado) y 844×390.

- 24 comparaciones T34 con CP11: exactamente los mismos píxeles en p=0,.2,.4,.6,.8,1. q0 de T45 coincide con el framebuffer F4 final en los cuatro perfiles. La fuente F4 embebida conserva su SHA256 original; 403 archivos del histórico F4 verificados sin cambios.
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
|escritorio|119.45|227.40|299.80|62.8 %|
|grande|196.70|359.50|2680.90|67.9 %|
|movil|88.20|143.10|174.00|53.9 %|
|horizontal|58.35|142.00|211.20|44.7 %|

El nuevo cuerpo necesita un segundo contexto WebGL de 1066×600 y reutiliza su canvas; F4 no se altera. El navegador por software puede sufrir picos. No se certifica fluidez de equipo físico ni calidad cinematográfica definitiva. La fuente de 600 px sigue limitando el ornamento, aunque se retrasa su presentación ampliada.

La materialización del soporte y el descubrimiento del contexto conservan el mecanismo del piloto; su frente de máscara todavía puede percibirse y sigue sujeto a revisión. La aproximación inicial conserva el relevo de capas 12–18 % de CP11. Este encargo se centró en el cambio de cuerpo y su ritmo, sin rediseñar el resto de la escena.

La política de este entorno bloqueó file:// en CP11; CP12 se probó como documento offline sin red, no como apertura nativa de archivo. Se incluye alternativa HTTP local. Móvil emulado; no se ha ensayado lector de pantalla físico ni memoria/temperatura de GPU. El fallback y la arquitectura accesible existentes se conservan, sin repetir aquí todas las pruebas históricas de fallo de WebGL.

## Reproducibilidad y entrega

`python implementacion/construir.py` reconstruye el HTML usando campos ya incluidos, con biblioteca estándar. `preparar_cuerpo.py` reproduce campos/máscara y requiere Pillow, NumPy y SciPy. `probar_cp12.py` requiere Playwright, Pillow y Chromium; genera resultados y capturas en `evidencias/`.

Se conserva `REFERENCIA_CP11.html` para comparación y el paquete CP10 con su F4 original. Los ZIP son independientes y menores de 32 MiB; el paquete de fuentes es acumulativo de esta revisión y su referencia, no del histórico F4 de 210 MB, que permanece en su tag original del repositorio. No se ha modificado Nero’s Vice.
