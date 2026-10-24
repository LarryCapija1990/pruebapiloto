# PoC futura: Thunder and Lightning → Innervision

23-10-2026 · F0 CP01. **Propuesta; no ejecutada.** Responsable de hipótesis: Work. Validación artística: dirección del proyecto. Validación de implementación: futuro equipo técnico en F4; no se simula aquí su aprobación.

## Pregunta que debe responder

¿Podemos partir de una portada auténtica completa, recorrer su escenario ampliado, seguir una descarga que cambia de forma hasta convertirse en el signo de otro disco y llegar a su frontal completo, controlando todos los estados hacia abajo y hacia arriba, sin saltos ni distorsión de los originales?

**Hipótesis falsable:** dos escenarios 2.5D y una transformación localizada rayo→eje/arco son suficientes para que el paso se perciba como viaje y cambio de materia. Si solo resulta creíble con una pantalla blanca/negra que tapa el cambio, con un vídeo autónomo o deformando toda la cubierta, se refuta esta solución de la ruta B.

## Por qué esta unión

T34-a tiene un motivo luminoso verificable en ambos extremos y permite probar dos dificultades a la vez: pasar de suelo con perspectiva a abstracción, y de contorno irregular a geometría simple. Comparada con T23-a (tela→roca), requiere menos superficie oculta y evita empezar por una simulación de tela. T23-a queda como alternativa fuerte, no como una versión de emergencia basada en fundidos.

T45-a (luz→humo) puede ser más decisiva para la personalidad del final, pero su ventana pequeña y detalle de cartas necesitan mejor master. Revisar sus fotogramas en F1 antes de producir toda la experiencia: aprobar T34 no garantiza que las otras tres uniones funcionen.

## Condiciones de entrada a F4

G1: ruta elegida. G2: storyboard y producción visual aprobados. Assets de F3 revisados: dos frontales autorizados, extensiones, máscaras, guía de registro y entradas/salidas. Resolver distintivo del borde de Thunder y edición de Innervision. Si faltan derechos o masters no declarar una prueba con sustitutos como validación de portadas reales.

## Alcance mínimo

- Dos mundos, una unión, texto de orientación y una conexión musical breve.
- Dos frontales sin alteración. Mostrar la diferencia entre frontal y extensión artística.
- Thunder: guitarra/rocas próximas, suelo medio y cielo; descarga aislada.
- Innervision: fondo extendido, puntos y signo separado; no inventar un planeta.
- Puente: una serie limitada de estados aprobados rayo→eje→arco, con máscaras que no toquen letras ni guitarra.
- Dos encuadres, horizontal y vertical, y lectura sin cámara. Sin sonido automático, cuentas, buscador, catálogo ampliado ni integración NV.

## Cinco fotogramas de prueba exploratorios

Estos son puntos de control F0, no el storyboard de seis fotogramas por unión que corresponderá a F1.

| Fotograma | Cámara y materia | Qué debe seguir reconocible |
|---|---|---|
| P1 | Portada Thunder completa; quietud de lectura | Banda, título, guitarra, cielo y proporciones |
| P2 | Escenario fullscreen, aproximación baja entre suelo y guitarra | Perspectiva del terreno, guitarra como escala; ningún canto de recorte |
| P3 | Ascenso y detalle: descarga conserva eje mientras pierde ramificación; arco empieza a formarse | Una línea rastreable, no un borrón blanco; zona de transformación explícitamente artística |
| P4 | Campo oscuro fullscreen y signo ya legible; cámara se retira | Eje/arco alineados; puntos en posiciones estables al invertir scroll |
| P5 | Frontal Innervision completo, exacto | Logo, título, III y proporciones del master |

## Estrategia preliminar, sin implementación

Primero composición de planos con máscaras y estado dependiente del progreso. Evaluar CSS/Canvas/GSAP antes de requerir Three.js. WebGL se justifica si una deformación localizada o la oclusión real no puede obtenerse limpiamente con la opción más sencilla. No usar vídeo largo como controlador principal: debe demostrar búsqueda hacia atrás exacta si se considerara.

La documentación de ScrollTrigger distingue enlace directo del suavizado que sigue avanzando después del gesto [R05]. El piloto debe comenzar con respuesta directa. Rotación del teléfono, resize y restauración de página conservan capítulo/progreso semántico y recalculan encuadre. Carga tardía no puede cambiar la posición de una escena ya leída.

## Presupuestos iniciales propuestos — no resultados

Herramientas: coste obligatorio de suscripción previsto 0 € para una PoC local con herramientas gratuitas; derechos y producción de arte no están cotizados. Nada comprado en F0.

Descarga visual inicial objetivo ≤3 MB; medios de toda la PoC objetivo ≤12 MB en escritorio y ≤6 MB en móvil. Son límites de diseño negociables al evaluar calidad, no garantías. Cargar versiones adecuadas al tamaño y preparar siguiente escena antes de cruzar. El peso comprimido no mide memoria de GPU [T01/T02]: una textura RGBA de 4096×4096 ronda 64 MiB antes de mipmaps; cuatro rondan 256 MiB. Evitar cinco escenarios completos residentes simultáneamente.

Propuesta de esfuerzo para planificar, no cotización ni plazo comprometido: preparar/ajustar assets de una unión puede exigir varias jornadas de diseño; implementar el control exige otra partida independiente. A menor tiempo disponible, reducir número de capas y movimiento, no sustituir el puente por un flash.

## Matriz de aceptación futura

| Prueba | Procedimiento | Criterio propuesto |
|---|---|---|
| Fidelidad | Comparar P1/P5 contra masters registrados | Sin deformación, letras cambiadas ni recorte; bordes completos visibles |
| Reversibilidad | Recorrer 0→100→0 y alternar 70→30→70 con rueda, touch y teclado | Misma posición produce mismo encuadre/máscara; sin reproducir una animación independiente |
| Detención | Soltar entrada en P2/P3/P4 | Cámara y transformación se detienen; ningún humo autónomo altera el estado |
| Continuidad | Inspeccionar al menos 11 posiciones y una captura de ida/vuelta | Sin huecos, bordes de capas, aparición súbita ni pantalla blanca/negra de cobertura |
| Cambio de mundo | Ver unión sin texto explicativo | Se puede seguir un motivo de origen a destino, y distinguir aproximación de transformación |
| Reconocimiento | Ensayo exploratorio con cinco personas no involucradas | Objetivo: cuatro identifican ambos frontales al mostrarlos junto a los originales; anotar respuestas, no afirmar validación estadística |
| Narración | Preguntar qué relación se cuenta | Reconocen a Scott en ambos proyectos; no deducen que son toda su discografía ni años consecutivos |
| Orientación | Detenerse en mitad; saltar a un álbum | Disco y capítulo accesibles; salto llega a frontal estable con foco correcto |
| Movimiento reducido | Activar preferencia y selector manual | Todos los discos/textos disponibles, sin desplazamiento de cámara ni zoom impuesto |
| Teclado/semántica | Tab, Enter, flechas/página y lectura del contenido | Sin trampa de foco; encabezados y textos reales; canvas no es el único contenido |
| Responsive | 1440×900, 1024×768, 390×844, 320×568, 844×390 | Sin scroll horizontal ni controles cortados; distinguir simulación de móvil físico |
| Rendimiento | Registrar dispositivo, navegador, red, carga fría/caliente y frame trace | Objetivo provisional: 95% de frames dentro de 33,3 ms durante recorrido en móvil de prueba; ninguna tarea larga >100 ms repetida. No reportar FPS sin medición |
| Fallo de render/carga | Desactivar WebGL o provocar recurso ausente en entorno de prueba | Lectura disponible y error explícito; no pantalla vacía sin salida |

Los umbrales son criterios de trabajo propuestos, no requisitos ya aprobados por un equipo externo. La prueba perceptiva es pequeña y diagnóstica; sirve para detectar fallos, no para proclamar eficacia universal.

## Evidencia que deberá entregarse

Video de ida/vuelta; secuencia de estados incluyendo intermedio difícil; listado de assets con procedencia; navegadores/dispositivos reales; registros de rendimiento; incidencias y limitaciones. Si solo se entregan capturas, no decir que prueban reversibilidad. Registrar fallos antes de corregir y distinguir una mejora de código de una revisión de arte.

## Cuándo simplificar o descartar

1. Si se descubren zonas inventadas al mover la cámara, reducir lateralidad y profundidad antes de añadir modelos.
2. Si el intermedio parece gelatina o ruido, redibujar estados; un shader más complejo no resuelve una mala correspondencia.
3. Si sobrepasa memoria, reducir dimensiones/capas activas y detalle móvil; no comprimir más el JPG esperando liberar GPU.
4. Si el único paso aceptable es un fundido total, declarar fallida T34-a y probar T23-a o volver a G1; no multiplicar el fallo por cuatro.
5. Si no se reconoce el original al final, corregir registro y composición, no añadir un rótulo que diga qué disco debería ser.

**Salida de esta fase F0:** esta propuesta y sus condiciones. La PoC permanece sin construir.
