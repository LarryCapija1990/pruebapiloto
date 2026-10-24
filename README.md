# Piloto 02 — F4 cerrado · CP03 v1.2

**Thunder and Lightning → Innervision, aprobada creativamente por el usuario para este piloto.** El cierre conserva el movimiento CP02 sin cambios artísticos. No se han construido otros álbumes ni se ha modificado Nero’s Vice.

## Verlo sin programar

1. Descargar [NV_SCOTT_PILOTO02_F4_CP03_v1.2_LOCAL.zip](descargas/NV_SCOTT_PILOTO02_F4_CP03_v1.2_LOCAL.zip). En la página del archivo, pulsar **Download raw file** o el icono de descarga.
2. Extraer todo en una carpeta nueva.
3. Hacer doble clic en **ABRIR_PILOTO_F4.html** y abrirlo con Chrome o Edge. `LEEME_PRIMERO.html` incluye las instrucciones.

El HTML contiene todos los recursos: no necesita Python, VS Code, terminal, servidor ni Internet. Necesita un navegador completo con JavaScript y WebGL. Si una política del equipo bloquea HTML local, usar el método de servidor explicado en [la guía de visualización](piloto02-f4/cierre-f4/RECUPERAR_Y_VISUALIZAR.md).

**Límite de la prueba local:** Chromium administrado bloqueó `file://`; se verificó el contenido del HTML en un navegador sin red y su igualdad de píxeles con CP02. La apertura nativa por doble clic no se afirma como ensayada en este entorno. La alternativa HTTP sí está probada.

## ZIP acumulativo estable y recuperable

[Descargar el cierre completo F4 CP03 v1.2](https://github.com/LarryCapija1990/pruebapiloto/archive/refs/tags/piloto02-f4-cierre-v1.2.zip).

El tag **`piloto02-f4-cierre-v1.2`** fija esta entrega. El ZIP contiene código, recursos, originales, máscaras, decisiones, historial CP01/CP02, cierre, pruebas y evidencias. Para recuperar la versión aprobada en el futuro, descargar ese tag y extraer en una carpeta nueva; `main` podrá avanzar.

## Evidencia verificable del cierre

- [Informe de cierre: pruebas, rendimiento y límites](piloto02-f4/cierre-f4/INFORME_CIERRE.md).
- [Aprobación y congelación de CP02](piloto02-f4/cierre-f4/APROBACION_F4.md).
- [Resultados estructurados de F4](piloto02-f4/cierre-f4/RESULTADOS_F4.json).
- [Capturas y evidencia visual](piloto02-f4/cierre-f4/EVIDENCIAS.md).
- [Qué se reutiliza y qué exige producción visual nueva](piloto02-f4/cierre-f4/REUTILIZACION.md).
- [Integridad del checkpoint](piloto02-f4/MANIFIESTO_F4.sha256).

Se completaron 104 comprobaciones generales, 61 de congelación/equivalencia, dos pruebas táctiles y dos recorridos de rendimiento. No hubo errores de aplicación en los flujos normales. El rendimiento por software fue lento y no certifica 30/60 FPS ni GPU o móvil físicos; consultar cifras y método en el informe.

## Ejecutar las fuentes, como alternativa

Desde la carpeta extraída del acumulativo, con Python 3.10+:

```text
Windows:       py piloto02-f4/prototipo/server.py
macOS / Linux: python3 piloto02-f4/prototipo/server.py
```

Abrir `http://127.0.0.1:4173` y mantener la terminal abierta. `Ctrl+C` detiene el servidor. Cerrar un servidor anterior o añadir `--port 4174` si el puerto está ocupado. La cabecera debe decir **F4 / CP03 · CIERRE ESTABLE**.

El archivo fuente `prototipo/index.html` requiere servidor porque carga recursos separados; el archivo **ABRIR_PILOTO_F4.html** del ZIP local es autocontenido. No deben confundirse.

## Archivo anterior

- [CP02: corrección del motivo y comparativas](piloto02-f4/revision-cp02/INFORME_CP02.md).
- [Vídeo CP02 antes/después, movimiento aprobado](piloto02-f4/revision-cp02/evidencias/F4_CP02_ANTES_DESPUES.mp4).
- [CP01: primera prueba funcional](piloto02-f4/INFORME_PRUEBAS.md).

Los textos «pendiente de revisión» de esos informes y vídeos son históricos. La aprobación vigente queda registrada en el cierre. F4 termina aquí; cualquier otra transición requiere un nuevo encargo y su propia producción visual.
