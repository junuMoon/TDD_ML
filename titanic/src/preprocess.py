from src import CAT_VARS

def preprocess(df, to_submit=False):

    df['Relatives'] = df['SibSp'] + df['Parch']
    df['Alone'] = df['Relatives'].apply(lambda x: 1 if x == 0 else 0)
    df['Cabin'] = df['Cabin'].apply(lambda c: c[0] if not isinstance(c, float) else 'U') # U for unknown
    for t in ['Mr', 'Miss', 'Mrs', 'Master']:
        df.loc[df['Name'].str.contains(t), 'Title'] = t

    if to_submit:
        df = df.drop(columns=['Name', 'Ticket'])
    else:
        df = df.drop(columns=['Name', 'Ticket', 'PassengerId'])


    df = freq_encoding(df, CAT_VARS)
    df = impute(df)
    # df = label_encoding(df, CAT_VARS)
    return df

def impute(df, num='median', cat='mode'): #TODO: select method
    # Impute
    df['Age'] = df['Age'].fillna(df.groupby(['Alone', 'Sex', 'Pclass'])['Age'].transform('mean'))
    for var in CAT_VARS:
        df[var] = df[var].fillna(df[var].mode()[0])
    for var in [c for c in df.columns if c not in CAT_VARS]:
        df[var] = df[var].fillna(df[var].median())
    return df

def label_encoding(df, cols):
    for col in cols:
        df[col] = df[col].astype('category').cat.codes
    return df

def freq_encoding(df, cols):
    for col in cols:
        encoding = df.groupby(col).size() / df.shape[0]
        df[col] = df[col].map(encoding)
    return df