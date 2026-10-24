# Guía del montaje y revisión honesta

## Seis estados entregados

| Progreso | Estado | Fuente |
|---|---|---|
| 0 % | Thunder completo con todos sus textos | JPG original ajustado dentro de viewport. |
| 20 % | Entrada al escenario con guitarra visible | Composición Thunder e inserto registrado. |
| 40 % | Acercamiento al impacto, destino legible dentro | Mismos archivos, distinto encuadre. |
| 60 % | Innervision ocupa gran parte de vista; periferia conserva Thunder | Destino renderizado directamente al tamaño de salida. |
| 80 % | Innervision expandido, después de atravesar apertura | Composición de destino completa. |
| 100 % | Portada completa de Innervision | JPG original ajustado dentro de viewport. |

Se conserva además un control 50 % y uno 70 %. Son imágenes de inspección, no frames de una animación temporal. No se entrega vídeo para evitar sugerir que existe una trayectoria continua ya validada.

Coordenadas reales del primer registro: inserto en (405,190)–(555,275) del lienzo 1066×600. Su relación de aspecto es prácticamente igual a la del destino; el redondeo 150×85 se documenta. La cámara se centra progresivamente en ese área. El mapa real sustituye solo los valores tentativos de composición del guion, no su principio creativo.

## Reversión

La lámina de vuelta reutiliza exactamente los mismos archivos en orden inverso. Por ello no hay variación aleatoria de estrellas o letras entre las vistas compartidas. Eso prueba identidad de estados estáticos, **no prueba funcionamiento de scroll ni ausencia de saltos entre ellos**. La prueba 60→30 requiere una interpolación futura; no se declara ejecutada.

## Mediciones realizadas

QA_MEDICIONES.json registra tamaño fuente, posición del original en el lienzo, cantidad de píxeles comparados y error de reensamblado. La región auditada excluye las bandas de mezcla lateral de 32 px y las regiones intervenidas para retirar texto. No se extiende la afirmación de identidad a toda la imagen expandida.

Los originales se auditan mediante SHA256 en MANIFIESTO_ARCHIVOS.json. PNG verificados por decodificación y presencia de alfa en recortes. La cifra de resolución del lienzo no implica aumento del detalle original.

## Observación visual y prioridad de corrección

1. **Alta:** diferencias entre arte central original y laterales sintéticos en Thunder, especialmente cielo derecho y masas de roca. Corregir localmente con edición, sin regenerar la guitarra.
2. **Alta:** áreas suavizadas donde se quitó tipografía en Innervision. El trazo principal se conserva, pero las zonas recuperadas necesitan textura coherente.
3. **Media:** apertura ovalada aún demasiado regular. Diseñar oclusión que nazca de la zona de impacto y mantenga visible el motivo del destino.
4. **Media:** el paso 70→80 implica retirada dentro del destino; necesita suficientes estados intermedios para comprobar ritmo y ausencia de salto.
5. **Pendiente:** móvil, movimiento reducido y recursos adaptativos. No derivar móvil mediante recorte automático de estas láminas.

**Dictamen:** útil para revisar la hipótesis de anidamiento y la conservación documental; no aprobado para implementación final. F3 sigue abierto. No recomendar otra generación completa de las portadas para solucionar los defectos localizados.
