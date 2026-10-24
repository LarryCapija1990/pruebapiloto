# F3 CP05 v1.0 · Corrección de integración Thunder → Innervision

23-10-2026. Dirección general del piloto aprobada por Sebastián. Este checkpoint responde a su corrección: estrellas dentro del cielo existente, rayo que evoluciona hacia el signo, ausencia de segunda imagen enmarcada. **Recursos estáticos para revisión F3; animación continua no validada.**

## Cambio de criterio autorizado

T34 sustituye el inserto anidado de CP04 por una transformación localizada del ambiente y de la luz. Es la excepción solicitada expresamente por el usuario, no una modificación silenciosa de las otras rutas. No se incorporan otros álbumes ni se cambia Nero’s Vice.

## Qué abrir

1. `comparaciones/ANTES_DESPUES_p040.jpg` y `ANTES_DESPUES_p060.jpg`: las vistas antes problemáticas, frente al nuevo montaje.
2. `comparaciones/SECUENCIA_CP05.jpg`: resumen de nueve momentos.
3. `fotogramas/`: **once PNG**, 0/10/20/30/40/50/60/70/80/90/100 %.
4. `comparaciones/COSTURAS_ANTES_DESPUES.jpg`: revisión de escenarios expandidos.
5. `documentacion/01_IMPLEMENTACION_POSTERIOR.md`: orden de capas y progresión propuesta, sin código de scrollytelling.

## Recursos nuevos

- Dos escenarios revisados v004, sin modificar los JPG documentales.
- Fondo espacial sin signo y estrellas por separado.
- Estrellas y signo original extraídos como RGBA, sin fondo rectangular opaco.
- Fondo Thunder con reparación localizada bajo el rayo, más rayo original separado.
- Campo irregular de aparición espacial y máscara del cielo oscuro.
- Para cada uno de los nueve estados intermedios: fondo compuesto, estrellas, evolución del rayo/eje y signo, con alfa real.
- Máscaras de intervención de costuras y de las reparaciones locales.

## Qué cambia visualmente

El espacio no entra como una segunda fotografía. Las primeras estrellas aparecen en las regiones oscuras del cielo; las nubes cálidas y el terreno se mantienen durante más tramo. El encuadre asciende y el suelo abandona progresivamente la vista. Una línea de luz interpretativa se alinea hacia el eje vertical y pasa de frío a cálido; el arco se descubre desde su zona inferior hacia sus extremos abiertos. Al final se conserva el momento de portada original completa.

No se aplica un único fundido entre dos portadas completas. La conversión del fondo utiliza una máscara espacial variable y las estrellas, línea y signo tienen progresos independientes. Eso no elimina el uso de mezclas locales de alfa: son recursos de composición, no la superposición uniforme de dos imágenes enteras.

## Dictamen de esta revisión

En las vistas revisadas al 40 y 60 % no aparece el borde rectangular/ovalado del inserto anterior. Se ha eliminado ese recurso de la pila de CP05. La comparación evidencia estrellas distribuidas por el cielo, en lugar de confinadas a una ventana. Esta observación se limita a los fotogramas entregados.

Las costuras laterales se han suavizado con máscaras anchas de contorno variable. Todavía puede percibirse diferencia de grano entre las fuentes de baja resolución y las extensiones generadas. El espacio bajo la antigua tipografía es reconstruido, no detalle documental recuperado. La línea intermedia entre rayo y eje es una propuesta gráfica nueva; necesita comprobar ritmo y grosor en la prueba futura.

No se declara aprobada la animación, la reversibilidad temporal, la versión móvil ni el rendimiento. Los once estados son evaluables y reproducibles; faltan decisiones de interpolación y pruebas de scroll real.

## Conservación

El ZIP conserva los archivos F0, F1, F2 y F3 CP04 tal como estaban en el acumulativo v1.1. Su informe histórico puede describir un portal y defectos que CP05 sustituye. Para esta unión, el estado vigente es CP05. Los originales íntegros siguen en CP04/originales.
