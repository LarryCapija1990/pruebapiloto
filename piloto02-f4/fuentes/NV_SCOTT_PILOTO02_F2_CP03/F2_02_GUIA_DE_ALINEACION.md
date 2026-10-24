# Guía común de composición y registro

F2 CP03 v1.0 · Objetivos de trabajo, no coordenadas medidas sobre masters.

## Tamaños y archivos

Escritorio: lienzo de trabajo tentativo 3200×1800 px. Móvil: composición independiente 1440×2560 px. Son objetivos de taller; si la herramienta devuelve otro tamaño, registrar dimensiones reales y resolver composición antes de aumentar resolución. No afirmar que ampliar una miniatura recupera detalle auténtico.

Conservar originales en su formato y perfil. Trabajo de edición en documento con capas si se dispone de editor; exportar además PNG reales por capa y máscaras. Composiciones de revisión en PNG; formatos WebP/AVIF y resolución final se decidirán al optimizar la PoC. No convertir prematuramente todos los fondos en una secuencia de vídeo.

Capas de una misma orientación comparten lienzo, origen y dimensiones para reconstruir EXP sin recolocación manual. El alfa debe existir realmente, no un damero pintado. No exigir transparencia para fondos completos. Un PSD/ORA u otro archivo editable solo se entrega si contiene capas reales y se ha abierto para comprobarlo.

## Las tres vistas que deben coincidir

1. **Ancla documental:** frontal completo sin recorte, con relación de aspecto de la fuente aprobada.
2. **Apertura expandida:** el motivo del original ocupa la misma posición que en la última vista anterior. La extensión aparece fuera de su área; nunca se presenta como parte auténtica del master.
3. **Inserto de destino:** recorte exacto de la composición destino aprobada. Su contorno, escala y orientación deben coincidir con la vista de emergencia.

Los logos históricos permanecen en MASTER. La composición escénica puede usar el arte sin tipografía, mediante edición y relleno controlados en una copia, documentando esas áreas como reconstrucción. No pedir al generador que copie palabras ni rediseñar logos. La transición de ancla a escena se resuelve con encuadre y registro: cualquier cambio visible de letras durante la apertura es un fallo a corregir, no un efecto.

## Anclajes tentativos de las cuatro uniones

| Unión | Objetivo escritorio | Motivo de borde origen | Recorte que debe venir del destino | Qué conservar durante cruce |
|---|---|---|---|---|
| T12 | x62 %, y48 % | Curvas en extensión del dragón | Tela roja y señal de asta de C02 | Contorno orgánico visible alrededor del inserto. |
| T23 | x38 %, y65 % | Borde interpretativo de tela | Piedras y señal de guitarra de C03 | Tela delante de parte del terreno; no morph de materiales. |
| T34 | x56 %, y38 % | Región interpretativa junto a impacto | Arco cálido sobre campo oscuro de C04 | Rayo exterior distinguible del arco interior. |
| T45 | x60 %, y58 % | Recorte claro en campo nuevo | Papel, borde de carta y mínima señal de humo de C05 | Campo oscuro alrededor hasta que papel ocupa la vista. |

Origen de coordenadas: esquina superior izquierda del viewport. No mover elementos del original para hacerlos coincidir con estos números. Ajustarlos al componer la extensión y conservar el cambio en GUIDE. Móvil: puntos dentro de x35–65 %, y35–65 % como orientación inicial, evitando áreas de lectura.

## Registro reproducible de la costura

Elegir tres puntos no alineados del detalle de destino (por ejemplo extremos del arco y punto del eje). Registrar sus coordenadas en INSERT y en la vista de emergencia. La escala y posición deben hacerlos coincidir; si necesitan deformaciones incompatibles, cambiar el recorte o cámara. No resolver con un nuevo dibujo parecido.

En 40 % el inserto ocupa aproximadamente 15–25 % del ancho; en 60 %, 65–90 %. Validar la resolución disponible para ese factor de ampliación. Si no alcanza, usar un inserto inicialmente mayor y reducir distancia de cámara. No inventar precisión o detalle macro mediante upscale y llamarlo documental.

Preparar composiciones de control de 0/20/40/60/80/100 %, y al menos una adicional entre 40 y 60 % cuando se inspeccione la costura. Los seis frames exigidos pertenecen al storyboard; el control intermedio evita aprobar solo extremos bonitos.

## Color y materiales

Cada mundo conserva su paleta de referencia. El puente cambia de contexto al entrar, no aplica el mismo filtro a los cinco discos. Mantener textura de ilustración, impresión o fotografía según corresponda. Superficies mates, sombras legibles, sin HDR, plástico 3D, brillos agresivos, viñeta o bloom añadido. En Thunder e Innervision conservar la luz propia del motivo sin convertirla en pantalla blanca.

No incorporar texto, firma, marca de agua, nuevos símbolos o adornos. Los símbolos ya presentes se preservan por composición del master, no se reinterpretan. Las instrucciones generales de cámara fotográfica no deben cambiar una ilustración histórica en fotografía.

## Movimiento sin nuevas vistas falsas

Limitar paralaje a planos delanteros con relleno suficiente detrás. No orbitar, voltear capas ni mostrar el reverso de guitarra, bandera, dragón o mano. La profundidad puede sugerirse con escala relativa; no requiere reconstrucción 3D. Si al desplazar una capa aparece una zona no documentada, marcarla como reconstrucción y restringir su exposición.

En la revisión inversa, todos los estados reaparecen idénticos. Humo, estrellas y descarga deben ser estáticos o depender de posición de scroll; no introducir un clip autónomo como solución de continuidad.
