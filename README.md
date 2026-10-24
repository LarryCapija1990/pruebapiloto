# Piloto 02 — F4 CP02 v1.1

Prototipo independiente de la transición **Thin Lizzy — Thunder and Lightning → Phenomena — Innervision**, controlada y reversible mediante scroll.

**Prueba funcional pendiente de revisión visual. No se declara aprobada la experiencia ni la calidad cinematográfica.** CP05 es la fuente visual vigente. No se modifica Nero’s Vice ni se incorporan otros álbumes al prototipo.

**CP02 corrige únicamente el motivo central:** conserva el rayo original al inicio y su curvatura en el centro; el enderezamiento se concentra en 62–90 %, con más cuerpo y luz. Cámara, fondo, estrellas y estructura de la experiencia se mantienen. Comprueba que la cabecera muestra **F4 / CP02**.

Consulta [la comparativa y el informe breve CP02](piloto02-f4/revision-cp02/INFORME_CP02.md). Las evidencias CP01 de más abajo se conservan como histórico.

## Descargar y ejecutar

Versión ligera vigente: [NV_SCOTT_PILOTO02_F4_CP02_v1.1_PROTOTIPO.zip](descargas/NV_SCOTT_PILOTO02_F4_CP02_v1.1_PROTOTIPO.zip). En su página de GitHub, pulsa **Download raw file**. Tras extraerla, usa `py prototipo/server.py` en Windows o `python3 prototipo/server.py` en macOS/Linux.

Checkpoint acumulativo versionado: [F4 CP02 v1.1 — ZIP del tag](https://github.com/LarryCapija1990/pruebapiloto/archive/refs/tags/piloto02-f4-cp02-v1.1.zip).

Para descargar todo el repositorio desde su rama principal:

En GitHub, pulsa **Code → Download ZIP**, descomprime el archivo y abre una terminal en la carpeta que contiene este README.

Con Python 3.10+ instalado:

```sh
# Windows
py piloto02-f4/prototipo/server.py

# macOS / Linux
python3 piloto02-f4/prototipo/server.py
```

Abre `http://127.0.0.1:4173` en tu navegador local. No abras `index.html` directamente: el prototipo carga sus capas por HTTP. No hace falta instalar paquetes para ejecutar la web. Requiere JavaScript y WebGL. `Ctrl+C` detiene el servidor.

Usa scroll, el control «Recorrido» o los botones de extremos. «Reducir movimiento» fija la cámara y el terreno; también se respeta la preferencia del navegador.

## Evidencias vigentes CP02

- [Informe breve y detalle del antes/después a 25, 50, 75 y 90 %](piloto02-f4/revision-cp02/INFORME_CP02.md).
- [Vídeo sincronizado CP01 / CP02](piloto02-f4/revision-cp02/evidencias/F4_CP02_ANTES_DESPUES.mp4).
- [Capturas completas y resultados CP02](piloto02-f4/revision-cp02/evidencias/).

## Archivo y documentación CP01

- [Grabación completa de ida y vuelta](piloto02-f4/evidencias/F4_CP01_ida_y_vuelta.mp4). En su página, usa **Download raw file** para descargarla.
- [Resumen de capturas: escritorio y móvil](piloto02-f4/evidencias/F4_CP01_RESUMEN.jpg).
- [Informe de pruebas, fallos y limitaciones](piloto02-f4/INFORME_PRUEBAS.md).
- [Instrucciones completas](piloto02-f4/README.md).
- [Decisiones de interpolación](piloto02-f4/DECISIONES_F4.md).
- [Resultados técnicos consolidados](piloto02-f4/evidencias/resultados-pruebas.json).
- [Integridad SHA-256 del checkpoint](piloto02-f4/MANIFIESTO_F4.sha256).

Después de descargar, `piloto02-f4/ABRIR_REVISION.html` permite explorar localmente las evidencias. Es un índice de capturas y vídeo; para probar el scroll real, ejecuta el servidor indicado arriba.

El checkpoint incluye el código, recursos runtime, fuentes históricas reconstruidas, documentación, pruebas y evidencias. Los documentos de otras fases se conservan como archivo histórico; el runtime cubre exclusivamente esta transición.

104 comprobaciones técnicas y 2 pruebas táctiles emuladas superadas; además se verificó el prototipo extraído en otra carpeta y puerto. Móvil se probó mediante Chromium emulado, no en un teléfono físico. La resolución, las reparaciones visibles de CP05 y la cadencia de la grabación están documentadas. Los resultados no constituyen aprobación artística.
