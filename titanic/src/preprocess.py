import numpy as np
import pandas as pd
from copy import deepcopy

CAT_VARS = ['Pclass', 'Sex', 'Embarked', 'Cabin', 'Alone', 'Title']
NUM_VARS = ['Age', 'SibSp', 'Parch', 'Fare']

def preprocess(df):
    # Categorical variables
    df['Alone'] = (df['SibSp'] + df['Parch']).apply(lambda x: 1 if x == 0 else 0)
    df['Cabin'] = df['Cabin'].apply(lambda c: c[0] if not isinstance(c, float) else 'U') # U for unknown
    for t in ['Mr', 'Miss', 'Mrs', 'Master']:
        df.loc[df['Name'].str.contains(t), 'Title'] = t
    
    # Impute
    df['Age'] = df['Age'].fillna(df.groupby(['Alone', 'Sex', 'Pclass'])['Age'].transform('mean'))
    for var in NUM_VARS:
        df[var] = df[var].fillna(df[var].mean())
    for var in CAT_VARS:
        df[var] = df[var].fillna(df[var].mode()[0])

    df = df.drop(columns=['Name', 'Ticket', 'PassengerId'])

    return df

