# Reutilización del sistema después de F4

Este documento describe el sistema que se conserva. **No inicia ni implementa nuevas transiciones.** La referencia estable es el movimiento CP02 aprobado, archivado en el cierre CP03.

## Qué se puede reaprovechar

| Componente | Parte reutilizable | Adaptación que deberá revisarse en otra unión |
|---|---|---|
| Scroll y estado | Progreso absoluto 0–1, reversibilidad, pausa, control de recorrido, teclado, botones y gestos | Longitud narrativa del recorrido y textos de cada capítulo |
| Composición | WebGL por capas, alfa real, máscara de umbral con rampa suave, precarga y manejo de fallos | Qué capas existen, su orden y el significado visual de sus máscaras |
| Cámara | Escala uniforme, contención de portadas completas, recorte intermedio, reencuadre reversible | Registro de cada portada y escenario, trayectoria, ascenso y puntos de interés |
| Motivo | Resampleo de un contorno por longitud, correspondencia de puntos, mezcla geométrica, cuerpo/núcleo/halo local | Silueta de origen, correspondencia de destino, anclajes, grosor, color y ritmo |
| Accesibilidad | Alternativa de movimiento reducido, controles visibles, estados accesibles y errores claros | Alternativa visual específica si otro motivo o cámara no admite el mismo tratamiento |
| Rendimiento | Dibujo bajo demanda, límite de DPR 1.5 y buffer de 2.5 MP, recursos locales, presupuesto de ocho samplers | Resolución y número de nuevas capas; ensayo real de GPU, memoria y dispositivo |
| Entrega | Constructor de HTML autocontenido, ZIP local, manifiestos y checkpoint por tag | Lista de recursos de entrada, identidad de versión y comparación con la nueva base aprobada |
| Verificación | Ida/vuelta, pausa, hash de canvas, capturas por progreso, controles, prueba sin red y mediciones | Estados críticos, umbrales de diagnóstico y referencias visuales de cada unión |

El renderer actual contiene datos específicos de Thunder → Innervision. **Reutilizarlo exige adaptar esos datos**, con aprobación y pruebas de la nueva unión; no basta con sustituir los JPG.

## Producción visual específica de cada nueva transición

1. Conservar las dos portadas originales completas, su procedencia y sus hashes. Registrar sus proporciones y el área documental que debe reaparecer al terminar.
2. Producir escenarios y extensiones apropiados para escritorio y móvil, con reparación localizada bajo textos y motivos que vayan a separarse. Revisar costuras y diferencias de grano; una extensión no añade detalle auténtico a un original pequeño.
3. Separar fondo, contexto, motivo y luz en capas con alfa real. Entregar máscaras de reparación y de intervención. Las estrellas separadas solo se reutilizan como mecanismo cuando el nuevo destino las necesita; su identidad y distribución deben corresponder a ese destino.
4. Diseñar el campo de aparición o transformación para el ambiente nuevo. Sus regiones y prioridades deben seguir la composición del arte. El mapa del cielo de Thunder no es una máscara universal.
5. Dibujar y registrar correspondencias de contorno y anclajes entre los motivos nuevos. Definir qué partes conservan curvatura, cuándo se ordenan y cómo se incorporan sus trazos originales. Mantener cualquier transformación interpretativa documentada.
6. Producir referencias de cámara, empalmes documentales y estados intermedios suficientes, especialmente donde cambie el motivo. Los fotogramas son referencias de revisión; no sustituyen una interpolación funcional.
7. Validar cada nuevo enlace en movimiento, en ambas direcciones, al detener el scroll y en móvil. La aprobación de este piloto no aprueba automáticamente esas otras uniones.

## Datos actuales que no deben copiarse sin diseño

- Lienzo **1066×600**; originales Thunder **600×593** e Innervision **600×594**.
- Registro documental en **x=233, y=3** dentro del escenario.
- Retirada del terreno **280 px**, con curva `smoothstep(0.30, 0.80, p)`.
- Campo de cielo CP05 y umbral aproximado **p−0.115**, con rampa suave ±0.13.
- Eje del signo en **x=524**, encuentro con el arco alrededor de **y=418**.
- Contorno irregular inicial, `line-geometry.json`, colores frío→cálido y espesores de este rayo.
- Conservación fotográfica hasta 28 %, relevo 28–46 %, enderezamiento **62–90 %** y entrada del eje **82–90 %**.
- Empalmes documentales **0–10 %** y **90–100 %**; modalidad reducida específica de esta escena.
- Nombres y asignación de recursos en `app.js`, coordenadas y máscaras del shader, anclajes de `motif.js` y lista de entradas del constructor portable.

Estos valores son parte del resultado artístico aprobado. No se generalizan ni se refactorizan durante el cierre de F4.

## Recursos y decisiones conservados

`fuentes/` mantiene las dos partes recibidas reconstruidas en una raíz, con 145 archivos. CP05 es la fuente vigente de esta unión; CP04 conserva los originales y el historial. Los documentos anteriores que describen un inserto o portal son históricos y no definen el runtime vigente.

Se mantienen las capas fuente, máscaras, campo de aparición, escenarios, once referencias estáticas, geometrías, JPG originales, procedencias, scripts de preparación y decisiones CP01/CP02. Se conservan también los diagnósticos corregidos y los límites conocidos; no se borran para presentar una historia de pruebas artificialmente perfecta.

La evidencia CP02 incluye vídeo y comparativas antes/después. El cierre agrega aprobación, hashes de congelación, equivalencia del portable, pruebas funcionales, capturas y rendimiento medido. La infraestructura puede reutilizarse; el diseño visual y la aprobación de cada nueva transición requieren su propia producción.
