# 📖 eBook Reader - Apps y Módulos

Este documento describe las **aplicaciones** que forman parte del eBook Reader, los lenguajes utilizados, sus dependencias, cómo integrarlas al sistema y ejemplos prácticos de desarrollo.

---

## 🛠 Lenguajes y frameworks

Las aplicaciones del eBook Reader están desarrolladas principalmente en:

| Componente         | Lenguaje | Framework                               |
|--------------------|----------|-----------------------------------------|
| Interfaz gráfica    | C / C++  | LVGL (Light and Versatile Graphics Library) |
| Lógica / Backend    | C / C++  | Nativo, sin frameworks pesados         |
| Scripts utilitarios | Python (opcional, durante generación de datos, no en runtime) | - |

El uso de C/C++ permite máxima eficiencia en el hardware limitado (RV1106, 256 MB RAM).

### ⚙ Herramientas de compilación sugeridas

- **Makefiles** o **CMake** para proyectos C/C++.
- Toolchain generada por Buildroot (cross-compilador para RV1106).
- LVGL como librería estática incluida en el build.

---

## 📦 Aplicaciones principales

| App          | Descripción                         | Binario / Módulo   | Dependencias            |
|--------------|-------------------------------------|-------------------|------------------------|
| **BibleTool** | Lectura, búsqueda y estudio bíblico | Binario integrado  | LVGL, acceso a CSV/JSON |
| **BookReader**| Lector de libros electrónicos       | Binario integrado  | LVGL                    |
| **NoteApp**   | App de notas y apuntes              | Módulo o binario   | LVGL                    |
| **Settings**  | Configuración del sistema           | Módulo esencial    | LVGL                    |

---

## 🔗 Integración al eBook Reader

- **Formato**: Las apps se integran como binarios independientes o módulos que el sistema llama desde el menú principal.
- **Compilación**: Cada app debe ser compilada estáticamente o como binario cargable desde el almacenamiento.
- **Recursos compartidos**: Framebuffer, entrada táctil (si disponible), eMMC, red.
- **Datos**: Formatos planos (CSV, JSON) alojados en el eMMC.

### 📂 Ejemplo de estructura de proyecto

```
/apps
  /bibletool
    main.c
    Makefile
    lv_conf.h
    /assets
      logo.bin
    /data
      rv60.csv
      diccionario.json
```

### 📝 Ejemplo de Makefile

```makefile
CC = arm-linux-gnueabihf-gcc
CFLAGS = -O2 -static
LDFLAGS = -llvgl

TARGET = bibletool
SRCS = main.c

all:
\t$(CC) $(CFLAGS) -o $(TARGET) $(SRCS) $(LDFLAGS)

clean:
\trm -f $(TARGET)
```

### 🚀 Comando de compilación

```bash
make
```
o manualmente:
```bash
arm-linux-gnueabihf-gcc -O2 -static -o bibletool main.c -llvgl
```

### 🛠 Instrucciones para integrar el binario

1️⃣ Copia el binario al dispositivo:
```bash
scp bibletool root@device:/apps/bibletool
```

2️⃣ Asegura permisos de ejecución:
```bash
chmod +x /apps/bibletool
```

3️⃣ Edita el menú del launcher:
```bash
vi /etc/ebook_launcher.conf
```
Y añade:
```
BibleTool,/apps/bibletool
```

---

## ✅ Requerimientos para añadir nuevas apps

- C/C++ o compatible con el entorno minimalista.
- Uso de LVGL o interfaz directa sobre framebuffer.
- Binarios compactos (ideal < 2 MB).
- Sin librerías externas pesadas.
- Integración al menú mediante launcher.

---

## 📄 Licencia

Las aplicaciones están licenciadas bajo **GPLv3**, salvo indicación diferente en casos particulares.

---

Si deseas más detalles sobre la creación de nuevas aplicaciones o la arquitectura de integración, revisa la documentación de **Buildroot** y **LVGL**.
