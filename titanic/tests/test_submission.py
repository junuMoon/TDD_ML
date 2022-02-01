import pytest

from src.uitls import submit_prediction
from src.preprocess import preprocess

from sklearn.ensemble import RandomForestClassifier

@pytest.fixture
def best_model():
    return RandomForestClassifier(oob_score=True, **{'n_estimators': 400,
                                'min_samples_split': 16,
                                'min_samples_leaf': 1,
                                'criterion': 'gini'})

@pytest.fixture(autouse=True)
def trained_model(best_model, train_data):
    train_data = preprocess(train_data)
    best_model.fit(train_data.drop(columns=['Survived']), train_data['Survived'])
    return best_model

def test_best_rf_model(trained_model, test_data):    
    test_data = preprocess(test_data, to_submit=True)
    test_data['Survived'] = trained_model.predict(test_data.drop(columns=['PassengerId']))
    acc = submit_prediction(test_data.loc[:, ['PassengerId', 'Survived']], 'rf_model')
    assert acc >= 0.8, f"{best_model.__class__.__name__} failed"