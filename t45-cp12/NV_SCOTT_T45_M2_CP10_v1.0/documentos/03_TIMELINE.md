# Storyboard técnico · ocho hitos

Porcentajes orientativos de progreso local, no segundos.

|q|Qué cambia|Cámara / condición|
|---|---|---|
|0.00|Innervision intacta|Parada F4; sin salto|
|0.12|Signo grande|Acercamiento frontal; tipografía sale por encuadre|
|0.28|Arco asciende|Extremos suben y eje se acorta|
|0.42|Cierre visible|Punta cerrada, hombros y pie nacen; cámara casi fija|
|0.52|Pica material|Relleno, pérdida de emisión, soporte gris cálido|
|0.64|Pica registrada|Soporte claro; ornamento original, retirada ya iniciada|
|0.80|Cartas y mano|Foto original, objetos entran por encuadre|
|1.00|Salute intacta|Cubierta entera, logo y título originales|

## Tramos de solape
0–.04: pausa documental. .04–.18: acercamiento; registrar el símbolo de la capa F4 antes de deformarlo. .18–.44: construir la pica, con el cierre visible entre .36–.44. .40–.60: material de soporte y relleno, sin ocultar el contorno. .56–.70: empalme registrado a textura original durante retirada. .70–.94: revelar fotografía y cubierta. .94–1: parada documental.

Usar interpolación de cámara sin sobrepaso; velocidades continuas en los empalmes. No interpolar ciegamente todas las curvas con Catmull–Rom: puede producir bucles o reabrir la punta. Las formas SVG son poses de diseño, no fotogramas que deban mezclarse por opacidad.

## Escala de llegada orientativa
En Salute, centro de pica ≈ (295,298), región de interés x282–310, y278–317. Comprobar visualmente antes de fijar. Centro de cubierta (300,296.5). En .64 encuadre de aproximadamente 100–150 px de ancho de la fuente alrededor del as; en .80 aproximadamente 230–330 px para revelar mano; en 1, contain de los 600×593 originales. Evitar mantener la pica de 28 px a pantalla completa como bitmap.

## Móvil y accesibilidad
Encuadre contain de originales en extremos; la figura intermedia debe caber en ancho y alto útiles, con mínimo 24 px de margen. Mantener pica centrada; desplazar hacia centro de cubierta al retirarse. No recortar logo ni título al terminar. Movimiento reducido: portadas fijas y avance accesible por hitos, sin zoom profundo ni morph obligatorio. Documentar esa variante por separado de la ruta cinematográfica.
