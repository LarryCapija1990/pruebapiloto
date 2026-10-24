# F4 CP01 · Contrato antes de implementar

Fuente vigente: F3 CP05; CP04 se usa exclusivamente para los dos JPG originales. No se integra Nero’s Vice ni ningún otro álbum. Los documentos históricos describen otros trabajos: no amplían el encargo actual.

## Interpolación elegida

El fondo se calcula desde C03_SIN_RAYO_RGB y ESPACIO_BASE_RGB mediante una rampa suave sobre CAMPO_APARICION_ESPACIO. CIELO_OSCURO_INICIAL modula la aparición temprana de estrellas. Las estrellas mantienen su identidad y coordenadas; no hay ruido animado. El desplazamiento del terreno es 280·smoothstep(0.30,0.80,p), que reproduce los nueve desplazamientos de ESTADOS_Y_CAPAS.json.

El trazo intermedio se implementa con correspondencias de 16 puntos por geometría. Se extraen los centroides de alfa por fila de las capas RAYO_EJE de CP05 entre 20–80 % y se interpolan sus puntos mediante Catmull–Rom; no se mezclan sus imágenes. Se pasa de una polilínea irregular a la vertical cálida en x≈524. No pretende restaurar ni vectorizar exactamente el rayo histórico. El original RGBA toma y entrega el relevo. El signo master conserva su geometría; se revela el eje y el arco con máscaras distintas, el arco desde abajo hacia sus extremos. El eje master entra después del 65 % para evitar una doble línea durante su alineación.

## Limitaciones conocidas antes de sustituir o completar un efecto

CP05 no proporciona una función original de generación de máscaras ni los puntos de la polilínea. No se puede afirmar igualdad píxel a píxel con los estados estáticos a partir de los recursos paramétricos. Se reconstruye la rampa documentada: al deshacer el desplazamiento de los estados, el umbral observado es aproximadamente p−0.115, con rampa suave ±0.13. Se derivan los puntos de las capas de luz entregadas. El primer empalme desde el rayo original usa una polilínea propia; en los demás estados se deriva de sus alfas. Esto mantiene el mecanismo sin interpolar los once fotogramas. Se conservarán los estados en fuentes para revisión.

Los enlaces 0–10 y 90–100 no tienen interpolación validada en CP05. F4 propone una cámara común entre imagen original y escenario registrado (original a x=233,y=3, tamaño nativo). La escala cambia uniformemente, sin deformación. Dentro de la huella registrada se restituyen gradualmente los píxeles documentales, incluidos textos, y fuera se retiran las extensiones. Este empalme localizado de capas es una propuesta pendiente de revisión; no es un fundido global entre dos portadas. El borde del original es visible en los extremos documentales por definición.

En móvil se recorta horizontalmente el escenario intermedio para ocupar pantalla; los originales se contienen completos en ambos extremos. No se inventan extensiones verticales. Con movimiento reducido se fija la cámara, se elimina el ascenso, se omite el trazo geométrico intermedio y se contiene el escenario: máscaras y controles siguen funcionando. El rayo original se retira y el signo se revela en sus posiciones fijas. Se evita toda animación temporal, incluida la interpolación inercial del scroll.

La resolución fuente limita el detalle; las reparaciones bajo el rayo y la tipografía pueden ser visibles. No se añaden flashes, bloom, partículas nuevas ni efectos para ocultarlas. El nivel de fidelidad y la calidad cinematográfica requieren revisión humana en funcionamiento.

## Ajustes comprobados durante F4

- Se contrastaron las máscaras de estado después de deshacer el desplazamiento del terreno; esto corrigió una conversión demasiado temprana del suelo entre 50–70 %.
- El trazo se deriva de los centroides de las capas CP05 en lugar de aproximar únicamente sus extremos. Se rasteriza vectorialmente en una capa transparente 1066×600 por cambio de progreso; no se calcula la distancia a cada segmento en cada píxel de pantalla. La composición conserva ocho samplers WebGL1, empaquetando los originales en un atlas a tamaño nativo.
- El rayo original comienza a entregar el relevo en el 10 %, al concluir la apertura, para evitar una pausa no intencionada hasta el 12 %.
- La restitución de las marcas del perímetro escaneado se retrasa al cierre de la retirada, evitando una línea rectangular blanca temprana durante 90–100 %.
- La medición de diferencias entre capturas usa remuestreo de alta calidad explícito. El filtrado bilineal por defecto al reducir a 320×180 generaba alias del grano y exageraba la métrica; se contrastó con Pillow antes de corregir el instrumento de prueba. No se relajaron los umbrales de continuidad.

Estos ajustes completan una propuesta F4; no convierten los estados CP05 en una certificación de fidelidad cinematográfica.
