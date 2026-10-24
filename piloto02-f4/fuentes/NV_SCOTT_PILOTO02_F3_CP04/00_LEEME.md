# F3 CP04 · Primer montaje visual real de T34-A

23-10-2026 · Ruta A, mundos anidados. G1/G2 aprobados; **checkpoint de producción en revisión, no cierre de F3 ni autorización de F4**.

## Qué abrir primero

1. `revision/T34_SECUENCIA_IDA.jpg`: seis fotogramas de Thunder completo a Innervision completo.
2. `revision/T34_SECUENCIA_VUELTA.jpg`: mismos estados en orden inverso.
3. `fotogramas/`: seis PNG sin rótulos editoriales para inspección individual.
4. `C03_Thunder/` y `C04_Innervision/`: composiciones, capas PNG reales y máscaras.

## Qué se hizo

Se utilizaron los JPG aportados por Sebastián como fuente del núcleo documental. Los escenarios generados previamente aportan los laterales interpretativos. Se conservaron los motivos originales por composición determinista, en vez de volver a generarlos. Las copias originales permanecen sin modificación en `originales/`.

Las letras se retiraron **solo de las copias escénicas**, mediante interpolación local y protección del trazo cálido de Innervision. Las máscaras de texto identifican dónde hubo intervención. No se afirma haber recuperado el arte escondido detrás de esas letras.

Se produjeron un fondo reconstruido, una capa de contexto y una capa de motivo por mundo. Los PNG contienen alfa real y se reensamblan exactamente al encuadre expandido. No se entrega un PSD ficticio ni se anuncia profundidad 3D.

El destino se inserta en un área próxima al impacto de Thunder. La vista cercana utiliza directamente la composición de Innervision a su resolución disponible, evitando ampliar solo una miniatura ya incrustada. Los frames son montajes estáticos con encuadres registrados; **no son capturas de una web ni prueba de animación**.

## Resultado de revisión

- Se conservan los píxeles del núcleo original fuera de las regiones de texto intervenidas y las bandas laterales de mezcla. Ver cifras en QA_MEDICIONES.json.
- Reensamblado de capas: error máximo por canal 0 en ambos mundos.
- Los originales del paquete coinciden byte a byte con los aportados.
- Hay seis estados 0/20/40/60/80/100 %, más controles 50/70 %.
- El destino es reconocible antes del cruce y los extremos muestran las cubiertas completas.

## Lo que aún no está resuelto

Las reparaciones donde había texto tienen menos textura y pueden leerse como zonas suavizadas. Los laterales generados no encajan perfectamente con todas las rocas y nubes del núcleo de Thunder. El borde del inserto es una máscara de trabajo ovalada y suavizada: aún debe integrarse mejor en la forma de la descarga. **No se aprueba por ello como acabado final.**

La fuente mide 600 px de ancho. El lienzo de 1066×600 sirve para esta prueba de composición; un zoom no añade detalle auténtico. Los fondos ocultos son reconstrucciones aproximadas y no habilitan giros o desplazamientos amplios. No se ha producido una composición móvil ni probado scroll, interpolación continua, accesibilidad o rendimiento.

## Próximo trabajo recomendado

Refinar la continuidad de nube/roca en los empalmes laterales y texturizar las reparaciones de letras mediante edición controlada. Sustituir la máscara ovalada por un borde propio del detalle de impacto, conservando el registro del destino. Después revisar una composición vertical. Solo con esas revisiones y aceptación visual corresponde preparar la PoC.

Este paquete es un avance tangible y revisable, no otra promesa de assets. Conserva F0–F2 sin cambios dentro del ZIP acumulativo. Nero’s Vice permanece intacto.
