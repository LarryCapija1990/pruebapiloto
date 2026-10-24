# Recursos y contrato para la futura implementación

Este documento no implementa una web. Los porcentajes son posiciones de recorrido, no segundos ni una grabación.

## Espacio de trabajo

Todos los PNG principales utilizan lienzo 1066×600, esquina superior izquierda como origen y la misma posición de cada estrella. Los JPG originales miden 600×593 y 600×594; no se afirma que el lienzo mayor cree detalle auténtico. Los extremos de revelación ajustan esas imágenes completas dentro de la pantalla y conservan textos, proporción y esquinas.

## Pila por estado

Orden de abajo a arriba:

1. `estados/pXXX_FONDO_RGB.png`: cielo/terreno ya compuesto con máscara espacial de ese progreso.
2. `estados/pXXX_ESTRELLAS_RGBA.png`: estrellas independientes, sin placa de fondo.
3. `estados/pXXX_RAYO_EJE_RGBA.png`: evolución interpretativa de la descarga hacia línea vertical cálida.
4. `estados/pXXX_SIGNO_RGBA.png`: porciones del signo procedentes de la escena de Innervision.

En p010 se añade el rayo original entre fondo y estrellas; el registro JSON lo indica. En p000 y p100 se utilizan directamente los fotogramas documentales. Cada capa tiene alfa real; los píxeles completamente transparentes tienen RGB cero para evitar contaminación de bordes.

Los fondos compuestos por estado se entregan para reproducir exactamente la revisión. No son una recomendación de cargar nueve fondos grandes en producción. Para una solución paramétrica futura se dispone de `C03_SIN_RAYO_RGB`, `ESPACIO_BASE_RGB`, `CAMPO_APARICION_ESPACIO`, máscaras y capas fuente. Optimizar sin cambiar el resultado deberá verificarse en F4.

## Progresión propuesta

| Tramo | Fondo | Luz y estrellas |
|---|---|---|
| 0–10 % | Del frontal completo al escenario Thunder | Descarga original reconocible. |
| 10–30 % | Las zonas oscuras empiezan a adquirir profundidad espacial | Primeras estrellas; línea aún fría. |
| 30–50 % | Cielo oscuro se convierte antes que nube iluminada y terreno | Estrellas más visibles; la línea reduce su irregularidad y se calienta. |
| 50–70 % | Ascenso del encuadre y retirada progresiva del suelo | Eje se aproxima a la vertical; arco emerge sin ventana. |
| 70–90 % | Predomina el campo espacial | Signo original toma el relevo de la línea interpretativa. |
| 90–100 % | Reencuadre hacia portada completa | Revelación documental de Innervision con sus textos. |

El campo de máscara utiliza luminancia, altura y variación suave: cielo oscuro primero, zonas iluminadas después y suelo al final. El archivo `CAMPO_APARICION_ESPACIO.png` es un mapa de umbral, no una imagen para mostrar. Negro significa aparición más temprana; blanco, más tardía. Aplicar una rampa suave alrededor del umbral, no un corte duro.

El suelo se desplaza hacia abajo hasta 280 px en el tramo intermedio. Los píxeles superiores que quedan libres se cubren con campo oscuro; no estirar una fila de nubes y crear columnas. Las estrellas no cambian de identidad de un estado a otro.

La línea rayo→eje se construye mediante correspondencia entre puntos de un trazo irregular y una vertical, con color frío→cálido. Es arte de transición, no una restauración del rayo original. La porción del signo se incorpora por una máscara que distingue eje y arco; el arco aparece gradualmente desde su zona inferior hacia los extremos. No se deforma el master de Innervision.

## Reversibilidad que deberá implementarse

Todo estado depende del mismo progreso absoluto. Al detenerse el scroll no deben continuar estrellas, luz o terreno. Al regresar a una posición se deben recuperar las mismas máscaras, posiciones y color, sin ruido nuevo ni acumulación de efectos. La semilla fija del campo de transición ya está incorporada en la máscara exportada.

No usar estos PNG como prueba de que la interpolación funciona. Un fundido entre cada par de fotogramas completos tampoco reproduce necesariamente el mecanismo descrito. Probar por separado el control de cámara, campo del cielo, visibilidad estelar y geometría de luz.

## Pendientes técnicos y visuales

Los empalmes entre frontal y escena, y la retirada final hacia la cubierta documental, no tienen todavía interpolación validada. No se ha construido móvil ni ensayado un dispositivo. Las imágenes de baja resolución limitan acercamientos extremos. No añadir efectos, bloom ni flashes para disimular estas limitaciones.
