# Procedimiento de edición y aceptación de assets

F2 CP03 v1.0 · Procedimiento para F3. No se ha ejecutado.

## Recepción

Registrar archivo recibido, dimensiones reales, formato, perfil, fuente, edición atribuida, fecha y condiciones de uso conocidas. Crear copia de trabajo y conservar el original sin cambios. Calcular huella del archivo cuando se archive; no escribir una huella inventada en el registro. Resolver recortes y relación de aspecto con evidencia, sin estirar automáticamente a cuadrado.

## Segmentación manual o asistida

1. Duplicar master en documento de trabajo; nombrar capa documental y bloquearla.
2. Dibujar máscara sobre motivo visible usando selección y corrección manual; proteger letras, bordes de instrumento, mano y naipes.
3. Exportar recorte con alfa real. Inspeccionarlo sobre blanco, negro y gris para detectar halos; no aceptar damero pintado.
4. Reconstruir fondo detrás solo hasta cubrir el desplazamiento previsto. Registrar las áreas nuevas en guía separada.
5. Mantener todos los planos en el mismo lienzo; el ensamblado debe reproducir EXP. Evitar exportaciones recortadas a contenido que pierdan el origen de coordenadas.
6. Integrar INSERT desde el destino aprobado; aplicar APERTURE_MASK del origen y oclusor delantero cuando corresponda.
7. Guardar documento editable con capas reales si el editor lo permite y exportar PNG individuales. Abrir ambos para confirmar; no entregar una imagen aplanada renombrada como multicapa.

Si una separación no es fiable, conservar los motivos agrupados. Una escena plana bien registrada es preferible a capas que revelan huecos o cantos.

## Hoja de control por archivo

Cada revisión debe anotar: nombre/versión, fuente y versión utilizada, función, dimensiones, orientación, estado (borrador/revisar/aprobado/rechazado), cambios realizados, zonas inventadas, motivo de rechazo y siguiente acción. La aprobación de un EXP no aprueba automáticamente sus máscaras ni la variante móvil.

## Pruebas de coincidencia

| Prueba | Qué mirar | Condición de rechazo |
|---|---|---|
| Superposición master | Contornos y proporciones en región preservada | Desvío visible de símbolo, instrumento, emblema, letras o anatomía. |
| Reensamblado de capas | Comparar con EXP aprobado | Diferencias de posición, recorte, color o alfa sin documentar. |
| Registro del inserto | Tres puntos compartidos entre recorte y emergencia | Cambian de posición relativa o dibujo durante el cruce. |
| Ampliación máxima | Ver a tamaño de salida previsto | Pixelación que impida lectura o detalles ficticios presentados como originales. |
| Estado intermedio 50 % | Observar borde y destino simultáneamente | Pantalla blanca/negra o fundido que oculte discontinuidad. |
| Secuencia inversa | Revisar 100→80→60→40→20→0 | Destino cambia de versión, humo avanza solo o bordes no regresan igual. |
| Vertical | Repetir revisión con composición móvil | Motivo fuera de campo o tapado por texto/controles. |

En lo conservado documentalmente no se acepta «parecido suficiente». En las extensiones se evalúan coherencia, legibilidad y continuidad; se reconoce que son creación artística.

## Paquete mínimo antes de F4

Para cada uno de los dos escenarios de la primera prueba: imagen_original, composición_expandida, máscaras/capas realmente necesarias, guía_de_cámara y fotogramas_de_entrada/salida. Además, INSERT_T34 y su máscara, seis keyframes de transición por orientación, archivo de procedencia y revisión de uso. Si falta una familia, registrar qué impide probar; no avanzar anunciando un recorrido completo.

## Criterios de detener o simplificar

- Sin master suficiente: detener la producción de ese mundo y pedir fuente; puede continuarse planificación de los otros.
- Sin permiso resuelto: no distribuir derivados; mantener el trabajo documental.
- Inserto requiere macro imposible: agrandar la abertura y acortar recorrido.
- Paralaje revela superficies falsas: aplanar o agrupar capas y limitar cámara.
- T45 parece una tarjeta: revisar composición; no cambiar silenciosamente a B.
- Herramienta altera letras o símbolos: volver a composición manual desde original.

No medir ni afirmar FPS con imágenes estáticas. Las pruebas de scroll real, dispositivos y rendimiento pertenecen a F4. No optimizar formatos hasta destruir detalle necesario antes de comprobar el recorrido.
