from src import data_dir
import os

def get_null_pcnt(df):
    """
    Return the percentage of null values in a dataframe.
    """
    return {col: df[col].isnull().sum() / df.shape[0] for col in df.columns}

class SubmissionFailed(Exception):
    pass

def submit_prediction(df, message=None):
    df.to_csv(data_dir/'submission.csv',
              columns=['PassengerId', 'Survived'], index = False)
    sub = os.popen(f'kaggle competitions submit -c titanic -f {str(data_dir/"submission.csv")} -m "{message}"').read()
    if not 'Success' in sub:
        raise SubmissionFailed(sub)
    result = os.popen('kaggle competitions submissions -c titanic').read()
    acc = float(result.split('\n')[2].split('complete')[1].split('None')[0])
    if acc: 
        return acc
    else:
        raise Exception('Submission failed.')
