# Proyecto de Asistencia y Producción

Este repositorio contiene una aplicación desarrollada en Python para el área de producción, destinada a procesar datos de asistencia y producción registrados en hojas de cálculo. La herramienta permite generar reportes estandarizados y previsualizar datos mediante una interfaz gráfica construida con PySide6.

---

## 🛠️ Tecnologías y librerías

- **Lenguaje:** Python 3.11+ (probado en versiones recientes de la rama 3.11/3.12)
- **GUI:** [PySide6](https://pypi.org/project/PySide6/) (bindings de Qt6 para Python)
- **Manipulación de datos:** `pandas`, `openpyxl`
- **Tests:** `pytest`

Ver `requirements.txt` para la lista exacta de dependencias.

---

## 🧱 Estructura del proyecto

```
Asistencia/                # carpeta raíz del workspace
├─ data/                   # datos de entrada y salida por defecto
├─ src/proyecto/           # código fuente principal
│  ├─ config.py            # rutas por defecto
│  ├─ main.py              # punto de entrada de la aplicación
│  ├─ processor.py         # lógica de la ventana y modelo de datos
│  ├─ utils.py             # utilidades generales (si aplica)
│  ├─ models/              # servicios de procesamiento
│  │  ├─ procesamiento_asistencia.py
│  │  └─ procesamiento_produccion.py
│  └─ UI/                  # interfaz generada por Qt Designer
│     └─ diseño.py
└─ tests/                  # pruebas unitarias con pytest
   ├─ test_asistencia.py
   ├─ test_produccion.py
   └─ test_plantilla.py
```

---

## ⚙️ Funcionalidades principales

1. **Procesamiento de asistencia**
   - Lee archivos Excel/CSV con columnas `Codigo` y `Fecha y hora`.
   - Filtra por rango de fechas configurables.
   - Calcula horas trabajadas, detecta turnos válidos, faltas de salida y marcaciones duplicadas menores a 30 min.
   - Genera un formato semanal de asistencia (`reporte_semanal.xlsx`) y un reporte consolidado (`reporte_asistencia.xlsx`).

2. **Procesamiento de producción**
   - Lee archivos con columnas `Codigo`, `Orden y maquina`, `Fecha y hora`.
   - Extrae orden y máquina, determina duración y último operador.
   - Clasifica turnos (día, noche, mixto) y genera `Reporte_produccion.xlsx`.

3. **Interfaz gráfica**
   - Pantalla única con botones para seleccionar archivo, carpeta de salida, previsualizar y generar reportes.
   - Cambio dinámico entre modo "Asistencia" y "Producción".
   - Tabla de previsualización con colores y estilos según observaciones.

4. **Pruebas unitarias**
   - Cobertura básica para validación de columnas, cálculo de observaciones y clasificación de turnos.
   - Se emplea `pytest` para garantizar integridad del procesamiento.

---

## 🚀 Uso

1. Clonar el repositorio.
2. Crear y activar un entorno virtual (recomendado).
3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```
4. Ejecutar la aplicación:
   ```bash
   python -m src.proyecto.main
   ```
5. Seleccionar el archivo de origen y carpeta de destino en la GUI.
6. Previsualizar los datos y generar el reporte.

---

## 📁 Archivos de datos por defecto

- `data/Asistencia.xlsx` -> plantilla de asistencia.
- `data/Produccion.xlsx` -> plantilla de producción.
- Salidas generadas se guardan en la misma carpeta `data/` si no se especifica otra.

---

## � Generar un ejecutable

Para facilitar la distribución a usuarios que no quieran instalar Python, se puede empaquetar la aplicación en un ejecutable independiente.

1. Instalar PyInstaller en el entorno virtual:
   ```bash
   pip install pyinstaller
   ```
2. Desde la raíz del proyecto ejecutar:
   ```bash
   pyinstaller --onefile --windowed src/proyecto/main.py
   ```
   - `--onefile` crea un único binario.
   - `--windowed` evita que aparezca una consola en Windows.

3. El ejecutable se generará en `dist/main.exe`. Copia también la carpeta `data/` si usas archivos predeterminados.
4. Opcional: personaliza el ícono con `--icon=path/to/icon.ico` y ajusta el `.spec` si necesitas incluir otros recursos.

Los usuarios sólo deberán ejecutar `main.exe` sin instalar nada adicional, siempre que las librerías necesarias estén empaquetadas correctamente. Si se detectan problemas con PySide6, puede ser necesario ajustar la configuración de PyInstaller o consultar la documentación oficial.

---

## �📝 Notas adicionales

- La interfaz fue diseñada con Qt Designer y convertida a Python en `src/proyecto/UI/diseño.py`.
- El proyecto se orientó a brindar una solución simple y reutilizable para el área de producción de la empresa.
- Se busca mantener el código modular para facilitar futuras extensiones o migraciones.

---

**Si necesitas más información o asistencia, revisa los archivos de tests o el código fuente; están bien documentados con comentarios.**

---

© 2026 - Desarrollo interno.