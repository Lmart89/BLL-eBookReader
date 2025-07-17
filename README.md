# 📘 Bll Pilot

**Bll Pilot** es un proyecto de hardware libre y software de código abierto cuyo propósito es crear un lector de eBooks bíblicos de bajo consumo, enfocado en la simplicidad, portabilidad y larga duración de batería, diseñado especialmente para funcionar en zonas de baja conectividad o para uso personal/devocional.

> ✝️ *“Bll” representa muchas cosas: por un lado, “Biblia de Lectura Libre”, como un enfoque hacia el acceso abierto a la Palabra. Pero también son las iniciales de tres personas que inspiran profundamente este proyecto: Brillyd (esposa), Lemuel (hijo) y Luis (autor). "Pilot" señala que esta es la primera etapa o base para versiones futuras.*

---

## 🚀 Estado del proyecto

✨ **Actualización clave:** Al adoptar el módulo Core 3506B, el proyecto gana notables ventajas:

- 🧠 Procesador Quad-Core para mejor rendimiento multitarea
- 🎨 GPU integrada que mejora la fluidez gráfica incluso en pantallas E-Ink
- 🚀 Duplicación de RAM: de 256MB (anteriormente) a 512MB DDR3L
- 🔌 Mayor cantidad de pines IO (120), facilitando expansión sin conflictos

Estas mejoras colocan al *Bll Pilot* en una posición robusta para futuras funcionalidades sin sacrificar simplicidad ni eficiencia.

🔧 En desarrollo activo – Actualmente se encuentra en fase de diseño de hardware y primeros prototipos físicos.

La primera versión se centrará en:
- Lectura offline de textos bíblicos
- Bajo consumo y pantalla de tinta electrónica
- Interfaz minimalista para navegación fluida

---

## 🔩 Características técnicas

### 🧠 Módulo principal

- **Módulo base:** `Luckfox Core 3506B`
- **Chip:** Rockchip RK3506B
- **Procesador:** 3× Cortex-A7 + 1× Cortex-M0
- **RAM:** 512 MB DDR3L externa
- **Almacenamiento:** eMMC 8 GB por defecto
- **Almacenamiento soportado:** SPI Flash / eMMC / SDMMC
- **RM_IO:** 32 pines Rockchip Matrix IO
- **GPU:** Aceleración 2D/3D integrada
- **Conectividad:** USB host, soporte para Wi-Fi vía dongle USB (o versión Lyra W con Wi-Fi onboard)
- **Dimensiones:** 32 mm × 32 mm
- **Conectores:** 120 pines tipo *stamp hole*




### 🖥️ Pantalla
- Tipo: Pantalla E-Ink ED060XD4 (6 pulgadas, reciclada de Kindle)
- Interfaz: SPI
- Controlador: Requiere PMIC externo (como TPS65185)

### 🔌 Conectividad
- Táctil capacitivo (opcional, vía I2C)
- MicroSD (opcional)
- USB tipo C para carga y datos

### 🔋 Energía
- Batería de polímero de litio (con circuito de protección y carga)
- Circuito de bajo consumo en standby


---

## 📱 Software

El sistema estará basado en:
- 🐧 **Linux embebido** con Buildroot
- 🧱 Interfaz ligera (basada en LVGL o framebuffer directo)
- 📖 Motor de renderizado de textos optimizado para pantallas E-Ink
- 🕮 Indexación de la Biblia en diferentes versiones
- ⛺ Posibilidad de agregar documentos EPUB, TXT o formatos ligeros


---

## 🔓 Licencia

### 🔧 Hardware
Este proyecto está licenciado bajo la **CERN Open Hardware License v2 – Strongly Reciprocal (CERN OHL v2-S)**.

> Esto significa que cualquier derivado del hardware deberá mantenerse igualmente abierto y compartido con la comunidad.

### 💾 Software
El software se publica bajo la **GNU General Public License v3.0 (GPLv3)**.

> Esta licencia protege las libertades de uso, estudio, modificación y distribución del código, asegurando que permanezca siempre libre para todos los usuarios.


---

## 🧭 Visión futura

**Bll Pilot** nace como una plataforma que va más allá de ser un lector de eBooks:

- 📖 Herramienta de estudio bíblico portátil
- ⛺ Recurso para comunidades en zonas rurales o de difícil acceso
- 🛠️ Plataforma educativa para makers que deseen aprender sobre hardware embebido
- 📚 Dispositivo de lectura privada o devocional

Más adelante podrían desarrollarse versiones ampliadas, con audio, conectividad Wi-Fi permanente, y sincronización de notas o planes de lectura.

---

## 🙏 Créditos y agradecimientos

Proyecto impulsado por Luis E. Martínez S., con pasión por la electrónica, la Biblia, y el aprendizaje autodidacta.

Inspirado en la necesidad de crear herramientas útiles, abiertas y accesibles para todos.

> *Soli Deo Gloria.*

