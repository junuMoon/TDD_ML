import numpy as np
import pandas as pd

def preprocess(df, drop=True):
    # Categorical variables
    df['Alone'] = (df['SibSp'] + df['Parch']).apply(lambda x: 1 if x == 0 else 0)
    df['Cabin'] = df['Cabin'].apply(lambda c: c[0] if not isinstance(c, float) else 'U') # U for unknown

    # Impute
    df['Age'] = df['Age'].fillna(df.groupby(['Alone', 'Sex', 'Pclass'])['Age'].transform('mean'))

    if drop:
        df = df.dropna()

    return df
