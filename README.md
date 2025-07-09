# 📖 Bll eBook Reader

**Un lector electrónico versátil, eficiente y con propósito**

---

## ✨ ¿Qué es el Bll eBook Reader?

El **Bll eBook Reader** es un lector de libros electrónicos creado desde cero, pensado no solo como una alternativa a dispositivos comerciales como el Kindle, sino como una **herramienta versátil de lectura, estudio y organización personal**, especialmente útil para quienes estudian, enseñan o predican la Biblia. Diseñado para funcionar con recursos limitados, es **libre, optimizado y altamente personalizable**.

---

## 🔧 Hardware

Este lector se basa en un hardware distinto a la mayoría de dispositivos similares, lo que permite libertad total en su desarrollo y expansión:

- **Procesador**: Luckfox Core RV1106 – Cortex-A7, eficiente y de bajo consumo.
- **RAM**: 256 MB DDR3
- **Almacenamiento**: 8 GB eMMC (integrado)
- **Pantalla**: E-Ink de 6 pulgadas (sin retroiluminación por ahora)
- **Touch**: Opcional, no habilitado en las primeras versiones
- **Conectividad**: Wi-Fi / Bluetooth integrados
- **Sistema Operativo**: Linux personalizado usando **Buildroot**
- **Placa Base**: Diseño propio (inspirado en proyectos como epdiy v7 pero adaptado al RV1106)
- **Fuente de alimentación y protección**: Incluye fusibles para proteger el SoM

---

## 🚀 Características destacadas

- 🧠 **Ultraligero**: sistema operativo minimalista con lo esencial, optimizado para bajo uso de RAM y energía.
- 📚 **Soporte para múltiples formatos de eBooks**: EPUB, MOBI, TXT, PDF (parcial).
- 📖 **Modo Biblia integrado**: navegación optimizada por libros, capítulos y versículos.
- 📝 **Notas personales**: sistema simple de notas para estudios, bosquejos y predicaciones.
- 📡 **Actualizaciones inalámbricas** (por Wi-Fi).
- 📁 **Sistema de archivos organizado** para acceder a libros, notas y documentos con rapidez.

---

## 🎯 ¿Por qué es diferente?

La mayoría de lectores electrónicos están cerrados a modificaciones. El **Bll eBook Reader** es:

- ✅ **Totalmente libre y abierto**: el software está bajo licencia GPLv3 y el hardware bajo una licencia de hardware libre.
- ✅ **Protegido contra la apropiación comercial restrictiva**: cualquier persona que modifique o redistribuya debe mantener la apertura del código y los archivos de hardware.
- ✅ **Versátil**: no se limita a libros; puede convertirse en una libreta digital, lector de notas pastorales, organizador de predicaciones, etc.
- ✅ **Diseñado para crecer**: puede extenderse con mejoras como pantalla táctil, retroiluminación o integración con servidores locales para compartir materiales.

---

## 🧱 Estado del desarrollo

- [x] Diseño del PCB personalizado
- [x] Integración básica con pantalla E-Ink
- [x] Sistema Linux embebido funcional (Buildroot)
- [ ] Interfaz gráfica liviana con **LVGL**
- [ ] Modo Biblia con navegación completa
- [ ] Sistema de notas sencillo
- [ ] Conectividad Wi-Fi funcional y segura
- [ ] Soporte para sincronización o backup

---

## 💡 Casos de uso

- Lectura diaria de la Biblia y devocionales
- Acceso a libros de estudio teológico
- Organización de bosquejos para sermones
- Anotaciones rápidas durante clases o reuniones
- Lectura offline de contenido útil sin distracciones

---

## 📜 Licencia

### Software

Este proyecto se distribuye bajo los términos de la **GNU General Public License v3.0 (GPLv3)**.  
Esto garantiza que cualquier persona que modifique o redistribuya el software **debe mantenerlo libre y accesible** bajo la misma licencia.

Consulta el archivo [`LICENSE`](./LICENSE) para más información.

### Hardware

Los archivos de hardware (esquemáticos, PCB, listas de materiales) se publican como **Open Hardware** bajo la licencia  
**CERN Open Hardware License v2 – Strongly Reciprocal**.  
Esto significa que:

- Puedes usar, estudiar, modificar y fabricar este hardware.
- Si lo redistribuyes o haces productos derivados, **debes también liberar tus archivos bajo la misma licencia**.
- **No está permitido cerrarlo ni venderlo como producto propietario** sin publicar tus modificaciones.

Consulta el archivo [`hardware/LICENSE`](./hardware/LICENSE) para más información.

---

