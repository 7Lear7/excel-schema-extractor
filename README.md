# excel-schema-extractor

Script en Python para extraer las columnas (esquema) de las tablas de archivos Excel.

## Estructura del proyecto

```
excel-schema-extractor/
├── src/
│   └── excel_schema_extractor/
│       ├── __init__.py
│       ├── extractor.py      # lee el Excel y obtiene las columnas
│       └── cli.py            # entrada por línea de comandos
├── tests/
│   └── test_extractor.py
├── data/
│   ├── input/                # Excels de entrada (NO se suben a GitHub)
│   └── output/               # resultados (NO se suben a GitHub)
├── .gitignore
├── requirements.txt
└── README.md
```

## Instalación

```bash
git clone https://github.com/7Lear7/excel-schema-extractor.git
cd excel-schema-extractor

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Uso

Coloca el archivo en `data/input/` y ejecuta:

```bash
PYTHONPATH=src python -m excel_schema_extractor.cli data/input/ejemplo.xlsx
```

Salida de ejemplo:

```json
{
  "Sheet1": ["id", "nombre", "edad"]
}
```

## Flujo de trabajo en equipo

Cada persona trabaja en **su propia rama** y se une a `main` mediante **Pull Request**. Nadie sube directo a `main`.

### 1. Antes de empezar

```bash
git checkout main
git pull
```

### 2. Crear una rama para la tarea

```bash
git checkout -b feature/nombre-de-la-tarea
```

Nombres de rama:

- `feature/...` para funciones nuevas (ej. `feature/detectar-tipos-datos`)
- `fix/...` para correcciones (ej. `fix/error-hojas-vacias`)

### 3. Guardar y subir los cambios

```bash
git add .
git commit -m "Descripción corta de lo que se hizo"
git push -u origin feature/nombre-de-la-tarea
```

### 4. Pull Request

1. En GitHub aparecerá el botón **Compare & pull request**.
2. Crear el PR con una descripción breve.
3. La otra persona lo revisa y hace **Merge**.
4. Todos actualizan su copia local:

```bash
git checkout main
git pull
```

## Reglas del equipo

- **Un script = un archivo.** Si cada quien trabaja en archivos distintos, casi nunca hay conflictos.
- **Avisarse** qué archivo está editando cada quien.
- Hacer `git pull` **antes de empezar** a trabajar.
- Commits **pequeños y frecuentes**, con mensajes claros.
- **Nunca subir archivos Excel reales** ni datos sensibles. `data/input/` y `data/output/` están ignorados en `.gitignore`.
- **Nunca subir contraseñas ni tokens** al repositorio (usar archivos `.env`, que también están ignorados).
- No subir la carpeta `.venv/`.

## Resolver conflictos

Si ambos editan las mismas líneas, Git marca el conflicto así:

```
<<<<<<< HEAD
tu versión
=======
la versión de tu compañera
>>>>>>> main
```

Pasos:

1. Abrir el archivo y borrar las marcas `<<<<<<<`, `=======` y `>>>>>>>`, dejando el código correcto.
2. Guardar y ejecutar:

```bash
git add archivo.py
git commit -m "Resuelve conflicto en archivo.py"
git push
```

## Dónde va cada script

| Archivo | Para qué sirve |
|---|---|
| `extractor.py` | Leer columnas del Excel |
| `tipos.py` | Detectar el tipo de dato de cada columna |
| `exportar.py` | Guardar resultados en CSV/JSON |
| `cli.py` | Unir todo y ejecutar desde la terminal |

## Dependencias

- Python 3.10 o superior
- pandas
- openpyxl
