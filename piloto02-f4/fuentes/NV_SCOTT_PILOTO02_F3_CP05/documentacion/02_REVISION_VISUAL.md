# Informe de corrección

## Defecto anterior

CP04 introducía un rectángulo de destino dentro de una máscara ovalada. Su negro y sus límites seguían comportándose como una imagen puesta encima de Thunder. La ampliación acentuaba la placa y podía dejar ver sus extremos rectos.

## Corrección

CP05 no utiliza T34_INSERT_RGBA_D ni T34_APERTURE_MASK_D. Separa fondo espacial, estrellas y signo. El cambio de ambiente se extiende por regiones del cielo, mientras el terreno mantiene su presencia hasta salir de la vista. La luz recibe una secuencia propia de alineación y cambio cromático.

Las máscaras laterales de ambos escenarios dejaron de ser dos bandas rectas estrechas: ahora abarcan una zona mayor y sus bordes varían con la altura. Se añadió textura tenue en reparaciones de tipografía para reducir el aspecto excesivamente liso; no se regeneró el núcleo del signo ni la pala/mano del primer plano. Las áreas intervenidas se entregan como máscaras.

## Comprobación visible

- Comparaciones exactas en p040 y p060 frente a los PNG entregados en CP04.
- Once vistas individuales y lámina de nueve momentos para revisar ritmo general.
- Ningún contenedor rectangular de Innervision forma parte de la pila nueva.
- Las estrellas tienen alfa propio y aparecen fuera de la antigua región de inserto.
- Los originales de ambos discos permanecen completos en p000 y p100.

Esta comprobación es visual y de archivos. No es una certificación automática universal de ausencia de cualquier artefacto, ni de animación continua. Los bordes externos del viewport y los márgenes de la presentación documental no son un borde del segundo mundo.

## Limitaciones pendientes

La reconstrucción de cielo bajo la descarga puede mostrar suavizado local; los contornos de roca y nube conservan diferencias entre fuente y extensión. El trazo de transición es más simple que la descarga original y necesita comprobarse en movimiento. El campo estelar procede de imágenes pequeñas; no debe prometerse resolución de macro.

El último ajuste al signo y el paso al frontal deberán verificarse con estados adicionales en F4. La geometría del trazo intermedio no afirma que la descarga histórica tenga forma de símbolo. No se han revisado móvil, consumo de memoria, FPS, teclado ni movimiento reducido en una implementación.

## Recomendación

Revisar si la progresión ambiente→estrellas→signo comunica el cambio solicitado. Mantener este nivel de complejidad para el piloto. No volver a introducir un portal para simplificar la implementación y no avanzar a F4 anunciando que la continuidad ya está validada.
