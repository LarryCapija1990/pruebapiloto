# Aprobación y congelación de F4

Fecha de registro: **2026-10-24 (Europe/Berlin)**.

El usuario revisó el prototipo CP02 y declaró:

> La nueva transición Thunder and Lightning → Innervision ha mejorado muchísimo y queda aprobada creativamente para este piloto.

Esta aprobación pertenece al usuario y cubre **este piloto y esta única transición**. Se registra separadamente de los resultados automáticos: una suite no concede aprobación artística.

## Versión que se conserva

- Movimiento aprobado: **F4 CP02 v1.1**, commit `2c680f925e801ca45f2904deb49a9953c7dd6634`, tag `piloto02-f4-cp02-v1.1`.
- Cierre y empaquetado: **F4 CP03 v1.2**, tag `piloto02-f4-cierre-v1.2`.
- CP03 mantiene byte a byte el motor, la cámara, las curvas, los colores, el ritmo, el CSS y los recursos del prototipo aprobado. Solo cambia tres textos de estado en `prototipo/index.html` para registrar la aprobación y el cierre.
- La versión autocontenida adapta únicamente la carga: integra CSS, JavaScript, shader, geometría e imágenes en un HTML. Su salida se compara con CP02 y con el runtime HTTP, no se presupone equivalencia.

`CONGELACION_CP02.json` conserva los 16 hashes de los archivos del runtime aprobado. `base-cp02/index.html` conserva la presentación anterior. Los otros 15 archivos deben coincidir exactamente. Esta combinación permite reconstruir la base de comparación incluso desde el ZIP acumulativo sin historial Git.

Las pruebas verifican igualdad de píxeles en los estados revisados de escritorio y móvil emulado, reversibilidad y movimiento reducido. No se ha cambiado la dirección artística ni se ha producido ningún otro álbum. No se ha modificado Nero’s Vice.

Los textos «pendiente de revisión» de informes, vídeos y capturas CP01/CP02 son históricos. La aprobación vigente está registrada en este documento y en `VERSION.json`; no se reescribe la evidencia histórica.

## Regla de recuperación y futuros cambios

No mover ni reutilizar los tags de CP02 o del cierre. Cualquier modificación posterior debe crear otra versión, conservar este punto y volver a verificar las partes afectadas. Las limitaciones de plataforma y rendimiento del informe de cierre no deben confundirse con una aprobación técnica de todos los dispositivos.
