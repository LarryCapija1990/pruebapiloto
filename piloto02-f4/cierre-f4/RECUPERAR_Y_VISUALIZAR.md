# Visualizar y recuperar el cierre de F4

## Sin conocimientos de programación

1. Descargar [el ZIP local F4 CP03](../../descargas/NV_SCOTT_PILOTO02_F4_CP03_v1.2_LOCAL.zip) desde GitHub. Si aparece una página de archivo, pulsar **Download raw file** o el icono de descarga.
2. Extraer todo el ZIP en una carpeta nueva. En Windows: clic derecho → **Extraer todo**. No abrir el piloto dentro del ZIP.
3. Hacer doble clic en **ABRIR_PILOTO_F4.html**, preferiblemente con Chrome o Edge actualizado. `LEEME_PRIMERO.html` contiene la guía por pasos.
4. Usar scroll, el control **Recorrido** o los botones de extremos. Para parar, detener el scroll. Para regresar, desplazar en sentido contrario. **Reducir movimiento** fija la cámara y el terreno.

No hace falta Python, VS Code, una terminal, servidor o conexión a Internet para el HTML autocontenido. Sí se necesita un navegador completo con JavaScript y WebGL. Algunos visores de archivos de móvil no ejecutan JavaScript: abrirlo con el navegador, no con la previsualización de archivos.

La cabecera debe indicar **F4 / CP03 · CIERRE ESTABLE**. El movimiento es exactamente el CP02 aprobado. Los únicos cambios visibles del cierre son los textos de estado.

**Límite de verificación:** el Chromium administrado del entorno de pruebas bloquea `file://` con `ERR_BLOCKED_BY_ADMINISTRATOR`. El HTML extraído fue probado cargando su contenido en un contexto de navegador sin red, con igualdad de píxeles; no se presenta como una apertura nativa de archivo validada. En un equipo con una política similar, usar la alternativa HTTP de abajo. No se han eludido políticas del navegador ni se han desactivado verificaciones de seguridad.

## Alternativa con servidor local, verificada

Usar el [ZIP acumulativo estable](https://github.com/LarryCapija1990/pruebapiloto/archive/refs/tags/piloto02-f4-cierre-v1.2.zip), extraerlo y abrir su carpeta en VS Code. Abrir **Terminal → Nueva terminal** y ejecutar una sola línea:

```text
Windows:       py piloto02-f4/prototipo/server.py
macOS / Linux: python3 piloto02-f4/prototipo/server.py
```

Abrir `http://127.0.0.1:4173` en el navegador local y mantener la terminal abierta. Este método necesita Python 3.10+; no instala paquetes. `Ctrl+C` detiene el servidor. Cerrar primero el servidor de una versión anterior para no visualizarla por error. Si el puerto está ocupado, añadir `--port 4174` y usar ese puerto en el navegador.

La restricción de abrir directamente `prototipo/index.html` sigue siendo válida para las fuentes, que cargan archivos separados. **ABRIR_PILOTO_F4.html es otro archivo, autocontenido**, preparado para uso local sin esas solicitudes de recursos.

## Recuperación exacta

La rama `main` puede avanzar en el futuro. Para recuperar este cierre, descargar siempre el ZIP del tag **`piloto02-f4-cierre-v1.2`**, no el ZIP de la rama. Extraerlo en una carpeta nueva para conservar cualquier trabajo local.

El acumulativo incluye código, fuentes F0–F3, originales, máscaras, capas, decisiones, CP01/CP02, cierre, pruebas, capturas, registros y el ZIP local. `MANIFIESTO_F4.sha256` verifica los archivos de `piloto02-f4/`; `PORTABLE.json` registra el ZIP local y los archivos que contiene. Los hashes sirven para detectar cambios; la procedencia se ancla en el commit y el tag del repositorio.

Para reconstruir el ZIP local desde las fuentes, un desarrollador puede ejecutar `python3 piloto02-f4/cierre-f4/crear_portable.py`. Solo usa la biblioteca estándar de Python. Su reconstrucción se comprueba por SHA-256 en el entorno de cierre; versiones diferentes de la biblioteca de compresión pueden producir bytes ZIP distintos, aunque los archivos HTML internos sean idénticos.

Para repetir pruebas se necesitan las dependencias opcionales de `pruebas/requirements.txt`, Chromium y, para regenerar vídeos, FFmpeg. Esas herramientas no son necesarias para visualizar el HTML local.
