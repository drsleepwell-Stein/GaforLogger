import pandas as pd
from pathlib import Path

EXCEL = Path("data/gafor_log.xlsx")

def append_row(timestamp, gafor_dict):
    row = {"Zeitstempel": timestamp}
    row.update(gafor_dict)
    df_new = pd.DataFrame([row])

    if EXCEL.exists():
        df_old = pd.read_excel(EXCEL)
        df = pd.concat([df_old, df_new], ignore_index=True)
    else:
        df = df_new

    EXCEL.parent.mkdir(exist_ok=True)
    df.to_excel(EXCEL, index=False)
