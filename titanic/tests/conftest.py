import pytest
from pathlib import Path
import os

import pandas as pd

path = Path(os.path.dirname(__file__))
data_dir = path.absolute().parent / 'data'

@pytest.fixture(scope='module')
def train_data():
    return pd.read_csv(data_dir / 'train.csv')

@pytest.fixture(scope='module')
def test_data():
    return pd.read_csv(data_dir / 'test.csv')
