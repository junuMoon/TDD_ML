from operator import sub
import pytest
from src.uitls import submit_prediction
from src.model import ModelPredictAllDied

def test_model_predict_all_died(test_data):
    model = ModelPredictAllDied()
    test_sub = test_data.copy()
    test_sub['Survived'] = model.predict()
    acc = submit_prediction(test_sub, message=' - ModelPredictAllDied')
    print(acc)
    assert acc > 0.5
