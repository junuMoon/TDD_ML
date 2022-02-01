import pytest
from pathlib import Path
import os

import pandas as pd

path = Path(os.path.dirname(__file__))
data_dir = path.absolute().parent / 'data' 
raw_dir = data_dir / 'raw'

from src.preprocess import preprocess
from sklearn.model_selection import train_test_split

@pytest.fixture
def cat_vars():
    return ['Pclass', 'Sex', 'Embarked', 'Cabin', 'Alone', 'Title']

@pytest.fixture
def num_vars():
    return ['Age', 'SibSp', 'Parch', 'Fare']

@pytest.fixture(scope='module')
def train_data():
    return pd.read_csv(raw_dir / 'train.csv')

@pytest.fixture(scope='module')
def test_data():
    return pd.read_csv(raw_dir / 'test.csv')

@pytest.fixture(scope='module')
def dataset(train_data):
    dataset = preprocess(train_data)
    return train_test_split(dataset.drop(columns=['Survived']),
                            dataset['Survived'],
                             test_size=0.3, random_state=531)