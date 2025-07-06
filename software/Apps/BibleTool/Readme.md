# BibleTool

**BibleTool** es una aplicación ligera, eficiente y de bajo consumo diseñada para el estudio y la consulta de la Biblia en dispositivos de recursos limitados, como e-readers basados en Linux con Buildroot (por ejemplo: el eReader personalizado de este proyecto).

BibleTool se construye con el objetivo de ofrecer una experiencia de estudio bíblico fluida, práctica y personalizable, sin sacrificar velocidad ni simplicidad.

---

## ¿Qué es BibleTool?

BibleTool es un motor de lectura y búsqueda bíblica que:

- Permite consultar el texto completo de la Biblia en español (Reina-Valera 1960 o 1909).
- Realiza búsquedas rápidas de palabras o frases en toda la Biblia, por testamento o por tipo de libro (ley, histórico, poético, profético, evangelio, epístola, apocalíptico).
- Muestra comentarios asociados a versículos específicos.
- Permite consultar definiciones y conceptos mediante un diccionario bíblico integrado.
- Diseñado para una interfaz basada en **LVGL** (Light and Versatile Graphics Library) y código en **C/C++**.

---

## Funcionalidades principales

✅ **Consulta de versículos**\
✅ **Búsqueda avanzada por palabra clave** (con filtros: testamento, tipo de libro)\
✅ **Acceso a comentarios vinculados al texto bíblico**\
✅ **Consulta de diccionario bíblico**\
✅ **Soporte para módulos adicionales (comentarios, diccionarios)**\
✅ **Bajo consumo de recursos (256 MB RAM, CPU RV1106)**\
✅ **Datos optimizados en archivos CSV y JSON**

---

## Arquitectura de módulos

BibleTool está organizado en módulos que corresponden a distintos tipos de contenido:

| Módulo          | Descripción                                | Tipo de archivo | Formato                                                       |
| --------------- | ------------------------------------------ | --------------- | ------------------------------------------------------------- |
| **Biblia**      | Texto completo de las Escrituras           | CSV             | Lb,C,V,TXT,TP,Tlb                                             |
| **Comentarios** | Notas y comentarios por versículo o pasaje | JSON            | Lista de objetos con referencia al libro, capítulo, versículo |
| **Diccionario** | Definiciones de términos bíblicos          | JSON o CSV      | Clave: término / Valor: definición                            |

### 📁 Formato de la Biblia (CSV)

| Columna | Descripción                                               |
| ------- | --------------------------------------------------------- |
| Lb      | Nombre del libro                                          |
| C       | Capítulo (entero positivo)                                |
| V       | Versículo (entero positivo)                               |
| TXT     | Texto del versículo                                       |
| TP      | Testamento: `A` = Antiguo, `N` = Nuevo                    |
| Tlb     | Tipo de libro: `L`, `H`, `P`, `Pm`, `Pn`, `E`, `Ep`, `Ap` |

Ejemplo:

```csv
Genesis,1,1,"En el principio creó Dios los cielos y la tierra.",A,L
Mateo,1,1,"Libro de la genealogía de Jesucristo, hijo de David, hijo de Abraham.",N,E
```

---

### 📁 Formato de los comentarios (JSON)

```json
[
  {
    "Lb": "Genesis",
    "C": 1,
    "V": 1,
    "Comentario": "Dios es el creador de todo lo visible e invisible."
  },
  {
    "Lb": "Mateo",
    "C": 1,
    "V": 1,
    "Comentario": "Introducción a la genealogía de Cristo."
  }
]
```

---

### 📁 Formato del diccionario (JSON)

```json
{
  "Amor": "Sentimiento de afecto y entrega desinteresada.",
  "Fe": "Confianza y creencia en Dios y sus promesas."
}
```

*(También puede usarse CSV con dos columnas: Término, Definición)*

---

## ¿Por qué BibleTool es útil y versátil?

- 🔹 **Ligero y rápido:** Diseñado para funcionar con hardware de bajo consumo (como RV1106 + 256MB RAM).
- 🔹 **Modular:** Puedes agregar o actualizar los módulos (Biblia, comentarios, diccionarios) sin modificar el motor.
- 🔹 **Filtros de búsqueda avanzados:** Busca por testamento, tipo de libro, o combinación de ambos.
- 🔹 **Fácil de adaptar:** El formato de datos es simple, plano y bien documentado.
- 🔹 **Libre de dependencias innecesarias:** Motor hecho en C/C++ con una interfaz LVGL optimizada.

---

## Licencia

BibleTool es un proyecto abierto en desarrollo. Licencia GPLv3

---

## Créditos

BibleTool es desarrollado por **Luis E Martínez S.** como parte de un proyecto personal de eReader personalizado para estudio bíblico.

---

*Nota:* En el futuro se podrá definir un logo y otros elementos visuales para BibleTool.

