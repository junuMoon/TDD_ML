from src import NUM_VARS, CAT_VARS

def preprocess(df, to_submit=False):
    df['Relatives'] = df['SibSp'] + df['Parch']
    df['Alone'] = df['Relatives'].apply(lambda x: 1 if x == 0 else 0)
    df['Cabin'] = df['Cabin'].apply(lambda c: c[0] if not isinstance(c, float) else 'U') # U for unknown
    for t in ['Mr', 'Miss', 'Mrs', 'Master']:
        df.loc[df['Name'].str.contains(t), 'Title'] = t
    df = impute(df)
    df = label_encoding(df, CAT_VARS)

    if to_submit:
        df = df.drop(columns=['Name', 'Ticket'])
    else:
        df = df.drop(columns=['Name', 'Ticket', 'PassengerId'])
    return df

def impute(df, num='median', cat='mode'): #TODO: select method
    # Impute
    df['Age'] = df['Age'].fillna(df.groupby(['Alone', 'Sex', 'Pclass'])['Age'].transform('mean'))
    for var in NUM_VARS:
        df[var] = df[var].fillna(df[var].median())
    for var in CAT_VARS:
        df[var] = df[var].fillna(df[var].mode()[0])
    return df

def label_encoding(df, cols):
    for col in cols:
        df[col] = df[col].astype('category').cat.codes
    return df

