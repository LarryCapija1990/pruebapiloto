# Integración con F4 inspeccionada

Base incluida sin alterar: F4 CP03 v1.2 LOCAL. Se inspeccionó su código, no se ejecutó su animación en esta entrega.

Observado: canvas WebGL, uP local, render programado con requestAnimationFrame, texturas incrustadas, geometría de línea ligada a progreso. Espacio común 1066×600. Huella original Innervision: esquina (233,3), tamaño (600,594). Centro de composición (533,300). Al cierre el shader usa contain fit=min((W−40)/600,max(100,H−(H<500?120:220))/594), centro de pantalla (W/2,H/2−(H<500?0:12)). Son coordenadas de su dominio interno: comprobar consistencia entre DPR y unidades CSS al extenderlo. El módulo T45 debe tomar exactamente la matriz y fotograma final, no recrearlos con otra regla CSS.

No reutilizar uP global para comprimir T34 y T45 en su antigua duración. Mantener progreso local y longitud original T34; añadir el segundo segmento. No editar el shader T34 para que dibuje Salute. Compartir infraestructura solo si las capturas T34 siguen iguales en el mismo viewport/progreso.

Recursos_F4 contiene space.png, stars.png, symbol.png y el original embebido, extraídos sin recodificar. Validar diferencias entre original embebido y original documental incluido antes del empalme: usar el embebido para continuidad F4 y el documental como referencia si difieren. No tratar toda expansión F4 como imagen original.

Salute se usa como plano único. No separar mano, naipes ni humo en planos con parallax independiente: no hay información real de reversos u oclusiones. La profundidad viene del acercamiento, escala y transformación, no de anatomía nueva.

Recursos nuevos de geometría: SVG vectoriales y JSON de poses manuales. No código de animación. Son guías ajustables. Llegada exacta y detalles pertenecen siempre a salute.jpg; registrar el contorno a ese raster a escala de uso.

Objetivo inicial de rendimiento: conservar límite de DPR existente y render bajo demanda. Precargar recursos antes del segmento, no descargar durante el morph. No usar video ni secuencia de cientos de bitmaps para resolver la forma. Las cifras de rendimiento deben medirse en Codex, no están certificadas aquí.
