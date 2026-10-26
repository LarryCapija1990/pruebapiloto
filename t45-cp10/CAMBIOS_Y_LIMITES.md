# Cambios y límites · CP11

## Congelación y arquitectura

No se edita ningún archivo de `piloto02-f4/`, ni el tag de cierre F4. El HTML original incluido en CP10 se incorpora íntegro mediante `iframe.srcdoc`, con todos sus recursos embebidos. Su SHA256 es `e478759325b4ad84a7156507961d72be514cb0be5ee8e3fd732d60d2c7ede1c0`, idéntico al cierre aprobado. T34 conserva su progreso p de 0 a 1 y 550vh de desplazamiento efectivo. Se añaden 20vh de parada y 550vh de T45. El contenedor mide 1220svh, cuyo desplazamiento efectivo es 1120 alturas de pantalla.

T45 usa Canvas 2D separado; no altera el shader WebGL de T34. p y q se calculan desde la posición absoluta. No hay vídeo, secuencia de bitmaps, reloj de animación, partículas ni humo añadido. La imagen de Salute se materializa usando un buffer de máscara reutilizable, sin copiar el canvas principal a dos buffers nuevos en cada posición; esta optimización no cambia geometría ni cronograma. El render se programa bajo demanda; el único temporizador de arranque comprueba disponibilidad de F4 y termina al cargar.

Los controles, rueda y gestos de F4 se coordinan con el contenedor exterior. La cámara de T45 q0 copia exactamente el framebuffer final, con el mismo viewport, DPR y estado de movimiento reducido. Se corrigió en desarrollo una carrera que podía copiar el fotograma inicial en lugar del final: la captura fuerza el render F4 p1 antes de copiar y antes de restablecer la posición externa. También se eliminó una restauración diferida de scroll tras redimensionar que podía anular una nueva orden de navegación; ahora el ajuste proporcional de posición es síncrono.

## Construcción de M2

- 0–4 %: parada documental en el fotograma F4 final.
- 4–18 %: aproximación frontal moderada, con límite de encuadre según tamaño útil. Se usa el fotograma real antes de pasar a las capas `space`, `stars` y `symbol` del paquete.
- 18–42 %: correspondencia de 96 puntos entre el arco abierto y el contorno del as; ambos extremos llegan a la misma punta. No se interpolan cadenas SVG de diferente topología ni fotogramas completos. La pose de llegada se ajustó manualmente al raster original, en lugar de adoptar la pica simétrica de la guía.
- 36–52 %: el eje se recoge por coordenadas y aparece el pie. No desaparece simplemente por opacidad.
- 42–59 %: solo tras cerrar la silueta se rellena desde el borde hacia dentro, baja la emisión y se vuelve tinta. El soporte gris cálido cambia en todo el campo entre 40–60 %. Las estrellas pierden contraste sobre ese material; el grano de enlace es fijo y de baja intensidad.
- 56–64 %: el ornamento y el pie originales se incorporan dentro de la silueta registrada mediante el mismo sistema de coordenadas de la fotografía.
- 64–70 %: el soporte da paso a la fotografía mediante un frente radial suavizado, ligado a q. Para entonces ya no hay universo estrellado. Este frente es una construcción de enlace explícita; no es una parte restaurada de la portada ni una mezcla entre dos portadas completas. Se debe revisar si se percibe demasiado como máscara de revelado.
- 54–94 %: retirada monótona, inicialmente muy lenta, acelerada después. La pica dirige el centro antes de desplazarlo al centro de la cubierta. No hay rotación ni planos independientes para la mano/cartas/humo.
- 94–100 %: Salute completa, sin sustituir sus letras, marco, mano, cartas o pica. Solo se escala uniformemente el JPG fuente.

## Límites visuales que requieren revisión

La silueta nueva es un trazado manual, no una segmentación exacta a subpíxel. Durante el cierre puede conservar facetas y asimetrías; el relevo ornamental debe revisarse especialmente en 56–70 %. La fotografía de 600×593 y la pica de unas decenas de píxeles no soportan macro fotorrealista: el ornamento ampliado es blando y el límite se aprecia a pantalla grande. No se ha regenerado ni afilado artificialmente.

La aproximación inicial es moderada para mantener el signo dentro de un encuadre móvil útil. El título y parte del logo pueden permanecer visibles hasta el relevo a las capas alrededor de 12–18 %; por tanto no se certifica que toda la tipografía salga exclusivamente por encuadre. El paso hacia las capas originales usa un relevo corto de su contenido registrado, no un fundido Thunder/Salute.

El frente de soporte 64–70 % puede revelar parte de la carta/contexto durante la materialización, antes de que todo ese contexto entre exclusivamente por retirada. Es una diferencia concreta respecto al ideal del storyboard: no se declara resuelta creativamente. No se utiliza humo ni un destello para ocultarla. La entrega permite revisar el mecanismo y sus límites, sin atribuir aprobación al usuario.

La composición cinematográfica requiere revisión humana en movimiento. Las comprobaciones automáticas cubren determinismo, enlace, fuente y manejo; no deciden si el cierre resulta convincente. El soporte/grano y las formas intermedias son construcción artística nueva, no textura documental de papel.

## Accesibilidad y reutilización

El modo reducido mantiene fotogramas fijos: Innervision hasta el hito de cambio y después Salute, con controles accesibles. El cambio de imagen de esta variante es discreto e intencional, separado de la ruta M2.

Reutilizables: arquitectura de progreso local, separación de módulos, render bajo demanda, embalaje offline, comparación de framebuffers, pruebas de inversión, controles y fallback. Específicos de esta pareja: trazado de pica y pie, correspondencia de ramas, ancla (295,297), capas del signo, colores de tinta/soporte y cronograma de cámara/material. No se ha construido un sistema universal ni otra transición.

## Alcance de las mediciones

Las pruebas se ejecutan en Chromium sin interfaz y render por software SwiftShader; móvil es emulado. El tiempo medido de T45 incluye dibujado Canvas y lectura de un píxel para forzar su realización, no latencia real de input/pantalla ni rendimiento completo de GPU. La memoria JS no es memoria total ni VRAM. No se certifican FPS, suavidad de dispositivo físico, temperatura o consumo. El HTML no hace peticiones HTTP durante la prueba offline; políticas locales de empresa pueden impedir abrir archivos o WebGL.
