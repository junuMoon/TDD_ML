from src import data_dir
import os
from datetime import datetime

def get_null_pcnt(df):
    """
    Return the percentage of null values in a dataframe.
    """
    return {col: df[col].isnull().sum() / df.shape[0] for col in df.columns}

class SubmissionFailed(Exception):
    pass

def submit_prediction(df, message=None):
    sub_dir = data_dir / 'submissions'
    f_out = sub_dir / f'{message}_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'
    df.to_csv(f_out,
              columns=['PassengerId', 'Survived'], index = False)
    sub = os.popen(f'kaggle competitions submit -c titanic -f {f_out} -m "{message}"').read()
    if not 'Success' in sub:
        raise SubmissionFailed(sub)
    result = os.popen('kaggle competitions submissions -c titanic').read()
    try:
        acc = float(result.split('\n')[2].split('complete')[1].split('None')[0])
    except (ValueError, IndexError):
        raise SubmissionFailed(result)
    return acc
