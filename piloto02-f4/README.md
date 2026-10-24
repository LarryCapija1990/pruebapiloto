# Piloto 02 · F4 CP02 v1.1

Versión vigente: **CP02**, corrección puntual del rayo. Ver [informe y comparativa CP02](revision-cp02/INFORME_CP02.md). Las evidencias y métricas CP01 indicadas en los apartados históricos se conservan para el antes/después; los archivos de `prototipo/` ejecutan CP02.

Prototipo web independiente de **Thin Lizzy — Thunder and Lightning → Phenomena — Innervision**. CP05 es la fuente visual vigente. CP04 aporta exclusivamente los JPG originales al runtime y permanece como archivo histórico. No se incorpora ningún otro álbum al prototipo ni se modifica Nero’s Vice.

**Estado: prueba funcional para revisión. No se declara aprobada la experiencia ni la calidad cinematográfica.**

## Ejecutar localmente

Requisitos: Python 3.10+ y un navegador moderno con JavaScript y WebGL habilitados. Sin Node, compilación, credenciales, API, CDN ni instalación de paquetes para ejecutar la web.

Desde la carpeta de este checkpoint:

```sh
python3 prototipo/server.py
```

Abrir `http://127.0.0.1:4173` en el navegador local. Esa dirección es de ejecución local, no un despliegue público. `Ctrl+C` detiene el servidor. Puede ejecutarse desde cualquier directorio usando la ruta al script. Si el puerto está ocupado: `python3 prototipo/server.py --port 4174`. No abrir `index.html` mediante `file://`: el shader y las geometrías se cargan por HTTP.

Para probar desde un móvil en la misma red: `python3 prototipo/server.py --host 0.0.0.0`; abrir la IP LAN del ordenador en el puerto 4173. Esta es una opción local y no publica el proyecto en Internet.

## Recorrer y revisar

- Scroll, rueda o gesto táctil: el progreso depende de la posición absoluta de un recorrido de 650 alturas de pantalla. No hay autoavance, temporizador, inercia añadida ni estrellas animadas por tiempo.
- El control «Recorrido» permite detenerse en pasos de 0.1 %. Con el foco en ese control: flechas, Home y End. Los botones Thunder e Innervision llevan a los extremos.
- Probar **0 → 60 → 30 → 60 → 100 %** y regresar; detenerse entre estados redondos, por ejemplo 53.7 %. Revisar 40–70 % y 90–100 %.
- «Reducir movimiento» fija la cámara y el terreno, omite la geometría intermedia y conserva máscaras, estrellas y signo. También respeta `prefers-reduced-motion` desde el inicio. No es necesario activar scroll automático para usarlo.
- Los originales aparecen íntegros en los extremos. El escenario intermedio ocupa pantalla y se recorta horizontalmente en móvil; no se estiran imágenes. En movimiento reducido se contiene el escenario para evitar desplazamientos de cámara.

## Contenido

- `prototipo/`: web autónoma, servidor estándar y todos sus recursos runtime (~3.2 MB).
- `fuentes/`: las dos partes reconstruidas en una sola raíz, con sus nombres y rutas internas originales. Documentación F0–F3 histórica conservada; **no se carga en la experiencia**.
- `DECISIONES_F4.md`: mecanismo y limitaciones de interpolación documentados antes de implementarlos, más ajustes derivados de la validación.
- `INFORME_PRUEBAS.md`: resultados, fallos corregidos, límites y verificaciones pendientes.
- `evidencias/`: capturas, resultados verificables JSON, registro de pruebas y grabación del navegador.
- `pruebas/`: scripts reproducibles y dependencias opcionales para verificación.
- `ABRIR_REVISION.html`: índice local de evidencias, sin necesidad de cargar una aplicación externa.

## Implementación

Una única pasada WebGL compone fuentes separadas. Usa el campo irregular y la máscara de cielo CP05 para revelar el espacio y las estrellas, conserva sus coordenadas, desplaza el terreno según la curva CP05 (0–280 px), interpola correspondencias geométricas del rayo/eje y revela el master del signo con máscaras independientes de eje y arco. No se cargan los once fotogramas ni se usan fondos compuestos por estado en el runtime. El signo master no se deforma.

En 0–10 y 90–100 % la cámara escala uniformemente desde/hacia el original registrado en el escenario, con restauración localizada de píxeles documentales y retirada de las extensiones. No es un fundido global entre las dos portadas. Las marcas escaneadas del perímetro se restituyen al final del reencuadre. Ver las limitaciones en el informe.

Se dibuja bajo demanda con `requestAnimationFrame` al cambiar el scroll, el tamaño o el modo. Sin bucle o ruido temporal. El buffer se limita a DPR 1.5 y 2.5 megapíxeles; fuente 1066×600. Todos los recursos son locales y se decodifican antes del primer estado. Si hay error de carga o WebGL, se informa y se ofrecen reintento y enlaces a los originales; no se simula una transición exitosa.

El trazo se rasteriza como vector sobre una capa RGBA transparente por cada cambio de progreso. No es una secuencia de imágenes. Los dos originales se empaquetan en memoria a tamaño nativo para conservar el límite de ocho samplers de WebGL1.

## Repetir las pruebas (opcional)

La web no necesita estas dependencias. Para probar con Chromium instalado:

```sh
python3 -m venv .venv
.venv/bin/pip install -r pruebas/requirements.txt
# Ejecutar el servidor en otra terminal.
.venv/bin/python pruebas/validar.py
```

El ejecutable Chromium se busca en `/usr/bin/chromium`; puede cambiarse con `F4_CHROMIUM=/ruta/al/chromium`. El script usa SwiftShader verificado por Chromium para hacer reproducible la composición sin GPU física. Esto no mide un teléfono real. El servidor puede cambiarse con `F4_URL=http://127.0.0.1:4174`.

`pruebas/preparar_recursos.py` permite recrear el runtime desde las fuentes. No es un paso obligatorio para ejecutarlo: los recursos ya están incluidos. `pruebas/grabar.py` captura el navegador mediante CDP y usa `ffmpeg` de sistema para guardar el MP4 de ida y vuelta.

## Revisión pendiente

Validar en funcionamiento la fidelidad del trazo, las reparaciones visibles de las fuentes, el ritmo de cámara y el empalme final. Las pruebas automáticas no otorgan aprobación artística. La emulación de móvil no sustituye una prueba física en Android/iOS; Safari y Firefox quedan fuera de la validación de este checkpoint.
