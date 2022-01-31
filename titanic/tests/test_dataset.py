import pytest
import pandas as pd

from src.uitls import get_null_pcnt
from src.preprocess import preprocess

def test_dataset_size(train_data, test_data):
    assert train_data.shape[0] == 891
    assert test_data.shape[0] == 418

def test_null_percentage(train_data):
    null_pcnt = get_null_pcnt(train_data)
    assert {col for col, pcnt in null_pcnt.items() if pcnt > 0} == \
                                            set(['Embarked', 'Age', 'Cabin'])

def test_target_columns(train_data):
    target = 'Survived'
    assert target in train_data.columns
    assert train_data[target].unique().shape[0] == 2
    assert list(train_data[target].unique()) == [0, 1]
    assert train_data[target].value_counts()[0] == 549
    assert train_data[target].value_counts()[1] == 342

def test_dataset_has_alone_col(train_data):
    train_data = preprocess(train_data)
    assert 'Alone' in train_data.columns
    assert train_data['Alone'].unique().shape[0] == 2

def test_cabin_col_grouped_by_first_letter(train_data):
    train_data = preprocess(train_data)
    assert isinstance(train_data.iloc[0]['Cabin'], str)
    assert len(train_data.iloc[0]['Cabin']) == 1

def test_impute(train_data):
    train_data = preprocess(train_data)
    assert train_data.isna().sum().sum() == 0