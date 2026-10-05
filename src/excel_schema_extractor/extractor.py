import pandas as pd

def extract_columns(path):
    """Devuelve {nombre_hoja: [columnas]} de un archivo Excel."""
    sheets = pd.read_excel(path, sheet_name=None, nrows=0)
    return {name: list(df.columns) for name, df in sheets.items()}
