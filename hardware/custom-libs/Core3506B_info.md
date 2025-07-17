# 📦 Información técnica del módulo Luckfox Core 3506B

El **Luckfox Core 3506B** es un módulo de cómputo compacto basado en el chip **Rockchip RK3506B**, diseñado para aplicaciones embebidas que requieren buen rendimiento, eficiencia energética y flexibilidad de expansión. Es ideal para dispositivos portátiles como el lector *Bll Pilot*.

---

## 🔍 Especificaciones generales

| Campo                     | Descripción                                     |
|--------------------------|-------------------------------------------------|
| **SoC**                  | Rockchip RK3506B                                |
| **CPU**                  | 3× ARM Cortex-A7 (hasta 1.5 GHz) + 1× Cortex-M0 |
| **GPU**                  | Integrada, soporte para gráficos 2D y 3D        |
| **RAM**                  | 512 MB DDR3L externa                            |
| **Almacenamiento**       | eMMC 8 GB integrada                             |
| **Soporte adicional**    | SPI Flash, SDMMC (microSD)                      |
| **Pines RM_IO**          | 32 líneas Rockchip Matrix IO                    |
| **Pines totales**        | 120 pines tipo *stamp hole* (espaciado 2.54 mm) |
| **Interfaces disponibles**| SPI, I2C, UART, PWM, USB, GPIO, SDIO           |
| **Dimensiones**          | 32 mm × 32 mm                                   |
| **Consumo energético**   | Bajo (ideal para dispositivos portátiles)       |
| **Conectividad**         | USB Host, posibilidad de WiFi vía dongle USB<br>Versiones Lyra W integran WiFi onboard |

---

## ✅ Ventajas clave

- 🧠 **Rendimiento superior:** arquitectura de 4 núcleos (3 Cortex-A7 + 1 Cortex-M0)
- 🎨 **Aceleración gráfica:** GPU integrada con soporte para 2D/3D
- 🔄 **Matrix IO:** multiplexación flexible de 32 líneas IO
- 🔧 **Diseño compacto:** ideal para placas base personalizadas
- 🔌 **Expansión amplia:** gracias a sus 120 pines y variedad de interfaces
- 📦 **Módulo SOM:** con formato estándar y fácil integración en diseños embebidos

---

## 📁 Aplicaciones sugeridas

- 📘 Lectores de eBooks (como *Bll Pilot*)
- 🏭 Interfaces industriales simples
- 📟 Terminales embebidos con pantalla de bajo consumo
- 🌐 Dispositivos conectados con WiFi externo o controladores USB
- 🎓 Plataformas educativas y proyectos maker

---

## 📎 Notas adicionales

- El módulo requiere una placa base (carrier board) que lo alimente y exponga sus periféricos.
- No incluye Wi-Fi de fábrica en esta versión (Core 3506B), pero puede añadirse vía dongle USB o mediante el uso del modelo **Lyra W**.

---

> Para más detalles técnicos, puedes visitar: https://wiki.luckfox.com/Core3506/Introduction (sitio oficial del fabricante)
