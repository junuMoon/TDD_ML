import pytest
from src.uitls import submit_prediction
from src.model import (ModelPredictAllDied,
                        ModelPredictbySex)

@pytest.mark.skip('already tested')
def test_model_predict_all_died(test_data):
    model = ModelPredictAllDied()
    test_sub = test_data.copy()
    test_sub['Survived'] = model.predict()
    acc = submit_prediction(test_sub, message='ModelPredictAllDied')
    print(acc)
    assert acc > 0.5

def test_model_predict_by_sex(test_data):
    model = ModelPredictbySex()
    test_sub = test_data.copy()
    test_sub['Survived'] = test_sub['Sex'].apply(lambda x: model.predict(x))
    acc = submit_prediction(test_sub, message='ModelWomenSurvived')
    print(acc)
    assert acc > 0.7

