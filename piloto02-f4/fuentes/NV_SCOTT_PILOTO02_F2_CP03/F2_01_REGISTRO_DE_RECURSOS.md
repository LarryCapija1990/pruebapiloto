# Recursos requeridos y estado real

F2 CP03 v1.0. Todos los recursos de producción siguientes están **pendientes**. «Referencia disponible» significa muestra pequeña investigada, sin asumir licencia. No existe todavía ninguno de los PNG indicados.

## Fuentes de partida

| Mundo / ID | Evidencia disponible en F0 | Master buscado | Incidencia antes de producir |
|---|---|---|---|
| C01 Chinatown | Frontal oficial 300×300; reproducción de autor 688×1000 que incluye frontal y reverso | Frontal completo, preferible 2000–3000 px de lado, perfil de color conocido | No confundir altura total de reproducción con resolución del frontal; arte Jim FitzPatrick. |
| C02 Renegade | Frontal oficial 300×300; captura NV con distinta dominante | Frontal completo de edición identificada | Resolver azul/verde mediante fuente de referencia; no inventar montaña en masa oscura. |
| C03 Thunder | Oficial 300×298; archivo 120×121 | Frontal de buena calidad, sin deformar relación de aspecto | Resolver distintivo de captura NV; conservar guitarra y terreno pedregoso. |
| C04 Innervision | Imagen comercial 430×426 | Frontal con edición y condiciones de uso identificadas | DINCD 18 catalogado 1992 frente a CSC 7060 de 1993; no certificar primera edición. |
| C05 Salute | AllMusic 400×388; muestra 200×200 | Frontal y detalle permitido de mano/cartas | Resolver recorte desde fuente; no escalar ni inventar índices de naipes. |

Procedencia y enlaces: F0/02_FICHAS_VISUALES_DE_PORTADAS.md e I01–I06 de F0/09_MANIFIESTO_FUENTES.csv. No sustituir estas muestras por el primer resultado de un buscador sin volver a identificar su edición.

## Familias de archivos por mundo

Convención: `NV_A_C03_BG_D_v001.png`, donde A es ruta, C03 mundo, BG tipo, D escritorio, M móvil, v001 versión. Omitir D/M para master. Mantener versiones anteriores y documentar cuál se aprueba. Los originales conservan además su nombre y formato recibidos; cualquier alias de trabajo apunta a esa copia, no la sobrescribe.

| Código | Entrega real esperada | Función / dependencia |
|---|---|---|
| MASTER | Copia original intacta en formato recibido | Documento de referencia. Registrar ancho/alto, origen, edición y permiso. |
| BG | Fondo expandido limpio, sin motivo delantero | Relleno detrás de capas; depende de master y encuadre aprobado. |
| MID | Plano medio recortado con alfa | Motivo reconocible: dragón, bandera, guitarra, signo o mano/cartas. |
| FG | Primer plano con alfa, solo si hace falta | Curva, borde de tela o piedras; prescindible si añade riesgo. |
| MASK_* | Máscara monocroma del motivo indicado | Blanco conserva, negro excluye; gris solo en borde necesario. |
| EXP | Composición expandida plana de control | Resultado ensamblado y verificable; no sustituye BG/MID/FG. |
| ENTRY / EXIT | Encuadres de llegada y salida | Deben compartir registro con la unión anterior/siguiente. |
| GUIDE | Documento con coordenadas y correspondencias | Centro, escala, recorte, huella del master y área inventada. |
| KF_p000…p100 | Seis fotogramas de revisión por transición | No son una animación ni prueba de scroll. |

## Capas mínimas específicas

| Mundo | Fondo | Plano medio | Primer plano / máscara | Lo que no se reconstruye libremente |
|---|---|---|---|---|
| C01 | Campo ornamental extendido | Dragón y ornamento principal | Curva próxima; máscara de paso T12 | Anatomía completa por detrás, ciudad o templos. |
| C02 | Cielo limpio y extendido | Bandera/asta/masa oscura agrupadas | Borde de tela; máscara T23 | Cara posterior, cordillera o estatua inferida. |
| C03 | Cielo y terreno prolongados | Guitarra y terreno central | Piedras cercanas; máscara T34 | Componentes nuevos de guitarra o mar. |
| C04 | Campo oscuro extendido | Signo fiel en plano | Puntos escasos; máscara T45 | Pirámide, nave, símbolo modificado. |
| C05 | Fondo interior y superficie exterior | Mano y cartas como grupo rígido | Humo opcional separado | Otra mano, mesa, habitación o nuevos naipes. |

Prioridad: P0 masters C03/C04; P1 sus extensiones, inserto T34 y capas; P2 composiciones de resto, con revisión temprana de T45; P3 detalles atmosféricos opcionales. No producir textura o partículas si la composición plana ya funciona.

## Paquete por transición

Para T12/T23/T34/T45 se requiere: `INSERT` (detalle derivado del destino aprobado), `APERTURE_MASK` (contorno del origen), `REGISTER` (guía de alineación) y seis keyframes por orientación. El inserto nunca se genera como una segunda versión independiente del destino. Mantener carpeta fuente y receta de recorte para poder reconstruirlo.

Cada estado debe registrar: archivo fuente y versión, rectángulo de recorte, escala, posición, oclusión, perfil de color y capa que pasa delante. Un CSV o tabla futura de registro será producto de la composición, no coordenadas fingidas antes de contar con imágenes.

## Disponibilidad y derechos

Las referencias F0 están disponibles como documentación enlazada. Masters, máscaras, extensiones y permisos siguen pendientes. Revisar autorización de uso y transformación con quien aporte los materiales; poseer una copia del disco o encontrar una imagen en línea no documenta por sí mismo permiso para distribuir derivados. No se han contactado titulares, comprado archivos ni solicitado licencias.
