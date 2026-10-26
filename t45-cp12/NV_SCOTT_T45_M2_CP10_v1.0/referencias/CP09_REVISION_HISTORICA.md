# PILOTO 02 — SCOTT GORHAM
## Revisión creativa F5.1 · CP09 v1.0
**26 de octubre de 2026 · Innervision → Salute · Documento para elegir mecanismo**

**Estado:** las imágenes CP08 y la ejecución anterior de la ruta A no están aprobadas. La selección previa de A queda reabierta por la revisión del usuario. No hay una nueva dirección aprobada. Thunder → Innervision permanece intacta y aprobada. Este documento no contiene código, nuevas imágenes ni una validación de animación.

## 1. Diagnóstico y cambio de método

Las tres imágenes anteriores compartían temas, pero no una geometría. El signo quedaba a la izquierda, la escena de Salute aparecía a la derecha y el humo suavizaba la separación. Cambiaban la posición de las estrellas, el filamento, los dibujos de las cartas y la mano. La ausencia de un borde rectangular no bastaba: seguían siendo dos composiciones superpuestas.

La nueva unidad de trabajo será **una transformación de un elemento identificable hacia una región precisa de la imagen original**. La cámara seguirá esa transformación y después descubrirá el contexto que ya contiene Salute. No generaremos cada momento de manera independiente. Un único montaje y una misma correspondencia entre puntos deberán producir todos los encuadres.

Los porcentajes de los storyboards son posiciones del recorrido, no tiempos. Las escalas y recorridos descritos son propuestas; no son parámetros medidos en una implementación.

## 2. Reexamen de las fuentes auténticas

Se examinaron nuevamente `21guns.jpg` y `innervision.jpg` aportados por el usuario. Son reproducciones de aproximadamente 600 píxeles de lado, suficientes para identificar motivos, insuficientes para afirmar detalle microscópico. Se conserva además el ZIP F4 CP03 v1.2 LOCAL: su documentación y código identifican un cierre estable y una llegada a Innervision completa. No se repitió aquí una prueba de ejecución de F4.

| Fuente | Observación auténtica | Lo que no demuestra |
|---|---|---|
| Innervision | Campo negro, puntos azulados/blancos, eje naranja vertical, arco elíptico abierto, textura granular del signo, logo superior, título y III. | No hay profundidad estelar medida ni cuerpo tridimensional del signo. Los puntos no son fibras de papel ni partículas físicas documentadas. |
| Salute: escena interior | Dos naipes superpuestos, uno con una pica grande y otro con figura; mano y muñeca con adorno oscuro; filamento de humo por encima; ambiente oscuro cálido. | No conocemos caras ocultas ni un espacio detrás de la mano. No se certifica la causa del humo ni se interpreta la piel como quemada. |
| Salute: exterior | Superficie beige/gris cálida de apariencia rugosa, logo 21 Guns con volumen aparente, marco de la fotografía y título inferior. | La apariencia no identifica por sí sola papel envejecido, piedra o yeso reales. No se inventa una pared arquitectónica completa. |

**Protecciones:** naipes, índices, figura, mano y pulsera deben proceder del original; no regenerarse para completar el movimiento. La pica se toma del naipe real, no de una tipografía genérica. El marco de Salute es auténtico: se puede descubrir al retirar la cámara, pero no utilizarlo como tarjeta flotante durante el cambio de universo.

**Añadidos de CP08:** estrellas nuevas y recolocadas, humo nuevo, beige extendido antes de tiempo, alteraciones del signo, cartas y anatomía. Son interpretación generada, no partes restauradas de las portadas.

**Añadidos posibles de esta revisión:** puntos intermedios, textura ampliada, trayectorias y contornos transitorios. Deben declararse como construcción artística. Los extremos documentales no incorporarán esos añadidos.

## 3. Investigación: estrellas, grano y papel

**Sí, existe una vía visual y técnica plausible para pasar de puntos luminosos a grano; no equivale a demostrar que estas dos portadas ya enlazan bien.** Hay que resolver cuatro cambios: distribución, profundidad, emisión de luz y material del fondo.

- Una estrella es un punto claro sobre oscuro. Un grano de impresión puede ser oscuro sobre claro. Invertir ambos de golpe genera un flash o un negativo: se propone pasar primero por puntos no emisivos gris cálido y solo después separar tinta y soporte.
- Hay pocas estrellas grandes y muchísimos detalles en una textura. No se puede fingir una correspondencia uno a uno entre conjuntos de distinta densidad. Los puntos principales conservarán identidad; el detalle fino surgirá gradualmente entre ellos mediante una textura fija vinculada al mismo plano.
- El cambio de profundidad debe ser visible: los puntos dejan de moverse a velocidades relativas distintas y acaban adheridos a una superficie. Ese momento explica por qué el universo empieza a leerse como materia.
- El grano fotográfico, la trama impresa y las fibras del papel son cosas distintas. Estas reproducciones contienen una mezcla no separada de detalle de imagen, impresión, escaneo y compresión. No presentaremos textura inventada como microfotografía del original.

### Referencias verificables y alcance

| Ref. | Fuente | Qué aporta | Qué no prueba |
|---|---|---|---|
| R1 | [Powers of Ten — Eames Office](https://www.eamesoffice.com/the-work/powers-of-ten/) | Recorrido de escalas con un motivo que mantiene orientación; referencia para acercarse a un detalle y revelar su contexto. | No resuelve esta unión de portadas ni scroll reversible. |
| R2 | [Cosmic Zoom — NFB](https://www.nfb.ca/film/cosmic_zoom/) | Cambio entre escala cósmica y materia mediante animación, comprensible sin palabras. | No permite afirmar que puntos estelares sean físicamente grano de impresión. |
| R3 | [Dissolve con shaders y partículas — Jatin Chopra, Codrops](https://tympanus.net/codrops/2025/02/17/implementing-a-dissolve-effect-with-shaders-and-particles-in-three-js/) | Documenta un campo de ruido común y un parámetro de progreso para coordinar superficie y partículas. | Su movimiento de partículas acumulado en el tiempo no debe copiarse como si fuera reversible por scroll. Se descartan bloom y disolución decorativa. |
| R4 | [Morphing de Luma — Chakib Mazouni, Codrops](https://tympanus.net/codrops/2024/12/09/creating-the-morphing-effect-of-the-luma-dream-machine-website/) | Explica reproducción indexada de secuencias previamente producidas. | El reproductor no crea coherencia entre imágenes. Tener fotogramas y recorrerlos no corrige cambios de identidad. |

Se verificó el contenido documental de estas fuentes mediante búsqueda web; no se reprodujeron íntegramente los filmes ni se ejecutaron sus demos en esta revisión. Las tres propuestas siguientes son inferencias de diseño, no efectos ya observados aplicados a estos discos.

## 4. M1 — Del punto luminoso al grano de la carta

**Idea central:** acercarnos a una pequeña zona estelar hasta que los puntos pierdan distancia y emisión, se conviertan en textura adherida a un plano y, al retroceder, descubramos que ese plano es el naipe original.

**Motivo rastreable:** tres puntos asimétricos —uno dominante y dos secundarios— se asignan a tres marcas concretas de una región del as. Esas marcas se elegirán sobre el original antes de producir nada. No convertir la estrella en toda la carta de golpe.

**Destino recomendado:** una región del límite entre pica oscura y soporte claro, alejada del índice y del dibujo de la segunda carta. Así el cambio negro/claro tiene un destino real y no exige inventar símbolos.

### Storyboard M1 · ocho momentos
| Momento | Transformación visible | Cámara y continuidad |
|---|---|---|
| 1 · 0 % | Innervision íntegra, exactamente en la parada final de F4. | Frontal estable. |
| 2 · 12 % | Se selecciona un pequeño grupo estelar; el signo sigue identificable. | Aproximación diagonal suave al grupo. El signo sale por encuadre, no se desvanece en otro sector. |
| 3 · 28 % | Los tres puntos crecen y se separan en profundidad; aparece detalle tenue entre ellos. | Avance por el mismo eje, sin cambio de centro de interés. No se añade una nube de partículas que tape todo. |
| 4 · 44 % | Los puntos pierden brillo propio y se aplanan; su alrededor adquiere grano mate gris cálido. | El avance desacelera. Disminuye el movimiento relativo entre puntos: empezamos a reconocer una superficie. |
| 5 · 58 % | Se distingue la frontera irregular tinta/soporte del as, todavía demasiado cerca para reconocer la carta entera. | Inicio gradual de retirada, manteniendo las tres marcas en el mismo lugar de la superficie. No hay marco del naipe dentro de otro fondo estelar. |
| 6 · 74 % | Aparecen pica completa, borde de carta, segunda carta y dedos que ya pertenecen a esa fotografía. | Retirada continua. Los objetos entran desde fuera del encuadre; no se materializan por opacidad en medio de la imagen. |
| 7 · 89 % | Mano, humo original, ambiente y borde real de la fotografía. | Se completa el registro con Salute y continúa la retirada. El humo no participa en el cruce. |
| 8 · 100 % | Salute completa con logo, proporciones y título intactos. | Parada documental. |

**Regreso:** 8→6 acerca el as; 6→5 vuelve a la misma región; 5→4 conserva las tres marcas mientras cambia soporte y emisión; 4→3 recupera profundidad; 3→2 reduce escala del grupo; 2→1 revela el signo. No regenerar grano ni seleccionar otra estrella al invertir.

**Recursos:** recorte original registrado de la región del as; mapa de tres anclas; textura intermedia fija de detalle moderado; máscara de tinta/soporte; posiciones iniciales/finales de puntos; plano maestro de Salute con la mano integrada; originales intactos. No se necesita una mano recortada flotando sobre estrellas.

**Riesgo:** el paso de negro a papel claro puede parecer un fundido. Para aceptarlo, las tres marcas deben seguir reconocibles durante el cambio y la planitud debe leerse antes de revelar la carta. La baja resolución exige un macro corto, sin prometer fibras nítidas. Si falla, reducir la escala, no añadir desenfoque encubridor.

## 5. M2 — El signo se vuelve la pica

**Idea central:** dar una relación formal explícita al objeto más reconocible de cada universo. El arco abierto y su eje dejan de emitir luz y se reorganizan como el contorno y la base de la pica del as. El soporte claro se revela alrededor de esa tinta.

**Diferencia respecto a T34:** no se endereza otra descarga. Cambia una silueta bidimensional completa, pasando de curva abierta y eje a una figura cerrada. Aun así comparte el protagonismo de un signo central con T34: esa posible repetición pesa en su evaluación.

### Storyboard M2 · ocho momentos
| Momento | Transformación visible | Cámara y continuidad |
|---|---|---|
| 1 · 0 % | Innervision original completa. | Misma parada que F4. |
| 2 · 12 % | El signo ocupa la mayor parte de la vista, con estrellas periféricas. | Avance frontal centrado en la intersección del arco y eje. |
| 3 · 28 % | Los extremos abiertos del arco suben y se aproximan; la zona inferior se estrecha. | Avance más lento; la intersección permanece como ancla. Es una deformación nueva, no el original animado como si fuera auténtico. |
| 4 · 44 % | Aparece una silueta intermedia de dos hombros y una punta superior; el eje inferior se ensancha hacia la base. | Cámara casi fija para poder leer la transformación. Los extremos cierran de forma visible, nunca mediante un salto de topología oculto. |
| 5 · 58 % | El contorno coincide con la pica real; el naranja pierde emisión y se vuelve tinta oscura. Aparece soporte mate alrededor. | Retirada incipiente. Las estrellas restantes se incorporan a grano local, sin quedar en una mitad separada. |
| 6 · 74 % | Se revelan los detalles interiores auténticos de la pica y el resto del as, después la segunda carta y dedos. | Retirada desde la pica hacia el naipe entero; el dibujo original toma el relevo únicamente cuando escala y contorno coinciden. |
| 7 · 89 % | Mano, humo y escena interior de Salute íntegros. | Retirada frontal, sin rotar la mano ni mostrar reversos. |
| 8 · 100 % | Salute documental completa. | Composición idéntica a la fuente. |

**Regreso:** el contexto sale por encuadre, se recupera la pica, se retira el soporte mientras la tinta gana emisión y el contorno se abre de nuevo en arco y eje. La apertura debe recorrer los mismos puntos que el cierre. Nada de reemplazar una figura por otra en negro total.

**Recursos:** extracción fiel de pica y signo; correspondencias de contorno; máscara de cierre; estados intermedios de silueta dibujados sobre el mismo registro; textura original de la pica; soporte y original Salute. Los detalles ornamentales no deben deformarse durante toda la transición: entran después de registrar la silueta.

**Riesgo:** no hay equivalencia geométrica natural perfecta: el arco es abierto y la pica cerrada; el eje atraviesa el conjunto. Hay que diseñar ese cambio, no pedir un morph automático. Puede parecer un símbolo nuevo arbitrario, repetir el recurso del signo de T34 o dar una lectura heráldica ajena al álbum. Descartar si el momento 4 no anticipa la pica sin explicación verbal.

## 6. M3 — El espacio se convierte en la superficie de la cubierta

**Idea central:** retirar profundidad al universo hasta que sus puntos se lean como irregularidades de una superficie mate. Esa superficie es la zona exterior beige de Salute. La cámara se desplaza por ella hasta descubrir el marco y su fotografía; después retrocede para revelar el frontal.

**Motivo rastreable:** un grupo triangular de puntos se convierte en tres irregularidades del campo exterior. El destino está en una zona próxima al marco, sin letras. No se fabrican cartas a partir de estrellas: se descubre la escena original al recorrer una superficie que ya la contiene.

**Diferencia con M1:** M1 cambia de escala para entrar en un detalle del naipe y salir hacia la mano. M3 cambia el espacio entero por una superficie continua y utiliza un desplazamiento lateral para descubrir la fotografía. Es una revelación de la cubierta como objeto gráfico, no un macro de la carta.

### Storyboard M3 · ocho momentos
| Momento | Transformación visible | Cámara y continuidad |
|---|---|---|
| 1 · 0 % | Innervision original completa. | Parada F4 intacta. |
| 2 · 12 % | Un área estelar lateral gana tamaño y el signo queda fuera por encuadre. | Aproximación oblicua breve. El destino permanece delante, no a un lado como imagen superpuesta. |
| 3 · 28 % | Los puntos se acercan a un plano común y dejan de emitir luz. | Se reduce el avance; una leve deriva lateral permite leer el aplanamiento. |
| 4 · 44 % | Aparece textura mate beige/gris en todo el campo; tres irregularidades conservan el patrón del grupo inicial. | Cámara rasante muy suave, sin relieve profundo ni pared inventada. Todavía no hay cartas ni ventana flotante. |
| 5 · 58 % | El borde auténtico del marco entra desde un margen, conectado físicamente a la superficie. | Desplazamiento lateral corto hacia el marco; su sombra/textura proceden del original. |
| 6 · 74 % | Se descubre la fotografía con mano y cartas, como imagen en la cubierta. | Cámara se vuelve frontal y retrocede; las cartas nunca abandonan su contexto original. |
| 7 · 89 % | Se incorporan logo superior y título inferior. | Retirada continua conservando proporciones, sin reconstrucción 3D del logo. |
| 8 · 100 % | Salute completa. | Registro exacto con el frontal. |

**Regreso:** acercarse a la superficie junto al marco; el marco sale por el mismo margen; las tres irregularidades recuperan brillo y profundidad; la cámara retrocede al universo y signo. No atravesar la fotografía ni confundir el relieve aparente con geometría auténtica.

**Recursos:** recorte del campo exterior adyacente al marco; textura ampliada moderada y fija; tres anclas; máscara del cambio de material; frontal entero como plano único; extensión periférica limitada solo si el recorrido la exige.

**Riesgo:** puede sentirse más editorial que cinematográfica y reducir la importancia de mano/cartas. La ventaja es que los objetos no necesitan aparecer ni deformarse. El borde rectangular solo entra una vez desaparecida la lectura espacial del cosmos: es el marco auténtico, no una ventana sobre estrellas. Si se ven a la vez una fotografía rectangular y un universo detrás, la ruta vuelve al fallo anterior y se rechaza.

## 7. Viabilidad para Codex

Evaluación relativa de diseño, no rendimiento medido.

| Criterio | M1 · Grano de carta | M2 · Signo/pica | M3 · Superficie exterior |
|---|---|---|---|
| Motivo central | Tres marcas que pasan de luz a materia | Silueta que cambia de forma | Tres irregularidades y plano continuo |
| Relación con los objetos de Salute | Directa: el detalle pertenece al as | Directa y simbólica | Indirecta pero clara: la cubierta contiene la fotografía |
| Profundidad/cámara | Alta: avance, aplanamiento y retirada | Media: lectura frontal del morph | Media: aplanamiento, desplazamiento y retirada |
| Dificultad de producción | Media-alta por textura y registro | Alta por cambio de contorno/topología | Media-baja con movimiento contenido |
| Riesgo de reinterpretar originales | Medio en macro; bajo al conservar foto | Alto durante el cambio de silueta | Bajo usando el frontal como plano |
| Riesgo de repetir T34 | Bajo | Medio-alto | Bajo |
| Reversibilidad prevista | Favorable con puntos y textura fijos | Viable con contornos diseñados | Favorable con plano y cámara fijos |
| Principal condición de aceptación | Las marcas sobreviven al cambio de material | El contorno intermedio conduce a la pica | La superficie se reconoce antes de entrar el marco |

**Contrato común futuro:** misma posición de scroll debe devolver cámara, color, máscara y puntos idénticos, independientemente de la dirección o del tiempo de espera. No utilizar partículas con vida libre ni humo autónomo. Una semilla aleatoria fija por sí sola no basta si el estado se acumula con el tiempo. Se necesitan trayectorias definidas por progreso.

La pequeña cantidad de estrellas originales obliga a distinguir puntos protagonistas y microtextura secundaria. El detalle nuevo debe permanecer adherido al plano y no cambiar al regresar. El final se registra con el JPG original completo: una aproximación visual no es fidelidad de píxeles. El paso de textura interpretativa a fuente se revisará a escala de uso, sin confiar en un fundido final que tape desalineaciones.

Codex ya dispone de una composición WebGL controlada por progreso en F4. Eso hace plausible este tipo de control, pero no resuelve automáticamente la dirección artística, los contornos ni los recursos. No se propone modificar la transición anterior ni se ha escrito nueva implementación.

## 8. Recomendación y siguiente decisión

**Recomiendo M1 — Del punto luminoso al grano de la carta.** Es el enlace más directo entre la petición de transformar estrellas en materia y el objeto auténtico de Salute. Da una explicación espacial a la aparición de la mano: estaba fuera del encuadre del detalle que acabamos de descubrir. Evita tanto el humo como cortina como la distribución de un álbum a cada lado.

M3 es la alternativa más conservadora si priorizamos fidelidad y un primer resultado de menor dificultad. Renuncia a parte de la sorpresa de entrar en el naipe, pero ofrece una causalidad visual clara. M2 es la opción más gráfica y arriesgada; no la recomiendo como primera prueba porque puede repetir el protagonismo del signo anterior y requiere un cambio de forma menos natural.

**No aprobar imágenes todavía. La decisión actual es elegir M1, M2 o M3.** Tras elegir:
1. Marcar en las fuentes la región de origen, la de llegada y tres anclas de correspondencia.
2. Preparar un único montaje maestro con esos puntos y la cámara definida.
3. Derivar del mismo montaje los momentos 3–6, incluidos dos estados muy próximos a cada lado del cambio decisivo.
4. Comprobar que las marcas se siguen sin explicación, que el cambio inverso devuelve el mismo estado y que Salute se recupera fielmente.
5. Solo entonces encargar extensiones o microtexturas que falten. No producir tres escenas completas mediante prompts independientes.

## 9. Criterios para aceptar el storyboard y conservar el histórico

El mecanismo debe poder describirse como «este elemento se convierte en este detalle concreto»; no «esta portada se va y esta llega». No debe existir un momento partido entre universo izquierdo y Salute derecha. Los objetos entran por encuadre o cambian desde formas rastreables; no aparecen por una máscara sin causa visual. El humo de Salute puede quedar presente en su fotografía final, pero no resuelve ningún enlace.

Los originales deben permanecer intactos en archivos separados y en sus momentos documentales. Las texturas intermedias se identificarán como interpretación, especialmente a esta resolución. El móvil requerirá encuadre específico tras la elección, sin perder las tres anclas.

Se conservan CP06/CP07 como decisiones históricas y CP08 como ensayo no aprobado. Este documento sustituye su recomendación vigente, no borra esos materiales ni los declara aptos para Codex. F4 CP03 v1.2 y Nero’s Vice no se han modificado. No se generaron imágenes ni se programó durante esta revisión.
