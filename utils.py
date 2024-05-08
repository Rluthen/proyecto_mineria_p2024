import pandas as pd
import os

OUT_DIR = 'out_datasets'
IN_DIR = 'in_datasets'

DATASET = './in_datasets/Base_PreguntasFormulario-1erDebatePresidencial2024.xlsx'

def save_df(df: pd.DataFrame, name: str, **kwargs) -> None:
    if not os.path.exists(OUT_DIR):
        os.mkdir(OUT_DIR)
    filename = os.path.join(OUT_DIR, name)
    df.to_csv(filename, **kwargs)