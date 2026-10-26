# CP11 v1.0 · T45 M2 · Para revisión

26 de octubre de 2026. Implementación aislada del encargo CP10: Thunder → Innervision (F4 original) seguido de Innervision → Salute. La aprobación de F4 se conserva; T45 no tiene aprobación creativa de animación.

## Ver el piloto sin programar

1. Descarga el ZIP **LOCAL** o **FUENTES** y extráelo por completo. No abras archivos desde la previsualización interna del ZIP.
2. Haz doble clic en **LEEME.html** o **ABRIR_T34_T45_CP11.html**. Elige Chrome o Edge si se abre otro programa. El HTML es autocontenido; no necesita Python, internet ni una carpeta de capas externa.
3. Recorre Thunder → Innervision. Tras la parada en Innervision continúa hacia abajo o pulsa «Continuar a Salute». El segundo tramo tiene un porcentaje propio.
4. Detén el scroll, invierte el recorrido y utiliza el control inferior para revisar puntos concretos. Con Tab puedes alcanzar los controles y con flechas modificar el deslizador. «Siguiente hito» recorre los puntos del checklist.
5. La opción de movimiento reducido usa imágenes fijas y avance por hitos, sin zoom profundo ni morph obligatorio. También sigue la preferencia del sistema operativo.

Visual Studio Code es opcional: abre la carpeta extraída y utiliza Live Server sobre el HTML. No requiere npm ni compilación. Si ya tienes Python instalado, abre una terminal en esta carpeta y ejecuta `py -m http.server 4190` (Windows) o `python3 -m http.server 4190` (macOS/Linux), y entra en `http://localhost:4190/ABRIR_T34_T45_CP11.html`. Cierra la terminal con Ctrl+C. Este enlace solo funciona en tu ordenador; no es una vista previa pública.

La política del navegador de pruebas puede bloquear `file://`. La comprobación offline carga el mismo HTML en un documento sin red; no se presenta ese procedimiento como una apertura nativa local aprobada por esa política.

## Qué incluye

- `ABRIR_T34_T45_CP11.html`: ejecutable offline completo, incluida F4 byte a byte.
- `implementacion/`: módulo T45 legible, plantilla, constructor y pruebas automatizadas.
- `NV_SCOTT_T45_M2_CP10_v1.0/`: paquete original de dirección, originales, geometría y ZIP F4 intacto. Se conservan las decisiones históricas como referencia, sin convertirlas en dirección vigente.
- `INTEGRIDAD_BASE.json`, `INVENTARIO_CP10.json`, `MANIFIESTO.sha256`: trazabilidad de la base y las fuentes.
- `evidencias/`: capturas secuenciales de ida/vuelta, comparación T34, resultados y log real.
- `REVISION_SECUENCIAL.html`: índice de las evidencias. Las capturas son evidencia; el prototipo no las reproduce como una presentación.
- `CAMBIOS_Y_LIMITES.md`: decisiones de implementación y puntos que requieren revisión.

## Reconstrucción y pruebas

Para reconstruir el HTML basta Python estándar: `python implementacion/construir.py`.
Para repetir las pruebas se necesitan Pillow y Playwright para Python y Chromium en `/usr/bin/chromium`: `python implementacion/probar.py`. Son dependencias de verificación, no del prototipo. El script mide este entorno concreto, no certifica dispositivos físicos. Las capturas se guardan en JPEG para respetar el límite de entrega; las comparaciones de píxeles se realizan sobre PNG sin pérdida en memoria.

Se entrega una copia del paquete CP10, no todo el histórico acumulativo F4 de 210 MB: el encargo limita cada ZIP a 32 MiB. La base F4 portable completa y sus recursos embebidos sí están dentro; el checkpoint histórico F4 sigue recuperable en el tag `piloto02-f4-cierre-v1.2` del repositorio.
