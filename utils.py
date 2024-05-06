import pandas as pd
import os

OUT_DIR = 'out_datasets'
IN_DIR = 'in_datasets'

FILENAMES = ['1_base_limpia.csv']
DATASET = './in_datasets/Base_PreguntasFormulario-1erDebatePresidencial2024.xlsx'

def save_df(df: pd.DataFrame, idx: int, **kwargs) -> None:
    if idx >= len(FILENAMES):
        raise IndexError
    if not os.path.exists(OUT_DIR):
        os.mkdir(OUT_DIR)
    filename = os.path.join(OUT_DIR, FILENAMES[idx])
    df.to_csv(filename, **kwargs)