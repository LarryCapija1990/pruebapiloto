# Revisión y criterios de aceptación · Ruta A

F1 CP02 v1.0 · **G1 aprobado / F1 entregado / G2 pendiente.** Fecha: 23-10-2026. Autor de propuesta: Work; decisión artística: Sebastián. No hay pruebas ejecutadas de animación ni assets producidos.

## Estado de cumplimiento documental

| Requisito del maestro F1 | Entrega | Estado |
|---|---|---|
| Cinco capítulos con original, apertura, planos y puntos de interés | F1_01 y F1_02 | Descrito. |
| Cámara, escala, dirección, ritmo y pausas | F1_02 y F1_04 | Objetivos tentativos, no mediciones. |
| Cuatro uniones con seis keyframes cada una | F1_03 | 24 fotogramas textuales, 0/20/40/60/80/100 %. |
| Reversión 60 % → 30 % por unión | F1_03 | Descrita explícitamente. |
| Microtextos verificables | F1_05 | Fuentes F0 y reservas identificadas. |
| Móvil y movimiento reducido | F1_02 y F1_04 | Propuestas, sin ensayo físico. |
| Recursos faltantes y alternativas simples | F1_02 | Por cada mundo; briefs de producción reservados a F2. |
| No aprobar sin G2 | Todos | G2 pendiente. |

## Qué se pide aprobar ahora

1. La secuencia de cuatro entradas: espacio entre curvas → recorte de tela → detalle junto al impacto → recorte con papel dentro del campo extendido.
2. El patrón «frontal completo / mundo expandido / destino anticipado / cruce / retroceso / frontal siguiente».
3. La decisión de mantener T45 como anidamiento visible, sin transformarlo en el morph luz→humo de B.
4. Los microtextos y la nota provisional del año de Innervision.

Una sola compuerta G2 para el conjunto; las correcciones pueden centrarse en una unión sin desechar las otras. La aprobación del storyboard permite pasar a F2; no declara aprobado el resultado visual futuro.

## Comprobaciones visuales futuras antes de producir el recorrido

| ID | Criterio | Evidencia futura | Rechazo / corrección |
|---|---|---|---|
| V01 | Cinco frontales completos, fieles y sin deformación | Comparación lado a lado con master autorizado en las cinco anclas | Corregir encuadre; no estirar una imagen para llenar pantalla. |
| V02 | Escenario ocupa pantalla durante inmersión | Encuadres horizontales y verticales 20–80 % | Componer extensión propia; no resolver con barras negras permanentes o tarjeta flotante. |
| V03 | Destino visible antes de cruzarlo | Fotogramas 40 % de las cuatro uniones | Si no se reconoce ningún motivo del destino, rediseñar inserto. |
| V04 | La costura se entiende durante el cruce | Comparar 40/50/60 %, incluyendo un estado intermedio no marcado | Rechazar flash, pantalla negra o disolución global que esconda cambio. |
| V05 | Mantener A como mecanismo | Revisión de motivos entre 40 y 60 % | Si rayo se vuelve signo o estrella se derrite en carta, se cambió a B: requiere decisión, no ajuste silencioso. |
| V06 | Cartas, guitarra, logos y anatomía intactos | Recortes de detalle comparados con originales | Reducir zoom antes de inventar letras o reconstruir sin evidencia. |
| V07 | Identidad de cada mundo y ritmo distinto | Revisar las cuatro uniones seguidas | Evitar cuatro portales circulares centrales con el mismo movimiento. |
| V08 | Original separado de interpretación | Revisar rótulos, créditos y texto accesible | No presentar insertos creados como parte histórica de la cubierta. |

La inspección puede empezar con composiciones estáticas en fases posteriores. Una secuencia textual no demuestra V01–V08; solo define qué habrá que mirar.

## Comprobaciones funcionales reservadas a F4

| ID | Prueba | Éxito esperado |
|---|---|---|
| M01 | Parar en 25/55/85 % | No continúa cámara, humo, destello ni partículas. |
| M02 | Recorrer 0→60→30→60→100 y volver | La misma posición devuelve el mismo encuadre y capas, sin acumulación de error. |
| M03 | Repetir subida/bajada rápida y lenta | Ningún frame negro/blanco, salto de máscara ni título deformado. |
| M04 | Saltar a cada capítulo con ratón, teclado y táctil | Llegada al frontal completo y foco de lectura correcto. |
| M05 | Cambiar orientación y tamaño | Mantener capítulo y lectura; no caer fuera de escena ni ocultar controles. |
| M06 | Activar movimiento reducido | Todo el contenido disponible sin zoom, cámara o animación obligatoria. |
| M07 | Bloquear un asset o escena avanzada | Portada/texto y navegación siguen siendo utilizables; alturas estables. |
| M08 | Ensayar móvil real con imágenes de producción | Movimiento y texto legibles, sin inversión de gesto ni bloqueo de scroll. |

Los presupuestos de rendimiento definidos en F0 son orientativos y deberán revisarse con activos reales. No afirmar ahora FPS, memoria o carga satisfactoria. No elegir WebGL por anticipado.

## Primera prueba futura de la ruta elegida

**Candidata:** T34-A. Pregunta falsable: «¿Se reconoce un mundo dentro del detalle de Thunder antes de cruzarlo, se llega al frontal fiel de Innervision y se puede deshacer el viaje sin ocultar la costura?».

**Mínimo:** dos masters autorizados; dos extensiones compatibles; inserto del destino, borde y detalle suficientes; seis estados de F1_03; composición móvil; identificación musical y modo Lectura. La PoC deberá probar avance rasante/ascenso, cruce y retroceso, no solo un zoom centrado.

**Comparación:** T23-A puede requerir menos control de luminosidad, pero el terreno y la guitarra exigen una perspectiva de salida coherente. T34-A se prefiere por su contraste de escala y porque expone pronto un posible fallo de la ruta. T45-A es el punto más débil semánticamente y requiere revisar una composición estática antes de comprometer los cinco mundos.

**Simplificar si:** el paralaje revela agujeros o cantos; empezar por composiciones planas y limitar desplazamiento. Si falta resolución, agrandar el inserto dentro de la extensión y acortar acercamiento. Si aun así no se distingue el destino, rediseñar la unión. No aumentar complejidad técnica para tapar una relación visual débil.

## Riesgos y decisiones pendientes

| Prioridad | Riesgo | Acción siguiente / responsable |
|---|---|---|
| Alta | Se percibe una sucesión de portales arbitrarios | Dirección de arte revisa anticipación y variedad; G2 decide los cuatro puntos de entrada. |
| Alta | Masters insuficientes o sin condiciones de uso resueltas | F2 documenta procedencia y requisitos; no distribuir derivados sin revisión. |
| Alta | T45 parece tarjeta pegada | Revisar inserto y escala; si fracasa, volver a decisión de mecanismo de esa unión. |
| Media | Año 1992/1993 de Innervision sin cerrar | Mantener nota; investigación documental futura, sin cambiar NV. |
| Media | Lectura compite con la cámara | Mantener una idea en cada ancla; probar composición móvil. |
| Media | Confundir «más sencilla» con «ya validada» | A es una hipótesis de menor complejidad geométrica; coste visual aún sin medir. |

## Cierre del checkpoint

Se entregan seis archivos F1 y copia íntegra de los diez F0 dentro de un ZIP acumulativo versionado. El manifiesto de fuentes de F0 conserva 44 registros. No se incluyen masters ajenos, imágenes nuevas, código web ni una PoC. Verificación de empaquetado: nombres, presencia de 24 hitos, lectura UTF-8 e integridad ZIP.

**Siguiente decisión:** aprobar este storyboard A o indicar qué unión cambiar antes de F2. No se requiere escoger herramientas.
