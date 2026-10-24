# Cámara y scroll · Especificación narrativa tentativa

F1 CP02 v1.0 · Sin implementación ni medición de rendimiento. Los parámetros ayudan a revisar el movimiento; no fijan tecnología.

## Un solo recorrido reversible

El documento se organiza como cuatro tramos T12, T23, T34, T45, entre cinco anclas documentales C1–C5. Cada ancla muestra un frontal completo y su información. La llegada de un tramo y la salida del siguiente usan **el mismo estado visual**, con continuidad de posición, escala y opacidad. No repetir el frontal para simular otro capítulo.

Unidades propuestas: H es la altura útil y estable del viewport. Como punto de partida, reservar 0,7 H de lectura en cada ancla y 3 H para cada transición en escritorio; 0,9 H y 2,2 H en móvil. Son hipótesis de longitud, no medidas probadas ni segundos. Total aproximado: 15,5 H escritorio y 13,3 H móvil, excluyendo navegación de cierre. Revisar fatiga con materiales reales; nunca justificar un trayecto excesivo solo por completar esta cifra.

El progreso p de cada transición va de 0 a 100 %. El mapa de seis hitos de F1_03 se interpola sin estados aleatorios. En cada p existe un único encuadre y una única posición de cada capa, independientemente del sentido, velocidad o cantidad de veces que se visite.

## Encuadres y escalas

La escala del frontal en las anclas es 1× respecto de su ajuste completo. Para los detalles, hablar de **ocupación de pantalla**, no de ampliar sin límite un JPG pequeño. A 40 %, el inserto ocupa aproximadamente 15–25 % del ancho visible; a 60 %, 65–90 %. La transición entre ambas cifras necesita un detalle suficiente o una composición de mayor resolución. No se promete que las miniaturas de F0 soporten ese aumento.

| Tramo | Objetivo de pantalla tentativo | Trayecto antes del cruce | Trayecto después del cruce | Variación respecto a otros |
|---|---|---|---|---|
| T12 | x62 %, y48 % | Aproximación oblicua, leve derecha | Retroceso para revelar bandera | Curva orgánica, desplazamiento diagonal. |
| T23 | x38 %, y65 % | Descenso junto al asta y entrada baja | Emergencia rasante, luego retroceso | Portal descentrado y cercano al suelo. |
| T34 | x56 %, y38 % | Avance bajo y elevación progresiva | Campo oscuro y retroceso frontal | Mayor cambio vertical y contraste espacial. |
| T45 | x60 %, y58 % | Desplazamiento corto y macro | Retirada más amplia hacia mano y marco | Recuperación de escala humana, cierre desacelerado. |

Estas coordenadas sitúan el inserto en la **composición nueva**; no aseguran que exista allí un hueco del original. Los encuadres definitivos se registrarán con masters. No desplazar un logotipo histórico para hacer sitio al objetivo.

## Curva de recorrido sin avance autónomo

| Progreso | Comportamiento |
|---|---|
| 0–10 % | Frontal estable o casi estable; iniciar apertura con velocidad espacial baja. |
| 10–30 % | Abrir la extensión y seguir el motivo de orientación. |
| 30–40 % | Reducir la velocidad de acercamiento para anticipar el inserto. |
| 40–60 % | Aproximación continua y cruce; mayor desplazamiento por unidad de scroll. |
| 60–70 % | Terminar entrada; reducir avance hasta cero. |
| 70–90 % | Cambiar gradualmente a retroceso dentro del destino, sin corte de cámara. |
| 90–100 % | Registrar frontal completo, reducir desplazamiento a cero. |

La aceleración describe cuánto cambia el encuadre por una distancia de scroll, no una animación que sigue corriendo después del gesto. El giro entre avanzar y retroceder sucede suavemente alrededor de 70 %; no cambia el sentido del scroll del usuario. Este puede seguir bajando mientras la cámara se aleja para revelar el destino. No simular una cámara con inercia añadida.

Los tramos estables no bloquean la rueda ni exigen un tiempo mínimo. El usuario puede pasar rápido, volver, usar teclado o saltar a un capítulo.

## Contrato de reversibilidad y navegación

- Parar en 55 % congela cámara, borde del inserto, atmósfera y cualquier humo. No hay ambiente animado independiente.
- Bajar a 60 % y subir a 30 % recorre exactamente los estados intermedios en orden inverso. No lanzar una animación distinta de «volver».
- Saltar a un capítulo coloca su portada completa y su encabezado; nunca aterriza en un macro sin contexto.
- Volver atrás en la navegación recupera capítulo y progreso si sigue siendo válido. Si cambió la orientación de pantalla, priorizar el ancla documental más próxima frente a reconstruir una posición visual inválida.
- Un recurso tardío no altera alturas ni posición de lectura. En caso de fallo, mostrar el frontal y texto disponibles con navegación a la siguiente ancla.
- La información musical nueva aparece en tramos de lectura. Durante el cruce se conserva identificación breve; no hacerla pasar detrás de una capa de arte.

## Adaptación móvil

Componer verticalmente cada escenario; no cortar el centro del panorama horizontal. Mantener objetivos en franja central de x35–65 % y y35–65 %, ajustando T23 algo más arriba si choca con controles. Desplazamiento lateral aproximadamente a la mitad del planteamiento de escritorio; dos o tres planos como máximo inicial. No usar inclinación del dispositivo ni gestos de pinza obligatorios.

Los frontales completos siguen ajustados a pantalla con margen. Rótulos pueden ir debajo del área principal o en zona editorial reservada para evitar tapar bandera, guitarra o cartas. Propuesta de texto de lectura: tamaño equivalente a 18 px y líneas cortas; verificar en prototipo, no se declara legibilidad probada. El alto de viewport debe estabilizarse frente a las barras del navegador sin interceptar el scroll nativo.

## Movimiento reducido y acceso sin escena gráfica

El modo Lectura ofrece las cinco portadas completas, microtextos, notas y navegación. Sin zoom, viaje de cámara, paralaje ni destellos; un detalle estático de conexión es opcional y no necesario para entender el contenido. Cambiar de modo conserva el capítulo, ubica el foco en su encabezado y no obliga a reiniciar.

Mismo contenido disponible si falla la composición avanzada. Descripciones de imágenes deben distinguir motivo original de extensión interpretativa, evitando narrar como hecho que hay una bandera dentro del dragón.

## Condición técnica reservada a fases posteriores

Primero evaluar composición 2D y máscaras. 2.5D significa unos planos separados, no modelado completo. Solo justificar geometría adicional si la oclusión no se resuelve con las capas aprobadas. No se elige framework ni se incluye código en F1. Los objetivos de peso y rendimiento de F0 son hipótesis para F4, no resultados actuales.
