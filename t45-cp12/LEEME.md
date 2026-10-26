# T45 M2 · CP12 v1.0 · Prueba de ritmo rápido

Esta revisión conserva la dirección símbolo → pica y la transición Thunder → Innervision intacta. El nuevo encendido, transformación de cuerpo y apagado ocupa **32–39 % del progreso local de T45: 7 puntos porcentuales**. La retirada empieza al 35 %, antes de acabar el apagado.

## Abrir sin programar

Descarga el ZIP LOCAL con **Download raw file**, extráelo completamente y abre **ABRIR_T34_T45_CP12.html** con Chrome o Edge. No lo abras desde dentro del ZIP. El HTML contiene todos los recursos; no necesita internet, npm ni Python. Recorre Thunder → Innervision y continúa hacia Salute. Utiliza «Siguiente hito» para entrar en 32–39 % y el deslizador con flechas para detenerte dentro del cambio.

Si el navegador corporativo bloquea archivos locales, puedes abrir la carpeta en Visual Studio Code y usar Live Server sobre el HTML. Con Python ya instalado: `py -m http.server 4191` (Windows) o `python3 -m http.server 4191` (macOS/Linux), desde esta carpeta; después abre `http://localhost:4191/ABRIR_T34_T45_CP12.html`. Ese enlace funciona solo en tu ordenador. Las pruebas del entorno usan carga de documento offline; no certifican una apertura nativa file://, bloqueada por la política en la revisión anterior.

## Qué cambió

- El símbolo fotográfico se mantiene hasta el encendido local. No se repasa con una línea nueva antes de deformarlo.
- La transformación usa campos de distancia del cuerpo del símbolo y de una máscara derivada de la tinta real del as. Cambia todo el cuerpo simultáneamente, incluido el antiguo eje. No hay capa de eje ni trazado independiente que permanezca después del cierre.
- El centro de la pica nace lleno durante la transformación. Se elimina la construcción de una pica cerrada hueca y su posterior relleno lento.
- El pulso naranja se limita a los píxeles del objeto y a su halo local. No hay flash global, humo añadido ni apagón.
- La máscara final conserva la asimetría y el borde de la fotografía. El suavizado inferior a un píxel fuente reduce la escalera del escaneo; no regulariza el signo como pica tipográfica ni emplea el polígono CP11 como borde de llegada.
- La retirada empieza durante la conversión a tinta. El ornamento original se introduce cuando cada píxel fuente ocupa como máximo **2,8 píxeles CSS**, completándose a 2,0. No se mantiene una pica fotográfica de treinta píxeles ampliada a pantalla completa.

## Revisar

Abre `REVISION_CP12.html` en el ZIP de fuentes para ver secuencias de ida/vuelta y comparaciones CP11/CP12 al mismo progreso. El prototipo es continuo; las capturas son solo evidencia. `REFERENCIA_CP11.html` conserva la versión anterior para comparar, no es la revisión nueva.

La dirección está conservada; esta prueba de ritmo **requiere revisión del usuario**. El origen de 600 píxeles sigue limitando el detalle del ornamento; el umbral de escala reduce la ampliación, no crea resolución. El relevo hacia el contexto fotográfico conserva el mecanismo de materialización del piloto y puede percibirse como máscara. El rendimiento medido por software y el móvil emulado no certifican fluidez en equipos físicos.

## Código y reconstrucción

`implementacion/t45.js`: montaje y cámara. `cuerpo.js`: shader del cuerpo. `preparar_cuerpo.py`: máscara/SDF, con Pillow, NumPy y SciPy; los resultados están incluidos en `assets/`, no se calculan al abrir el prototipo. `construir.py`: genera el HTML con Python estándar y los recursos ya preparados. `probar_cp12.py`: comprobaciones con Playwright, Pillow y Chromium `/usr/bin/chromium`.

La base CP10 y F4 se conservan byte a byte. El archivo original F4 incorporado mantiene SHA256 `e478759325b4ad84a7156507961d72be514cb0be5ee8e3fd732d60d2c7ede1c0`. El recorrido T34 sigue teniendo 550vh efectivos y progreso propio. Los tags CP11 y F4 permanecen recuperables; no se ha modificado Nero’s Vice ni se han construido otras transiciones.
