# Diagnóstico de transporte · 27 de octubre de 2026

## Error original y alcance real del diagnóstico

El usuario informa de `decoded message length too large: found 4554464 bytes, limit 4194304` **al abrir el chat o la vista previa**. Se conservan ambos valores literalmente. No se ha repetido esa apertura fallida ni se ha enviado un payload de ese tamaño para reproducirla.

Las herramientas sí se ejecutan en este turno. No hay una traza del cliente que identifique el nombre de la llamada, su dirección, identificador o contenido exacto. Se buscaron los términos del error en 26 logs/JSONL accesibles de trabajo/temporales: sin coincidencias. Se revisaron además 90 informes JSON originales, excluyendo este diagnóstico: tampoco contienen esa excepción. No hay logs de sesión expuestos en las ubicaciones de Codex accesibles. **La llamada interna que produjo los 4.554.464 bytes sigue sin identificar.** No se atribuye el fallo al código de la animación ni se da por reparado el visor del chat. El código que emite esa excepción tampoco está expuesto aquí.

## Llamadas grandes encontradas en la inspección estática

En `t45-cp13/implementacion/probar_cp13.py`, las líneas 27 y 28 llaman a `Page.set_content(html)` y `Page.set_content(old)`. Intentan transportar documentos completos a través de la conexión de automatización. Se inspeccionaron sus tamaños sin ejecutarlas de nuevo:

|Contenido|Bytes UTF-8 del documento|Bytes como valor JSON, ensure_ascii=False|
|---|---:|---:|
|CP13 HTML completo|7.176.301|7.178.386|
|Referencia CP12|7.175.040|7.177.107|
|F4 HTML embebido|4.330.403|4.331.444|

Son mayores que 4.194.304, pero **ninguno coincide con 4.554.464**. Son cargas grandes confirmadas por tamaño, no una identificación causal de la excepción del cliente. Pertenecen al canal Playwright Python–Node; `exec_command` solo envía el comando de shell y no ese HTML. Las pruebas históricas terminaron sin esa excepción: no se presupone que el límite del cliente sea el mismo que el de Playwright. Las llamadas originales y los archivos aceptados se mantienen sin modificar. No se usa `set_content` en la prueba alternativa.

También hay una llamada de pruebas `Page.evaluate(canvas.toDataURL().split(...))` que devuelve un PNG como base64. Su tamaño depende del viewport y del estado. No se la ha repetido con salida de imagen ni se la declara responsable del tamaño denunciado. La alternativa calcula el hash del PNG dentro del navegador y solo devuelve metadatos.

## División/externalización realizada

Se genera `CP13_VISTA_HTTP/`, una copia independiente para servir por HTTP local:

- `index.html`: 18.623 bytes, frente a 7.176.301 originales.
- `f4/index.html`: 32.069 bytes, frente a 4.330.403 originales.
- Diez imágenes/recursos binarios únicos separados; el mayor mide 1.246.683 bytes. Todos conservan los bytes y SHA256 del recurso decodificado original. No se cambia tamaño, formato, calidad, color ni resolución.
- El cambio de montaje es cargar la página de F4 por URL relativa en lugar de introducir su texto completo en `iframe.srcdoc`. Se añade un aviso si se abre esta variante como file://, evitando acceso entre archivos de origen opaco. No se cambia el render, las funciones de cámara o el mapa de scroll.

La prueba usa **`Page.goto(URL_local_corta)`**. El navegador descarga los archivos desde el servidor local; esos cuerpos no se empaquetan como argumento de una llamada de herramienta. Para comparar, el PNG se crea y se resume con SHA256 dentro de la página: Python recibe tamaño, dimensiones y 64 caracteres de hash, sin base64 ni captura completa.

## Reintento medido

`PRUEBA_TRANSPORTE.json` registra las llamadas de la ruta alternativa y el tamaño serializado de cada mensaje de la conexión **Playwright Python ↔ Node**, después de inicializar Playwright. Esa conexión es observable; no es el transporte interno del cliente Codex/visor del chat. Se impuso un presupuesto preventivo de 262.144 bytes por mensaje y se desactivó la salida de depuración que podría imprimir paquetes enteros.

Resultado: **23 comprobaciones correctas, 0 fallos**. Máximo observado: **824 bytes enviados**, **808 bytes recibidos**. Ninguna llamada `setContent` ni `screenshot`; no se devuelve base64. No hubo errores JavaScript ni HTTP en el recorrido probado.

En 1440×900 y 390×844 DPR2, las doce comparaciones de PNG mediante hashes coinciden exactamente con CP13: T34 en 0, 50 y 100 %; T45 en 35, 64 y 100 %. También se verifican inversión y pausa en ambas ventanas. Móvil emulado y Chromium/SwiftShader: no es una certificación de rendimiento físico.

La distribución también se divide en dos ZIP independientes de aproximadamente 2 MB; cada uno queda por debajo de 3,5 MB incluso si se codificase en base64. No se envían como adjuntos inline: se descargan desde GitHub y se extraen ambos en la misma carpeta. Los originales no se reducen.

## Qué queda abierto

No se dispone de la llamada ni del payload original de la apertura del chat/vista previa. Para atribuir ese error concreto falta el registro del cliente o de red asociado a esa apertura. La copia ligera evita transportar HTML gigante como mensaje y todas sus páginas son pequeñas, pero no puede reparar por sí sola un mensaje antiguo ya almacenado en el chat o un fallo interno de ese visor.

Para probar sin esa capa, descarga la copia ligera desde GitHub y ábrela en un navegador externo con el lanzador local o Live Server. No es una nueva dirección visual ni sustituye el checkpoint aprobado. CP12, CP13 y F4 se verifican sin cambios; la aceptación visual queda intacta.

## Archivos reproducibles

- `crear_vista_http.py`: extrae datos a archivos conservando bytes; no reduce imágenes.
- `EXTERNALIZACION.json`: inventario, SHA256 y diferencias de carga.
- `probar_transporte.py`: reintento con URLs, guardas de tamaño y hashes dentro del navegador.
- `PRUEBA_TRANSPORTE.json` / `.log`: observación de llamadas y resultados pequeños.
- `INTEGRIDAD_ORIGINALES.json`: comprobación de los checkpoints preservados.

No se han mostrado ni enviado al chat HTML completos, base64 o capturas de gran tamaño en este diagnóstico.
