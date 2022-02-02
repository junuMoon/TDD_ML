from pathlib import Path
path = Path(__file__).absolute().parent.parent
data_dir = path / 'data'
raw_dir = data_dir / 'raw'

import pandas as pd

def load_dataset():
    df_train = pd.read_csv(raw_dir / 'train.csv')
    df_test = pd.read_csv(raw_dir / 'test.csv')
    return df_train, df_test

CAT_VARS = ['Pclass', 'Sex', 'Embarked', 'Cabin', 'Alone', 'Title']