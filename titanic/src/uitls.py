def get_null_pcnt(df):
    """
    Return the percentage of null values in a dataframe.
    """
    return {col: df[col].isnull().sum() / df.shape[0] for col in df.columns}