# Piloto 02 — F4 CP01 v1.0

Prototipo independiente de la transición **Thin Lizzy — Thunder and Lightning → Phenomena — Innervision**, controlada y reversible mediante scroll.

**Prueba funcional pendiente de revisión visual. No se declara aprobada la experiencia ni la calidad cinematográfica.** CP05 es la fuente visual vigente. No se modifica Nero’s Vice ni se incorporan otros álbumes al prototipo.

## Descargar y ejecutar

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

## Evidencias y documentación

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
