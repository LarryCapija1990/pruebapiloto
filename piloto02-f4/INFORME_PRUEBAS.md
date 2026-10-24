# Piloto 02 — F4 CP01 v1.0 · Informe de pruebas

Fecha: 24-10-2026. Alcance único: **Thunder and Lightning → Innervision**. Prototipo autónomo con recursos visuales CP05. No se ha modificado Nero’s Vice ni se han integrado otros álbumes al runtime.

**Resultado: prototipo ejecutable y validado técnicamente en los escenarios ensayados. Pendiente de revisión de la experiencia en funcionamiento y de aprobación visual/cinematográfica.**

## Integridad y reconstrucción

Los dos ZIP se extrajeron en `fuentes/`, preservando nombres y rutas internas. Ambos archivos pasaron CRC; no hubo rutas escapadas ni colisiones con contenido diferente. Se reconstruyeron **145 archivos fuente**. Las **80 entradas del manifiesto CP05** coinciden con SHA-256. Están presentes capas, máscaras, escenarios, estados, documentación y los once fotogramas de referencia. Los originales de CP04 permanecen sin modificar: Thunder 600×593 e Innervision 600×594. Sus hashes figuran en `evidencias/integridad-fuentes.json` y los hashes de los dos ZIP recibidos en `VERSION.json`.

Se leyeron `00_LEEME_CP05.md` y `documentacion/01_IMPLEMENTACION_POSTERIOR.md` antes de desarrollar. CP04 es histórico: su inserto y su máscara ovalada no se cargan ni se usan en F4. La documentación antigua no amplía este encargo.

## Implementación verificada

- Vista fija a pantalla completa, progreso absoluto por scroll y control de recorrido a pasos de 0.1 %, reversible. Teclado, botones de extremos y toque funcionales.
- Transformación del cielo por campo irregular de umbral y máscara de cielo oscuro CP05; estrellas RGBA independientes, con identidad y posición constantes. No existe un contenedor rectangular de Innervision dentro de Thunder.
- Ascenso del terreno según `280·smoothstep(0.30,0.80,p)`: valores comprobados a 30, 40, 50, 60, 70 y 80 %, con tolerancia ±0.25 px por cuantización del scroll.
- Correspondencias geométricas derivadas del alfa de las capas RAYO_EJE de CP05; interpolación Catmull–Rom, color frío→cálido y relevo al master del signo. Eje y arco se revelan por separado; el master no se deforma.
- Empalmes documentales registrados en 0–10 y 90–100 %: escala uniforme compartida y restitución localizada de píxeles originales, con retirada de las extensiones. No se funden globalmente las dos portadas.
- El runtime **no solicita ninguno de los once fotogramas ni los fondos compuestos por estado**. Las geometrías se derivaron offline de las capas del trazo, no de las composiciones completas.
- Ninguna capa usa tiempo, ruido nuevo o acumulación. Al detenerse el scroll, se detienen imagen y programación de nuevos renders.

## Pruebas ejecutadas

Chromium 154.0.8037.57, headless con SwiftShader forzado para reproducibilidad. Perfiles: escritorio 1440×900 DPR1; móvil 390×844 DPR2 con táctil emulado; móvil pequeño 320×568 DPR2; horizontal 844×390 DPR1. El buffer interno limita DPR a 1.5 y área a 2.5 megapíxeles. **La emulación no equivale a un dispositivo físico.**

Resultado consolidado: **104 comprobaciones aprobadas, 0 fallidas pendientes**, más **2 pruebas táctiles aprobadas**. Ver JSON de resultados, registros y scripts incluidos.

| Comprobación | Resultado |
|---|---|
| 0 → 60 → 30 → 60 → 100 en los cuatro perfiles | El 60 % devuelve exactamente los mismos píxeles (SHA-256 del canvas). |
| Pausa en 53.7 % durante 600 ms | Imagen idéntica y contador de renders sin incremento. |
| Rueda, teclado Home/End/flecha y ambos botones | Funcionan en los cuatro perfiles; se espera el estado realmente dibujado. |
| Scroll táctil y toque directo sobre el control | 2 comprobaciones adicionales aprobadas en Chromium emulado. |
| Controles en 0/25/40/45/50/55/60/65/70/75/90/92.5/95/97.5/99/100 % | Visibles dentro del viewport y sin elemento que intercepte su centro, en escritorio y móvil. |
| 201 posiciones, cada 0.5 % | 201 imágenes distintas. Diferencia media máxima: 9.533/255 al entrar en 7 %; umbral de diagnóstico 15/255. |
| Diez empalmes a ±0.1 % | Diferencias menores de 5/255 a ambos lados; sin salto detectado por esta métrica. |
| Movimiento reducido | Preferencia del navegador respetada desde inicio y conmutación manual funcional; cámara/terreno fijos, sin trazo geométrico móvil. Los dos originales completos siguen accesibles. |
| Restaurar modo normal al 60 % | Recupera los mismos píxeles que antes de activar movimiento reducido. |
| Errores JS, consola y peticiones en flujos normales | 0 errores de JavaScript, 0 errores/avisos de consola, 0 cargas fallidas y 0 HTTP 4xx/5xx. |
| Fallo deliberado de stars.png | Mensaje específico, reintento y acceso a originales. Separado de los contadores normales. |
| WebGL deliberadamente deshabilitado | Mensaje explícito y enlaces a originales; no se presenta una falsa transición funcional. |

La métrica de diferencia entre imágenes detecta saltos grandes, pero no certifica ausencia universal de artefactos ni aprobación artística. Se inspeccionaron capturas principales y críticas; el índice local permite revisarlas a resolución completa.

## Diagnóstico y correcciones

1. El primer montaje retiraba demasiado pronto el suelo cerca del 60 %. Se reconstruyó el umbral desde las máscaras CP05 después de compensar su desplazamiento; no se inventó otra transición.
2. El trazo inicial era demasiado grueso y aproximado. Se redujo el grosor y se extrajeron sus correspondencias de las capas CP05. Se retrasó la entrada del eje master para reducir la doble línea.
3. La marca vertical del borde del escaneado aparecía demasiado pronto al retirar la cámara. Se restituye el perímetro al final del empalme documental.
4. Había una pausa visual no intencionada entre el 10 y el 12 %. El relevo del rayo comienza ahora al terminar la apertura; el recorrido final tiene 201 estados distintos.
5. Una comprobación inicial de botón falló por esperar únicamente 120 ms. Se verificó que el scroll sí alcanzaba el extremo y el render llegaba después. La prueba espera el estado dibujado y registra la latencia observada, en lugar de equiparar un timeout corto con un destino incorrecto.
6. La reducción bilineal de capturas a 320×180 exageraba diferencias del grano y activó dos diagnósticos falsos de salto. Se contrastó a 39.9→40 %: bilineal 6.1016/255, filtrado alto 1.9894/255 y Pillow bicúbico 1.9545/255. Se corrigió el instrumento y se repitieron las 201 posiciones y los diez empalmes, **sin relajar sus umbrales**. Los resultados anteriores se conservan como diagnósticos históricos y no se confunden con la validación final.

`resultados-pruebas.json` consolida las pruebas de flujo y la revalidación de continuidad. `ejecucion-pruebas.log` conserva la ejecución completa anterior, incluidas las dos advertencias de la métrica de remuestreo, y `revalidacion-continuidad.log/json` demuestra su resolución. La primera ejecución se interrumpió para optimizar el trazo; su registro no se presenta como suite completada.

## Rendimiento y estabilidad

El trazo vectorial se rasteriza únicamente cuando cambia el progreso y se compone como textura RGBA, evitando recorrer 15 segmentos por cada píxel de pantalla. Ocho samplers WebGL1; originales empaquetados en memoria a tamaño nativo. Aproximadamente 3.2 MB de recursos runtime, sin red externa, APIs ni servicios adicionales. No se genera ni decodifica una secuencia de fotogramas.

En 56 repeticiones directas de `draw + gl.finish`, mediana **0.50 ms**, p95 **2.50 ms**, máximo **14.10 ms**. Estas medidas en SwiftShader no incluyen toda la cadena de entrada/composición y **no equivalen a FPS sostenidos**. Latencias observadas del clic al estado comprobado, incluyendo automatización y espera de frames: {"escritorio": 265.2, "movil": 191.4, "movil-pequeno": 122.2, "horizontal": 97.1} ms; son observaciones de laboratorio, no una garantía de respuesta física.

No se registraron pérdidas de contexto durante los flujos normales. La memoria real y la temperatura de un móvil no se perfilaron. El límite del buffer y los recursos fijos reducen el coste, pero falta medir hardware real. La grabación conserva los tiempos observados del navegador y se codifica a 30 fps mediante duplicación de frames cuando procede; **no se sintetiza movimiento ni se afirma render a 30/60 FPS**.

## Limitaciones visuales pendientes

- La reparación del cielo bajo el rayo tiene suavizado y residuos visibles, especialmente en móvil al llenar pantalla; está en la capa fuente CP05. No se regeneró ni se ocultó con efectos.
- Hay diferencias de grano entre originales y extensiones. El material de 600 px y el escenario 1066×600 limitan el detalle en pantallas grandes y acercamientos; no se promete macro ni calidad 4K.
- La transformación del trazo es interpretativa. Aunque deriva de geometrías de CP05 y conserva el signo original, no reproduce todos los detalles de la descarga histórica.
- La rampa paramétrica y las mezclas locales no equivalen exactamente a los nueve fondos estáticos CP05. Se mantiene su mecanismo y su curva de ascenso, con las diferencias documentadas en `DECISIONES_F4.md`.
- El reencuadre final restaura gradualmente textos y marcas del original; su ritmo y su percepción de continuidad necesitan revisión humana. Los límites de la portada escaneada son visibles en el extremo documental, como en la fuente; no se usan como ventana de transformación.
- En móvil el escenario intermedio se recorta por los lados para ocupar toda la pantalla; ambas portadas permanecen completas en los extremos. A 70 % los extremos laterales del arco pueden salir del viewport móvil antes de retirarse la cámara. No se deforma el signo para hacerlo caber. Esta decisión debe revisarse visualmente.
- El modo reducido prioriza cámara y terreno inmóviles y contiene el escenario con márgenes; modifica la puesta en escena para reducir movimiento y conserva la navegación funcional.

## Fuera de la validación

Safari/iOS, Firefox, teléfonos físicos, lectores de pantalla reales, GPU/temperatura/memoria de móvil y continuidad durante una rotación en mitad del recorrido. El perfil horizontal se comprobó por separado. No se declara compatibilidad o rendimiento no ensayados. No se hizo despliegue público ni se validó restauración en una tarea de nube nueva.

## Evidencias y reproducción

Abrir `ABRIR_REVISION.html` para ver MP4 de ida y vuelta, lámina y capturas. Hay PNG en 0/25/50/75/100 %, muestreos adicionales de 40–70 y 90–100 %, movimiento reducido, horizontal y fallo deliberado. Para recorrer el prototipo real: `python3 prototipo/server.py`; instrucciones completas en README. Los scripts de pruebas, regeneración de recursos y grabación están incluidos.

Se guardó `start_skill` en el borrador del entorno de nube con arranque, reutilización del servidor y comprobaciones funcionales. No fue necesario guardar `install_script`: el runtime no instala dependencias. Guardar ese borrador no ejecuta instrucciones ni publica el entorno. Para reutilizarlo mediante el producto, revisar y guardar los cambios en ajustes y publicar el entorno; no se ha realizado esa publicación.

**Próxima decisión: revisar el prototipo en funcionamiento, especialmente 40–70 % y 90–100 %, antes de aprobar la experiencia.**

## Grabación entregada

`evidencias/F4_CP01_ida_y_vuelta.mp4`: captura real 1280×800, 765 frames de navegador en 85.49 segundos de timestamps. Se verificaron los extremos 0→100→0 y los estados intermedios de ida y vuelta. El MP4 a 30 fps duplica capturas cuando corresponde; el entorno con captura y render por software no acredita fluidez a 30/60 FPS. La captura tiene cadencia limitada y queda como limitación de rendimiento de esta evidencia. Sin audio.

## Verificación de la entrega extraída

El ZIP ligero se extrajo en una carpeta temporal independiente y se arrancó en un puerto libre desde otro directorio. Se cargaron las ocho imágenes y se recorrió 0→60→30→60→100: píxeles idénticos al regresar al 60 %, extremos distintos y cero errores JS/consola. El servidor de prueba se cerró al terminar. Ver `evidencias/validacion-entrega.json`. Esto acredita el ZIP local; no una restauración de nube nueva.
