from pathlib import Path
path = Path(__file__).absolute().parent.parent
data_dir = path / 'data'

import pandas as pd

def load_dataset():
    df_train = pd.read_csv(data_dir / 'train.csv')
    df_test = pd.read_csv(data_dir / 'test.csv')
    return df_train, df_test