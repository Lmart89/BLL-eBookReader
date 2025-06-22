# BLL-eBookReader
Bll EbookReader es un lector de libros electronicos inspirado en proyectos opensource como el ePDiy v7, y proyectos similares como el OSO-Book Reader, de Joy Castillo.  
El objetivo de este proyecto es ofrecer una alternativa con capacidad de personalizacion e interaccion fluida, donde sea posible brindar una experiencia de lectura lo mas comoda posible y lo mas similar en cuanto a fluidez, cercana a los Kindle de Amazon, pero a su vez permita ofrecer la modularidad y escalabilidad para futuras mejoras.

Como cerebro y conrazon principal de este proyecto se encuentra el SoM (System on Module) de Luckfox: Luckfox Core Rv1106. entre las ventajas que ofrece es la cantidad de memoria ram, la integracion de wifi y un generoso almacenamiento eMMC de 8GB, mas que suficiente para alojar el sistema operativo, o firmware, y a su vez espacio disponible para los ficheros de usuario. esto hace que su eleccion sea mucho mas practica en comparacion con el esp32-s3 que aunque potente, no tiene ram ni el espacio de almacenamiento que si ofrece el Luckfox core rv1106.

## Caracteristicas base del Bll eBookReader.
estas son las caracteristicas base que definen el hardware base para el proyecto.
- Procesador Risc-V o ARM con potente y eficiente.
- SoC o SoM de tamaño reducido.
- bajo consumo energetico.
- soporte de buildroot o linux.
- soporte de LVGL o FrameWork grafico para desarrollo de UI
- almacenamiento interno tipo eMMC o Flash Nand de 8 GB.
- RAM 256MB - 512MB
- Soporte Wifi/Bluetooth integrado.
- Soporte para almacenamiento externo tipo micro sd.
- Pines GPIO suficientes para conexion de dispositivos y futuras expansiones. 


## Roadmap estratégico del BLL eBookReader — RV1106 con Wi-Fi / Bluetooth integrado

---

## 📦 1. Sistema operativo embebido

| Meta                                 | Estado      | Acción / Herramienta                           |
|--------------------------------------|-------------|-------------------------------------------------|
| Linux embebido funcional             | 🟢 En curso | Buildroot con kernel Rockchip                  |
| BSP para RV1106 + Wi-Fi              | 🟢 Planeado | Activar soporte al módulo integrado en DTB     |
| Arranque rápido (≤ 7 s)              | 🟢 Objetivo | Init mínimo + framebuffer + app estática       |
| App principal al inicio              | 🟢 Planeado | Lector EPUB con LVGL o UI dedicada             |

---

## 🖥️ 2. Interfaz gráfica

| Meta                                     | Estado      | Acción / Motor                                     |
|------------------------------------------|-------------|----------------------------------------------------|
| LVGL optimizado para e-paper             | 🟢 Activo   | Color 1 bit, redibujo parcial, memoria mínima      |
| Modo técnico con Nuklear (debug/config)  | 🔵 Explorando| Binario separado con acceso a parámetros internos  |
| Reinicio UI desde panel debug            | 🟢 Planeado | `lv_deinit()` o relanzamiento de binario          |
| Soporte para temas/config en tiempo real | 🟢 Objetivo | Cambios desde `/data/config.json` o similar        |

---

## 🗃️ 3. Almacenamiento eficiente

| Meta                                 | Estado      | Acción / Consideración                        |
|--------------------------------------|-------------|-----------------------------------------------|
| Uso total del sistema ≤ 100 MB       | 🟢 Meta clave | Buildroot + BusyBox + app propia optimizada   |
| Rootfs comprimido (`squashfs`)       | 🟢 Sugerido  | Reducción de tamaño en eMMC                   |
| Partición de datos (`/data`)         | 🟢 Planeado  | EPUBs, notas, configuración del usuario       |
| SD externa soportada                 | 🟢 Activo    | Lectura de archivos y actualizaciones         |

---

## 📡 4. Conectividad integrada

| Meta                        | Estado      | Acción sugerida                              |
|-----------------------------|-------------|-----------------------------------------------|
| Wi-Fi integrado operativo   | 🟢 Confirmado| Incluir driver y firmware en Buildroot        |
| Bluetooth habilitado        | 🔵 Opcional | Activar si planeas emparejar dispositivos     |
| OTA desde red local         | 🟢 Planeado | Script Python o shell para actualizar         |
| Navegación básica por red   | 🔵 Explorando| Futuro soporte para descargas o sincronización|

---

## 🔋 5. Energía y consumo

| Meta                        | Estado      | Acción                                        |
|-----------------------------|-------------|-----------------------------------------------|
| Control GPIO de encendido   | 🟢 En marcha| Pulsador + script `poweroff` limpio           |
| Suspensión por inactividad  | 🔵 A diseñar| Timeout + apagado e-paper                    |
| Apagado por menú o botón    | 🟢 Planeado | Entrada física mapeada a comando de apagado   |

---

## 📚 6. Experiencia de lectura

| Meta                         | Estado     | Acción / Herramienta                        |
|------------------------------|------------|---------------------------------------------|
| EPUB parser eficiente        | 🟢 En progreso| Motor propio o adaptado a e-paper          |
| Soporte para TXT             | 🟢 Ligero  | Render directo por líneas optimizadas       |
| Compatibilidad futura con PDF| 🔵 Evaluar| `muPDF` o rasterización a 1 bit             |
| Personalización de lectura   | 🟢 Planeado| Tamaños, tipografías, márgenes desde menú   |

---

todas estas implemntaciones estan en proceso de evaluacion y desarrollo. 


