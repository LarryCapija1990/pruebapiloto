# Riesgos, decisiones y vocabulario

F0 CP01 · 23-10-2026. Dueño del diagnóstico: Work. G1 pendiente de dirección. Ninguna acción sobre el canon activo.

## Registro de riesgos

| ID | Clase / prioridad | Evidencia o condición | Consecuencia | Respuesta y responsable futuro |
|---|---|---|---|---|
| DOC-01 | Documental / alta | Innervision DINCD 18 1992 frente a CSC 7060 1993; reedición comercial lo describe como álbum de 1993 | Falsa fecha definitiva o falsa secuencia 04→05 | Conservar 1992 provisional y separar año de obra/edición; custodio del catálogo coteja libreto y prueba contemporánea |
| DOC-02 | Créditos / alta | Reseñas discrepan sobre bajo y pistas de Brian May en Innervision | Inventar exclusividad de Scott o relaciones musicales | Priorizar datos de edición; rol de Scott a nivel álbum confirmado, reparto por pista sin cerrar |
| DOC-03 | Narración / media | Cinco discos son una selección | Presentarlos como carrera completa o culminación en 1992 | Texto explícito «cinco paradas del archivo»; no causalidad entre Phenomena y 21 Guns |
| IMG-01 | Recursos / crítica para producción | Muestras pequeñas, sin masters autorizados | Zoom borroso y reconstrucción presentada como original | Conseguir originales permitidos antes de F3/F4; producción visual |
| IMG-02 | Edición / alta | Thunder tiene distintivo lateral en captura; Renegade varía tono; Salute 400×388 | Mezclar ediciones, eliminar arte o estirar frontal | Cotejar frontal/back/matriz y registro de color; no corregir NV por cuenta propia |
| IMG-03 | Derechos / alta | Acceso público no acredita permiso de adaptación | Distribuir assets sin autorización | Dossier enlaza, no redistribuye arte. Obtener autorización/alcance de uso antes de distribuir derivados; sin dictamen jurídico aquí |
| ART-01 | Creativa / alta | Puentes son interpretaciones | Portales repetidos o morph arbitrario | Mantener anclajes de forma, dirección y materia; evaluar intermedios estáticos |
| ART-02 | Fidelidad / alta | Una imagen plana no tiene reverso documentado | Dragón, mano o guitarra inventados | Limitar cono de cámara; rotular extensión; cinco masters separados |
| ART-03 | Continuidad / alta | Paso de luz a humo puede resultar débil | Final de la ruta B desconectado | Revisar T45 temprano en F1; alternativa T45-b solo si conserva viaje fullscreen |
| UX-01 | Control / alta | Demos pueden tener avance autónomo/inercia | Scroll secuestrado, retorno inconsistente | Estado determinista por posición, sin autoplay ni snap forzado |
| ACC-01 | Acceso / alta | Zoom/parallax no esenciales para leer | Fatiga o exclusión | Modo Lectura completo, teclado/foco y preferencia de movimiento reducido |
| PERF-01 | Rendimiento / alta | Muchas texturas grandes ocupan GPU | Pantalla vacía o pérdida de contexto | Dos mundos activos como inicio, reducir dimensiones, liberar recursos, ruta de lectura |
| MOB-01 | Validación / alta | Sin pruebas físicas en F0 | Confundir emulación con experiencia táctil | Matriz de dispositivos en F4; variantes de encuadre vertical |
| REF-01 | Evidencia / media | Monolith no reproduce; Oryzo sin escena visible | Atribuir conductas no vistas | Fuera de referencias finales utilizables; no bloquean investigación restante |
| PROC-01 | Alcance / crítica | Usuario pide exclusivamente F0 | Programación o producción prematura | Cierre en G1; ninguna instalación/prototipo/web realizado |

## Incidencia detallada de Innervision

**Evidencia a favor de 1992:** Musicbase registra Dino Music DINCD 18, código 7392451001716 y matriz CD PLANT MFG DINCD 18 CDM01 [D05]. Musik-Sammler registra un ejemplar con el mismo catálogo y EAN en 1992 [D07]. Discogs indexa esa edición en 1992 [D16], pero su página completa no fue accesible. Musicbase/Discogs pueden compartir datos: no contarlos como tres confirmaciones independientes.

**Evidencia de 1993:** Recordsale identifica edición alemana CSC 7060 [D06]; Musik-Sammler registra esa edición con matriz OPTIMAL GERMANY CSC7060 [B]1 [D12]. Burning Shed describe su reedición de 2018 como álbum de 1993 [D11]; el resultado indexado está disponible, la apertura completa devolvió 403.

**Conclusión calibrada:** la edición más temprana localizada está catalogada en 1992 y tiene identificadores concretos. Eso justifica mantener provisionalmente el año de NV, pero **no certifica primera venta mundial ni fecha exacta**. Falta escaneo legible de libreto/disco de DINCD 18 y prueba contemporánea de lanzamiento. La existencia de una edición 1993 no desmiente por sí sola 1992; una fecha ℗ tampoco prueba por sí sola el día de publicación.

La cubierta observada se corresponde visualmente con CSC 7060, pero comparte motivos y no revela necesariamente edición. Registrar por separado `año_album_provisional=1992`, `edición_imagen_por_confirmar`, `edición_alemana_documentada=1993`. Esta es una recomendación de investigación, no un cambio ejecutado en la base.

**Créditos:** fuentes de edición atribuyen bajo/voces a O’Ryan y teclados/sampling a Leif; una reseña atribuye bajo a Leif y enumera pistas de Brian May de manera distinta [D13]. Rechazar ese detalle controvertido para el guion. Mantener Scott y Brian como guitarristas acreditados, sin distribución por pista. «Keith Murell» es una grafía de catálogos; se conserva como variante de Keith Murrell, pendiente de libreto al normalizar. No crear nuevos IDs ni editar alias en F0.

## Decisiones

| Estado | Decisión |
|---|---|
| Aprobado por encargo | Cinco discos cerrados; solo F0; original completo reconocible; scroll reversible; no modificar NV |
| Aprobado por encargo | Barlow, negro/hueso, lila de guitarra para interfaz; no imponer Xerox sobre masters |
| Propuesta Work | Ruta B como dirección principal; T34-a como PoC; T45-a como control creativo temprano |
| Propuesta Work | Usar 2.5D y máscaras primero; 3D localizado solo si su aporte está demostrado |
| Pendiente G1 | Elegir A/B/C; única decisión creativa solicitada al cierre |
| Pendiente fases futuras | Masters, permisos, edición exacta, storyboard, presupuestos de peso finales, validación móvil |
| No autorizado ahora | Generar imágenes, construir escenarios, programar PoC, publicar o integrar |

## Coste y esfuerzo: qué sí puede afirmarse

GSAP anuncia gratuidad en su página de precios [T03]; Three.js dispone de licencia MIT [T04]. Para el prototipo no se identifica necesidad de una suscripción de software. Esto no significa producción gratis: máscaras, fondos ocultos, intermedios, revisión y posible autorización de arte son trabajo/costes separados. No se han solicitado tarifas ni comprado recursos. No es posible dar un coste inevitable de derechos sin consultar a sus titulares.

Orden relativo de esfuerzo propuesto: A exige más ilustración de costuras; B más control de transformación; C más reconstrucción espacial y optimización. En las tres rutas hay cinco escenarios y cuatro puentes, pero no se presupuesta un “prompt por escenario”. La calidad depende de iteraciones específicas, especialmente T12 y T45.

## Glosario para decisiones creativas

| Término | Explicación simple | Decisión que afecta |
|---|---|---|
| Master | Copia de referencia fiable que no se altera | Qué versión de cada portada es la verdad documental |
| Fullscreen / viewport | Toda el área visible del navegador | El paisaje llena pantalla; el frontal puede conservar márgenes |
| 2.5D | Planos recortados a diferentes distancias que parecen tener profundidad | Cuánto puede moverse la cámara antes de mostrar huecos |
| 3D | Objetos con volumen y vistas laterales | Solo conviene si hace falta ver alrededor de algo y se puede producir esa información |
| Parallax | Un plano cercano se mueve más que uno lejano | Sensación de distancia, con riesgo de mareo y cantos visibles |
| Cámara | Punto de vista y encuadre virtuales | Dónde miras y cómo cambia la escala |
| Zoom | Cambiar el tamaño aparente desde un encuadre | Acercarse no demuestra por sí solo profundidad |
| Travelling | Desplazar el punto de vista por el espacio | Permite pasar junto a tela, roca o guitarra |
| Compositing | Combinar capas en una sola imagen coherente | Unir luz, suelo, humo y fondo sin costuras |
| Máscara | Recorte que deja ver una parte de una capa | Transformar solo rayo/humo sin tocar títulos |
| Textura | Imagen o patrón que da materia a una superficie | Conservar tinta, fibra, piedra o papel |
| Match cut / empalme por correspondencia | Enlazar dos imágenes porque comparten posición, forma o dirección | Motivo claro para pasar entre discos |
| Oclusión | Algo cercano tapa algo que está detrás | Ocultar una costura con la propia tela, sin flash artificial |
| Morph / metamorfosis | Cambio gradual de forma entre dos estados | Núcleo de B; puede parecer gelatina si faltan intermedios |
| Shader | Instrucción que calcula apariencia o deformación de píxeles/superficies | Solo se usa si mejora un puente concreto, no como efecto gratuito |
| WebGL | Tecnología de navegador para dibujar con GPU | Habilita escenas complejas, también añade consumo y fallos posibles |
| Scrub | La posición del scroll controla el avance de la animación | Detener y volver exactamente al mismo estado |
| Keyframe / fotograma clave | Estado visual importante que guía el recorrido | Aprobar la imagen intermedia antes de programar |
| Extensión / outpainting | Crear imagen fuera de los bordes existentes | Es interpretación nueva, no recuperación documental |
| Registro | Alinear posición, tamaño y perspectiva de capas | Volver del mundo expandido al frontal sin salto |
| Movimiento reducido | Recorrido alternativo sin desplazamientos visuales forzados | Mismos contenidos con otra presentación |
| PoC | Prueba pequeña para resolver una incertidumbre | Una unión completa antes de construir las cuatro |

## Criterio editorial final

Separar siempre cinco etiquetas: hecho respaldado, observación visual, interpretación artística, decisión aprobada y prueba pendiente. Que dos discos tengan el mismo músico es un hecho; que una descarga se convierta en un signo es una interpretación; que esa transición funcione en móvil será un resultado solo cuando se pruebe.
