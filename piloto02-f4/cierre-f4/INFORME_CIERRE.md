# Cierre controlado de F4 — CP03 v1.2

**Aprobada creativamente por el usuario para este piloto.** Se archiva el movimiento CP02 como una versión estable y recuperable. CP03 incorpora aprobación, empaquetado, pruebas y documentación; no cambia su dirección artística ni su movimiento. No se han empezado los demás álbumes ni se ha modificado Nero’s Vice.

## Estado del cierre

| Elemento | Estado y evidencia |
|---|---|
| Aprobación creativa | Registrada en [APROBACION_F4.md](APROBACION_F4.md), con alcance y commit aprobado. |
| Congelación | 15 archivos de motor/CSS/recursos idénticos por SHA-256 a CP02; en index.html solo cambian tres textos de estado. |
| Scroll y continuidad | Suite general completada: **104 comprobaciones superadas, 0 fallidas**; 201 estados distintos, empalmes y trayectoria de cámara comprobados. |
| Equivalencia del portable | **61 comprobaciones superadas, 0 fallidas**: CP02, HTTP y HTML autocontenido producen los mismos píxeles en los estados comparados. |
| Reversibilidad y pausa | 0→60→30→60→100 recupera los mismos píxeles; 53.7 % queda inmóvil y sin nuevos renders. |
| Escritorio y móvil | Chromium: escritorio 1440×900, móvil 390×844 y 320×568 emulados, horizontal 844×390; 2 pruebas táctiles adicionales superadas. |
| Movimiento reducido | Comprobado desde preferencia de navegador y control manual; conserva la salida aprobada. |
| Errores de aplicación | Cero errores de consola/JavaScript/carga en los flujos normales; los fallos deliberados de recurso y WebGL muestran la recuperación prevista. |
| Fuentes | 145 archivos fuente conservados; 80 entradas SHA-256 CP05 intactas. |
| Paquete | ZIP local con CRC válido; reconstrucción idéntica por SHA-256 en este entorno. |
| Recuperación | Tag estable `piloto02-f4-cierre-v1.2`, manifiestos, fuentes, scripts y evidencias acumuladas. |

Los resultados automáticos no otorgan aprobación artística: esa aprobación viene del usuario. El campo histórico `visual_approval:false` de la suite general indica que la suite no concede esa aprobación; el cierre la registra expresamente por separado.

## Visualización sencilla

Descargar el ZIP local desde `descargas/`, extraerlo por completo y abrir **ABRIR_PILOTO_F4.html** en Chrome o Edge. No necesita Python, terminal, servidor ni conexión a Internet. La guía [RECUPERAR_Y_VISUALIZAR.md](RECUPERAR_Y_VISUALIZAR.md) explica el proceso y la alternativa HTTP de las fuentes.

**Limitación de plataforma comprobada:** Chromium administrado bloquea las navegaciones `file://` con `ERR_BLOCKED_BY_ADMINISTRATOR`. No se afirma haber validado una apertura nativa por doble clic. Se probó el contenido extraído en un contexto de navegador sin conexión mediante `page.set_content`, sin peticiones HTTP/HTTPS, y se comparó con la versión HTTP y con CP02. La alternativa de servidor local sí se ensayó. No se eludió la política del navegador. Esta limitación y el diagnóstico inicial se conservan en los registros.

## Rendimiento medido

La prueba recorre 200 cambios de posición 0→100→0 por perfil, espera al estado y a `gl.finish`, sin captura de vídeo ni de pantalla durante la medición. Mide una respuesta serializada de entrada a dibujo completado, no los FPS máximos de un equipo real. El renderer es Chromium headless con **SwiftShader por software**, no una GPU física.

| Perfil | Mediana | P95 | Máximo | Estado |
|---|---:|---:|---:|---|
| Escritorio 1440×900 | 182.85 ms | 250.00 ms | 532.50 ms | 200 cambios completados; sin errores GL ni pérdida de contexto |
| Móvil emulado 390×844 | 133.05 ms | 184.80 ms | 849.90 ms | 200 cambios completados; sin errores GL ni pérdida de contexto |

**Estas respuestas son lentas en el entorno por software. No constituyen una aprobación de fluidez ni certifican 30/60 FPS.** No se ha medido GPU física, temperatura ni memoria total de un teléfono. El heap JavaScript observado está en el JSON, y no se presenta como memoria GPU ni total. No se altera el movimiento aprobado para intentar compensar esta restricción del entorno.

El cierre técnico queda delimitado a funcionalidad, determinismo, conservación y recuperación en los perfiles ensayados. Una homologación de rendimiento para dispositivos concretos queda fuera de lo verificado y requiere medición física. La aprobación creativa del usuario se mantiene.

## Recursos y decisiones para reutilizar

[REUTILIZACION.md](REUTILIZACION.md) separa infraestructura reutilizable y producción visual específica: máscaras, capas, registros de cámara, contornos, anclajes, ritmos y variantes móviles deben diseñarse y aprobarse para cada nueva unión. No se ha convertido el piloto en un sistema multialbum ni se ha construido otra transición.

Se conservan los originales, capas, máscaras, campo espacial, escenarios, geometrías, referencias estáticas y documentos F0–F3; también CP01/CP02, sus comparativas y diagnósticos. El vídeo CP02 sigue siendo la evidencia de movimiento aprobada; la equivalencia de píxeles y hashes demuestra que el cierre la mantiene.

## Pruebas ejecutadas y repetición

- [Suite general: resultados](evidencias/regresion/resultados-pruebas.json) y [registro](evidencias/regresion.log).
- [Congelación y equivalencia](evidencias/verificacion-cierre.json), [registro](evidencias/verificacion-cierre.log) y [bloqueo file:// inicial](evidencias/diagnostico-file-policy.log).
- [Rendimiento: muestras y método](evidencias/rendimiento.json).
- [Gestos y control táctil](evidencias/resultados-tactiles.json).
- [Integridad y reconstrucción](evidencias/integridad-y-reconstruccion.json).
- [Resumen estructurado](RESULTADOS_F4.json).

Scripts: `verificar_integridad.py`, `verificar_cierre.py`, `medir_rendimiento.py`; suite general y gestos en `../pruebas/`. Las dependencias opcionales están fijadas en `../pruebas/requirements.txt`. El código, las fuentes y las referencias de comparación se incluyen para repetir las verificaciones sin necesitar el historial Git. Ninguna dependencia de pruebas es necesaria para ver el portable.

Los fallos deliberados se distinguen del flujo normal; no se presentan como errores de la experiencia. El bloqueo de plataforma permanece identificado. No hay fallos funcionales inexplicados ni una ejecución vacía de tests.

## Conservación y siguiente alcance

El ZIP acumulativo del tag contiene el cierre junto con toda la historia disponible, y el ZIP local está identificado por SHA-256 en `PORTABLE.json`. `MANIFIESTO_F4.sha256` permite verificar los archivos del checkpoint extraído. Para recuperar, usar el tag y una carpeta nueva, no la rama cambiante `main`.

F4 queda cerrado como checkpoint del piloto creativamente aprobado, con las evidencias y los límites anteriores expresos. No se inicia producción visual ni código de los otros álbumes. Cualquier ampliación debe partir de este punto recuperable y de un nuevo encargo.

## Configuración de nube

Se guardaron las instrucciones de arranque (`start_skill`) apuntando al checkout canónico y al cierre aprobado. El guardado está confirmado como borrador; no ejecuta scripts ni publica una instantánea. Para activar esa configuración en futuras tareas de nube, revisar y guardar los ajustes y publicar el entorno. No se ha validado esa publicación/restauración. La descarga y el uso local del checkpoint son independientes de ese paso.
