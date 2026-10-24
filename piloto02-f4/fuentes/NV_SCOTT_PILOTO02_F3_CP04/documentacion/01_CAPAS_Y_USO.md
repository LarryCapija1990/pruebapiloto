# Cómo usar las capas entregadas

Todas las capas D utilizan lienzo 1066×600, origen (0,0), sRGB operativo RGB de 8 bits. No se asigna autenticidad colorimétrica a fuentes sin perfil verificado. Los masters conservan sus bytes y metadatos recibidos.

Orden de abajo a arriba, sin desplazar:

1. `C03_BG_D.png` o `C04_BG_D.png`: fondo con relleno bajo motivo.
2. `*_MID_CONTEXTO_D.png`: anillo de contexto que restituye el contorno del área reparada; alfa real.
3. `*_MOTIVO_D.png`: recorte del motivo con alfa real.

El resultado coincide con `*_EXP_D_v003.png` y con `*_REENSAMBLADO_D.png`. Las máscaras MOTIVO son L monocromas: blanco conserva. La máscara TEXTO indica intervención en la copia escénica; no es un recorte de letras para animarlas.

La separación del motivo usa un contorno amplio, no un recorte editorial perfecto de cada pelo/clavija. En Thunder se agrupa el conjunto de pala y mano del primer plano para no inventar anatomía. En Innervision se agrupa el trazo cálido y su entorno inmediato. El relleno bajo estos grupos es aproximado: no aprobar paralaje por el hecho de contar con capas.

## Inserto T34

`T34_INSERT_RGBA_D.png` contiene una copia reducida del destino y alfa de apertura, ya posicionada en el lienzo de Thunder. `T34_APERTURE_MASK_D.png` indica su área. Sobreponer INSERT al EXP de Thunder reproduce `T34_ANIDADO_D_v001.png` salvo redondeos de la operación alfa.

`T34_DESTINO_REGISTRADO_D.png` es el destino completo que debe usarse para planos cercanos; no ampliar únicamente el PNG pequeño del inserto. La transformación está registrada en REGISTRO_GEOMETRIA.json. No cambiar Innervision por otra versión después de preparar el inserto.

La máscara ovalada es provisional. No forma parte de la portada histórica ni constituye la decisión de fabricar cuatro portales iguales. Su función en este checkpoint es permitir evaluar tamaño y legibilidad. Falta un contorno adaptado a la descarga.

## Extremos documentales

Los frames 0 y 100 ajustan los JPG originales completos sobre margen oscuro. Se preserva su relación de aspecto; no se recrean sus títulos. La apertura hacia escena y la retirada hacia el frontal siguen pendientes de interpolación y evaluación continua en F4; estos seis encuadres no prueban por sí mismos esa continuidad.
