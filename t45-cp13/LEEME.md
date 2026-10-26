# CP13 v1.0 · Ajuste de ritmo por scroll

El usuario acepta la apariencia CP12 de Thunder → Innervision → Salute. Esta versión modifica exclusivamente la distribución y longitud del scroll, para probar los tramos abstractos a la mitad de distancia. No cambia formas, texturas, color, trayectoria de cámara ni originales. El ritmo CP13 queda para revisión.

## Abrir

Descarga el ZIP LOCAL con **Download raw file**, extráelo por completo y abre **ABRIR_T34_T45_CP13.html** con Chrome o Edge. El HTML contiene todos los recursos; no requiere internet ni instalar programas. No lo abras desde dentro del ZIP.

Si tu equipo bloquea HTML local, abre la carpeta en Visual Studio Code y usa Live Server. Si ya tienes Python, ejecuta `py -m http.server 4192` (Windows) o `python3 -m http.server 4192` (macOS/Linux) en esta carpeta y visita `http://localhost:4192/ABRIR_T34_T45_CP13.html`. Ese enlace funciona solo en tu ordenador. Este entorno bloqueó file:// en las versiones anteriores; la prueba offline de documento no equivale a verificar doble clic bajo esa política.

## Distribución de la primera prueba

|Tramo visual de CP12|Antes|CP13|
|---|---:|---:|
|Thunder: entrada documental, p 0–10 %|55vh|55vh|
|Thunder → Innervision abstracto, p 10–90 %|440vh|220vh|
|Innervision: revelación completa, p 90–100 %|55vh|55vh|
|Parada entre transiciones|20vh|20vh|
|Innervision: acercamiento, q 0–18 %|99vh|99vh|
|Innervision → Salute abstracto, q 18–70 %|286vh|143vh|
|Salute: revelación completa, q 70–100 %|165vh|165vh|
|**Total efectivo**|**1120vh**|**757vh**|

El recorrido pasa de 11,2 a 7,57 alturas de pantalla: **32,4 % menos**. No se redistribuyen los 363vh eliminados a pausas ni a otros tramos. La parada explícita de Innervision sigue siendo 20vh y se conservan sus estados documentales contiguos.

Los porcentajes de los controles siguen designando **las mismas imágenes p/q de CP12**, no una fracción lineal de la nueva distancia de scroll. El cambio de cuerpo de T45 sigue en q 32–39 % como referencia visual; ahora se recorre más deprisa. Acercamiento y revelación conservan su distancia original.

La entrada y salida de cada banda acelerada tienen rampas suaves de velocidad. En sus extremos la relación con el scroll coincide con la original; en el centro alcanza 2,25× para que la banda completa ocupe exactamente la mitad. El mapa es monótono, invertible y sin velocidad infinita. No hay reloj, reproducción autónoma ni efectos nuevos.

## Qué se conserva

El prefijo de render de `t45.js` (incluidas geometría, cámara, material y composición), `cuerpo.js`, máscaras y campos permanecen byte a byte como CP12. F4 se sigue incorporando desde su ZIP original, sin editar su motor: el cambio de duración de Thunder → Innervision ocurre en el coordinador exterior. CP12 y los anteriores checkpoints permanecen recuperables.

`REFERENCIA_CP12.html` es la versión aceptada anterior, incluida para comparar. El nuevo ejecutable es **ABRIR_T34_T45_CP13.html**. El paquete de fuentes incluye código, recursos, referencia y pruebas; no incluye los 210 MB del histórico F4, que siguen en su tag original.

## Código y pruebas

- `implementacion/ritmo.js`: único modelo nuevo; convierte progreso visual a distancia y viceversa.
- `implementacion/t45.js`: usa ese mapa para leer scroll, navegar y calcular longitudes; render y cámara sin cambios.
- `python implementacion/construir.py`: reconstruye el HTML con biblioteca estándar.
- `node implementacion/probar_modelo.cjs`: verifica longitudes, mitad exacta, monotonía, inversa y empalmes.
- `python implementacion/probar_cp13.py`: comparación visual con CP12, scroll reversible, pausa, resize, controles y modo reducido; requiere Playwright, Pillow y Chromium.

Las comparaciones exactas de imagen fijan el mismo progreso visual p/q en ambos motores. Las pruebas de navegación usan scroll real y tolerancia .001 por su redondeo a píxeles enteros, ahora ligeramente más visible al acelerarlo. Se comprueban por separado: no se confunde posición física de scroll con identidad del fotograma.

Consulta `INFORME_CP13.md` y `REVISION_CP13.html`. La aceptación visual procede del usuario; la nueva distribución es una primera prueba de ritmo. El móvil de pruebas es emulado y el render por software no certifica fluidez física. No se ha modificado Nero’s Vice ni se han añadido álbumes.
