import pandas as pd
from pathlib import Path

def open_data_file():
    xlsx_path = Path(__file__).parent
    df = pd.read_excel(xlsx_path / "encoded_data.xlsx", sheet_name='INDIV_VAR_REG')
    return df

