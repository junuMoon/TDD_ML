import pytest
import pandas as pd

from src.uitls import get_null_pcnt

@pytest.mark.xfail(reason="'Embarked', 'Age', 'Cabin' needs to be imputed.")
def test_null_percentage(train_data):
    null_pcnt = get_null_pcnt(train_data)
    assert False
