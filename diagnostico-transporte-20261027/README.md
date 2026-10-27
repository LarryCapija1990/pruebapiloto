# Diagnóstico del límite de mensajes · 27 de octubre de 2026

El error original se produce al abrir el chat/vista previa. **Su llamada interna exacta no está disponible en los logs accesibles**; no se atribuye a la animación. El informe distingue ese fallo de los riesgos detectados en llamadas de prueba que enviaban HTML completo.

- [Informe: evidencia, llamadas candidatas y límite del diagnóstico](INFORME.md).
- Copia ligera: [parte 1](https://github.com/LarryCapija1990/pruebapiloto/blob/diagnostico-transporte-cp13-v1.0/descargas/NV_SCOTT_CP13_VISTA_HTTP_PARTE_01_v1.0.zip) y [parte 2](https://github.com/LarryCapija1990/pruebapiloto/blob/diagnostico-transporte-cp13-v1.0/descargas/NV_SCOTT_CP13_VISTA_HTTP_PARTE_02_v1.0.zip). Ambas se extraen en la misma carpeta; no se recomprime ninguna imagen.
- [Medición de mensajes y pruebas de la ruta alternativa](PRUEBA_TRANSPORTE.json).
- [Integridad de los originales](INTEGRIDAD_ORIGINALES.json).

La copia ligera se abre **en navegador externo mediante un servidor local**, no en el visor del chat. Extrae ambos ZIP en la misma carpeta; usa `INICIAR_WINDOWS.bat` si tienes Python, o Live Server de Visual Studio Code sobre `index.html`. En macOS/Linux: `python3 INICIAR.py`.

Los documentos pasan de 7,18 MB y 4,33 MB a 18,6 KB y 32,1 KB. Diez recursos conservan sus bytes originales. El reintento observado devuelve solo hashes y tamaños: máximo 824 bytes de envío y 808 de recepción en Playwright; 23 comprobaciones correctas. Estos límites medidos no son una traza del cliente Codex.

Se preservan F4, CP12 y CP13 sin cambios. La alternativa está verificada; no se declara solucionado un error interno del chat que no se puede observar desde este entorno.
