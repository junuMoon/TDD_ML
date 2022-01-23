import pytest
import pandas as pd

from src.uitls import get_null_pcnt

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

def test_categorical_columns(cat_vars, train_data):
    assert cat_vars == ['Pclass', 'Sex', 'SibSp', 'Parch', 'Embarked']

def test_cat_cols_trgt_var_pcnt(cat_vars, train_data):
    cat_vars_trgt_pcnt = {}
    for c in cat_vars:
        frec_tbl = pd.crosstab(train_data[c], train_data.Survived, normalize='index').round(4).to_dict()
        cat_vars_trgt_pcnt[c] = {k: round(v * 100, 1) for k, v in frec_tbl[1].items()}
    assert True

def test_most_passengers_were_alone(train_data):
    no_parch = train_data.Parch == 0
    no_sibsp = train_data.SibSp == 0
    assert train_data.loc[no_parch&no_sibsp].shape[0] == 537