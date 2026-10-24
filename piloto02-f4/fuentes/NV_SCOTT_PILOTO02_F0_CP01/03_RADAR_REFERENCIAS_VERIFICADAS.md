# Radar de referencias: evidencia y transferencia

Consulta: 23-10-2026. Diez referencias finales, más dos preferidas con bloqueo visual. «Verificada» distingue enlace/contenido, mecanismo documentado y comportamiento observado. **No significa que diez demos se hayan probado exhaustivamente.**

Prueba directa: Chrome remoto de escritorio, capturas de viewport aproximadamente 1363×936, rueda/teclado/clic donde se indica. No se probó móvil físico, lector de pantalla, cambio de preferencia del sistema, consumo GPU ni FPS. Los momentos indicados como documentales describen la fuente, no una sesión simulada. Las capturas temporales se usaron para observación; no se redistribuyen en el ZIP.

## Selección y diferencia de mecanismos

| ID | Referencia | Carril | Mecanismo que aporta | Evidencia |
|---|---|---|---|---|
| R01 | The Descent / The Book Without End | B experimental | Espacios anidados en detalles de la imagen | Navegador, ida y regreso parcial |
| R02 | Zoomquilt | B experimental | Continuidad pintada entre escalas | Navegador + explicación del autor |
| R03 | Selva | A/B | Capítulos legibles sobre entorno persistente | Navegador parcial + declaración del creador |
| R04 | Cinematic 3D Scroll, Codrops | A/B experimental | Cámara espacial vinculada al scroll | Tutorial y repositorio del autor |
| R05 | GSAP ScrollTrigger | A funcional | Posición de scroll = posición de animación | Documentación primaria |
| R06 | WebKit Reduced Motion Demos | A funcional | Una segunda experiencia sin desplazamiento visual forzado | Demo documentada por WebKit |
| R07 | Powers of Ten | C, cine | Viaje de escala y regreso al origen | Eames Office/Foundation; no película visionada íntegra |
| R08 | Gorogoa | C, videojuego; experimental | Continuidad por alineación de dibujos/contextos | Editorial oficial; juego no ejecutado |
| R09 | Caroline Leaf: Hand-Crafted Cinema | C, cine/animación; experimental | Materia manipulada fotograma a fotograma | Ficha NFB y documentación de la autora |
| R10 | Animating Pictures with Eulerian Motion Fields | B, investigación experimental | Movimiento local de humo/fluido desde una imagen | Resumen original de investigación; modelo no ejecutado |

Las referencias 1, 2, 4, 8, 9 y 10 aportan mecanismos experimentales distintos. 7–9 proceden de fuera del diseño web. Las referencias funcionales no se presentan como propuestas estéticas para copiar.

## R01 · The Descent — título actual: The Book Without End

[Demo](https://inkwell-press-the-descent.replit.app/). El extractor web no pudo acceder; el navegador sí cargó el sitio. Estado: **observación directa parcial**.

**Momentos observados:** 1) librería con libro abierto; 2) acercamiento al libro, barco dentro de la página; 3) mar y casco ocupando casi toda la vista; 4) acercamiento al ojo de buey y cabina con globo nevado; 5) al subir, regreso de la cabina al casco. El DOM describe siete mundos, pero no se recorrieron todos: tienda, mar, cabina, pueblo, ático, observatorio y estrella. No se certifica el bucle completo.

**Mecanismo:** el siguiente espacio ya está visible en pequeño antes de entrar. La continuidad depende de imágenes dibujadas para encajar, no de un zoom aplicado a fotos arbitrarias.

**Transferencia propia:** en ruta A, anunciar la bandera dentro de una zona de la extensión del dragón antes de atravesarla; conservar encuadre de entrada y salida. No introducir libros, barcos ni bolas de nieve en Scott.

**Recursos/riesgo:** cada unión exige doble composición perfectamente registrada; coste visual alto aunque el render pueda ser 2D. El centro repetido puede volver monótono el viaje. Móvil no probado; propuesta: anclajes verticales propios y menor distancia de zoom. No se atribuye framework, IA ni licencia de assets por apariencia.

## R02 · Zoomquilt

[Obra y explicación](https://zoomquilt.org/). Estado: **observación directa + documentación de autor**.

**Momentos observados:** paisaje surreal con puentes y bandas naranjas; el centro aumenta de tamaño entre observaciones sin scroll; al pulsar la imagen aparece panel con control «Zoom speed»; una acción de rueda altera el control mostrado. No se demostró correspondencia absoluta entre scroll de documento y posición del viaje.

La explicación del sitio describe 46 imágenes anidadas, cada una al 50% de la anterior y cierre circular. Es una obra de avance autónomo, no una prueba de accesibilidad de un relato documental.

**Transferencia:** diseñar el borde común de dos mundos antes de sus interiores. En Scott interesa la costura pictórica; no adoptar el avance perpetuo. Las cinco portadas requieren paradas reconocibles y salida finita.

**Recursos/riesgo:** alta dedicación al dibujo intermedio; resolución multinivel y administración de memoria. No se reutilizan sus imágenes. Móvil no probado; lectura alternativa imprescindible. Valor: ruta A; referencia de continuidad, no de navegación final.

## R03 · Selva

[Demo](https://isolume.studio/selva). Estado: **navegador parcial y explicación del creador**.

**Momentos observados:** 1) Canopy con texto, ave y ruina/follaje detrás; 2) scroll a Understory con encabezado persistente y marcador actualizado; 3) avance a River con otra figura en borde derecho; 4) acción de regreso hacia capítulos anteriores. La escena de fondo se mantuvo muy parecida en estas muestras: no se certifica un gran vuelo de cámara solo por lo que promete el texto.

El creador declara Three.js, geometría creada en ejecución, planos con fotografías y otros elementos generados. También declara respeto a movimiento reducido; esa preferencia no se probó aquí.

**Transferencia:** separar orientación/lectura del espectáculo. Adoptar nombres de capítulos accesibles, anclas y contexto persistente; no su vegetación, sonidos, bloom o viñeta.

**Recursos/riesgo:** mezclar planos y geometría puede abaratar un escenario frente a modelarlo todo. No demuestra que funcione automáticamente con las cubiertas. Móvil y rendimiento no medidos. Ruta C puede aprender su organización, conservando un trayecto más acotado y sin modo de paseo libre.

## R04 · Cinematic 3D Scroll Experiences — Joseph Santamaria / Codrops

[Artículo](https://tympanus.net/codrops/2025/11/19/how-to-build-cinematic-3d-scroll-experiences-with-gsap/) · [Demo](https://tympanus.net/Tutorials/Cinematic3DScroll/) · [Repositorio del autor](https://github.com/JosephASG/codrops-cinematic-scroll-animations).

Estado: enlaces y documentación comprobados; demo respondió sin texto extraíble, **animación no manipulada**. El artículo y repo explican un cilindro con imágenes y una segunda escena con cámara y tipografía ligadas al scroll.

**Tres momentos documentados:** posición distante, acercamiento/cambio de altura, posición próxima y lateral. Son fases del tutorial, no observaciones de ejecución. Existe código de ejemplo, pero no se instaló ni ejecutó en F0.

**Transferencia:** una trayectoria puede coordinar cámara, máscara y texto. Tomar esa coordinación; descartar el cilindro de imágenes porque transformaría los discos en galería y deformaría los frontales.

**Recursos/riesgo:** geometría, texturas y control de cámara; licencia MIT declarada en repo, verificar archivos aplicables antes de reutilizar. El ejemplo incluye suavizado e inercia: no copiar si hace que la cámara continúe después del gesto. Móvil no probado; limitar profundidad, densidad y tamaño de texturas. Aporta factibilidad para C, no valida todavía su dirección artística.

## R05 · ScrollTrigger como contrato reversible

[Documentación](https://gsap.com/docs/v3/Plugins/ScrollTrigger/) · [adaptación de condiciones](https://www.gsap.com/docs/v3/GSAP/gsap.matchMedia%28%29/) · [precio](https://gsap.com/pricing/).

Estado: **documentación primaria**, no test de una PoC. Tres estados documentados: inicio del tramo; progreso ligado a la posición del scroll; fin. La documentación distingue enlace directo (`scrub: true`) de suavizado numérico, que tarda en alcanzar el scroll.

**Transferencia:** reversibilidad debe ser una función de posición, no una cadena de órdenes «reproducir siguiente». Misma posición = misma cámara y misma transformación. Por el encargo, preferir enlace directo inicialmente; no snapping ni inercia posterior a detenerse.

**Recursos/coste:** la página de precios consultada declara la biblioteca gratuita. No requiere suscripción Webflow para esta propuesta; verificar términos de distribución al implementar. CSS/Canvas siguen siendo alternativas. Riesgo principal: cambios de altura, restauración de posición y carga tardía. Móvil: recalcular encuadres por orientación, sin interceptar el scroll nativo. La decisión de librería se reserva para F4.

## R06 · WebKit Reduced Motion Demos + criterio W3C

[Ejemplos](https://webkit.org/blog-files/prefers-reduced-motion/prm.htm) · [W3C 2.3.3](https://www.w3.org/WAI/WCAG21/Understanding/animation-from-interactions).

Estado: página/demo documentada, **sin alternar configuración del sistema**. Tres casos descritos: zoom que se sustituye por disolución; fondo que deja de rotar; selección de versión animada solo cuando la preferencia lo permite. No son observaciones de un teléfono.

**Transferencia:** el visitante puede acceder a los mismos cinco discos, créditos y relaciones sin zoom, trayectorias ni humo animado. Propuesta propia: modo Lectura con portada completa, texto y enlace al capítulo siguiente; recordar capítulo al cambiar de modo. No reducir el movimiento a “la misma animación un poco más lenta”.

**Recursos/riesgo:** coste bajo de gráficos, trabajo real de estructura semántica y foco. No confundir este criterio AAA concreto con una auditoría WCAG completa. Móvil no probado; el ejemplo contempla tap pero nuestro diseño requiere pruebas táctiles. Es una condición transversal a A/B/C.

## R07 · Powers of Ten — Charles y Ray Eames, 1977

[Ficha Eames Office](https://www.eamesoffice.com/the-work/powers-of-ten/) · [explicación Eames Foundation](https://eamesfoundation.org/work/powers-of-ten-and-the-relative-size-of-things-in-the-universe/).

Estado: **documentación de responsables de la obra**, película no visionada íntegra en esta ejecución. Momentos documentados: escala humana; alejamiento a escala astronómica; retorno y entrada en microescala. No se proporcionan timecodes inventados.

**Transferencia:** orientar mientras cambia la escala; reconstruir el punto de partida hace comprensible la distancia recorrida. En Scott, un plano general del frontal después del macro demuestra que seguimos en ese disco. No trasladar distancias científicas a paisajes ficticios.

**Recursos/riesgo:** imágenes de escala consistente y referencias estables; el cine lineal no resuelve interacción reversible. Reutilización de película no propuesta. Móvil: ancla central o lateral constante y rótulo breve. Valor para A y C: alternar expansión y contracción, en lugar de acelerar continuamente.

## R08 · Gorogoa — Jason Roberts / Buried Signal

[Página oficial de Annapurna](https://www.annapurna.com/interactive/gorogoa). Estado: **descripción editorial primaria, juego no ejecutado**.

La fuente documenta ilustraciones que se ordenan y combinan para resolver relaciones. No permite describir aquí tres escenas concretas observadas. Para transferencia se proponen tres operaciones, explícitamente nuestras: separar un marco, alinear dos formas, revelar que una figura pertenece a otro contexto.

**Transferencia:** transformar el borde de una imagen en parte del espacio siguiente. Para Innervision→Salute, el eje puede conservar posición mientras su lectura cambia de luz a humo. Usar la relación contextual, no importar cuadrícula, puzles ni tarjetas.

**Recursos/riesgo:** composiciones hechas para una correspondencia exacta. El juego es una obra comercial; no se necesita adquirirlo para desarrollar esta hipótesis y no se usa su arte. Hay versiones móviles listadas, pero eso no prueba rendimiento de nuestro piloto. A/B: acierto perceptivo a partir de dibujos, no dependencia de realismo 3D.

## R09 · Caroline Leaf — animación directa

[Hand-Crafted Cinema, NFB](https://www.nfb.ca/film/handcrafted_cinema/) · [The Street, colección NFB](https://collection.nfb.ca/film/the_street) · [documentación de la autora](https://www.carolineleaf.com/direct_animation.php).

Estado: fichas NFB accesibles; documentación de autora indexada pero apertura agotó tiempo. **No se reprodujo ni compró el taller.** NFB identifica arena, pintura sobre vidrio y rayado. No se atribuyen escenas concretas no vistas.

**Transferencia propia en tres momentos:** trazo reconocible; manipulación de su masa/contorno; nueva figura reconocible con textura compartida. Aplicable a la curva del dragón que se vuelve pliegue y al signo que se vuelve humo. No se propone imitar personajes, argumento ni fotogramas de Leaf.

**Recursos/riesgo:** dibujo de intermedios y control de continuidad; gran trabajo manual. Una película grabada es lineal: para scroll reversible se necesita acceso determinista a estados. Móvil: intermedios limitados y optimizados; modo estático conserva extremos. Es el fundamento material de B y una alternativa al morph digital con apariencia gelatinosa.

## R10 · Animating Pictures with Eulerian Motion Fields

[Investigación original, Holynski et al.](https://arxiv.org/abs/2011.15128). Estado: **resumen de autores consultado, sistema no ejecutado ni benchmark reproducido**.

Tres operaciones documentadas: estimar un campo de movimiento desde imagen; desplazar características; construir un bucle mediante flujos adelante/atrás. El trabajo aborda fluidos como agua y humo. No es evidencia de una transición entre las dos portadas ni garantía de que una carta permanezca intacta.

**Transferencia:** limitar la animación a una máscara de humo o nube y mantener rígidos mano, cartas, letras y guitarra. Para B, un campo dibujado manualmente puede ser más controlable que adoptar todo el modelo.

**Recursos/riesgo:** máscara limpia, fondo reconstruido y estados estables. Coste computacional/modelo no estimado; no se recomienda inferencia IA en el navegador. Sin compra o servicio obligatorio. Móvil: reproducir solo estados preparados, no generar vídeo. Sirve como investigación ambiciosa y como advertencia: animar un fluido no equivale a narrar un paso entre mundos.

## Referencias solicitadas que no se certifican

**R11 — [The Monolith Project](https://themonolithproject.net/).** El enlace responde, pero en Chrome remoto apareció «Unable to play media» y pantalla gris. No se obtuvieron 3–6 momentos de movimiento. No afirmar mezcla 2D/3D, reversibilidad ni comportamiento móvil. Se conserva como interés del usuario, fuera del cómputo de diez referencias utilizables.

**R12 — [Oryzo AI](https://oryzo.ai/).** Texto del sitio y DOM accesibles; pantalla verde uniforme en las observaciones inicial y posterior a scroll. Contenido identificado como proyecto ficticio de Lusion sobre un posavasos, no producto de IA real. No se observaron cámara, objetos o transformaciones en esta sesión. No inferir coste/peso por el prestigio del estudio. Fuera del cómputo final.

## Descartes y límites del abanico

- TSAM excluida por instrucción del encargo, no reconsiderada.
- Galerías cilíndricas y rotaciones de tarjetas: investigadas como técnica, descartadas como dirección porque no entran en el arte de las cubiertas.
- Portales circulares repetidos: útiles para entender Descent/Zoomquilt, insuficientes como única gramática de cuatro uniones.
- Salpicaduras o distorsión WebGL genérica: no justifican la relación entre discos; deforman con facilidad texto y emblemas.
- Humo/video IA continuo como solución única: no se ha demostrado acceso rápido y exacto hacia atrás ni permanencia de detalles documentales.
- Lo verificado en documentación técnica prueba que existe un mecanismo. Solo una PoC con los assets reales podrá demostrar que produce el viaje de Scott con buena continuidad.
