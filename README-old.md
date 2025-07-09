# BLL-eBookReader
Bll EbookReader es un lector de libros electronicos inspirado en proyectos open-source como el ePDiy v7, proyectos similares como el OSO-Book Reader, de Joy Castillo, e incluso el Esp32-epub reader.  
El objetivo de este proyecto es ofrecer una alternativa con capacidad de personalizacion e interaccion fluida, donde sea posible brindar una experiencia de lectura lo mas comoda posible y lo mas similar en cuanto a fluidez, cercana a los Kindle de Amazon, pero a su vez permita ofrecer la modularidad y escalabilidad que el usuario requiera ya sea desarrollando su propia implementacion o modificando el sistema a gusto propio.

## ¿Porque un SoM 🧩 (System on Module) y no un MCU 🧠 (Microcontrolador)?

Existen muchas razones por las que este proyecto esta enfocado en el uso de un SoM 🧩 y no un mcu; La respuesta a esta pregunta tiene que ver con 3 aspectos fundamentales de este proyecto:
### 1 - desempeño.
La mayoria de mcus en el mercado actual tienen un desempeño limitado para tareas pesadas, de alli su bajo precio y facilidad de uso, porque estan diseñados para control y automatizacion de tareas especificas. A diferencia de los mcu, los SoM usan una cpu mas potente ofreciendo incluso excelente desempeño para tareas y cargas de trabajo mas pesadas.
### 2 - integracion.
La diferencia fundalmental entre un SoM y un MCU radica en las prestaciones de los componentes. un mcu aunque posee un nivel de integracion alto, las prestaciones estan enfocadas en ofrecer eficiencia energetica y un desempeño modesto. en cambio un SoM es un mini pc embebido con componentes de alto desempeño enfocado en ofrecer mayor rendimiento para tareas mas complejas, permitiendo mayor fluidez en rendimiento general.
### 3- flexibilidad de funcionamiento.
Los mcus estan limitados a ejecutar cierto software de programacion basico, como micropython o el indicado por el fabricante, y aunque puede ser altamente personalizable, tiende a ser limitado en cuanto a frameworks de desarrollo y programacion.
Los SoM a ser computadoras embebidas en una placa, y debido a sus prestaciones permiten opciones mucho mas flexibles de desarrollo, entre ellas la capacidad de ejecutar entornos linux y acceso a funcionalidades y librerias extendidas.
Estos aspectos clave dieron forma las caracteristicas que deben ser incorporadas.

## Caracteristicas base del Bll eBookReader.
estas son las caracteristicas base que definen el hardware base para el proyecto.
- Procesador Risc-V o ARM con potente y eficiente.
- SoC o SoM de tamaño reducido.
- Bajo consumo energetico.
- Soporte de buildroot o linux.
- Soporte de LVGL o FrameWork grafico para desarrollo de UI
- Almacenamiento interno tipo eMMC o Flash Nand de 8 GB.
- RAM 256 MB - 512 MB.
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


