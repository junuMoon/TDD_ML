from statistics import LinearRegression
import pytest

from src.uitls import submit_prediction
from src.model import (ModelPredictAllDied,
                        ModelPredictbySex,
                        ModelSexPclassEmbarked)

def test_model_predict_all_died(dataset):
    X_train, X_test, y_train, y_test = dataset
    model = ModelPredictAllDied()
    y_pred = model.predict(X_test)
    acc = (y_pred == y_test).mean()
    assert acc >= 0.5, f"{model.__class__.__name__} failed"

def test_model_predict_by_sex(dataset):
    X_train, X_test, y_train, y_test = dataset
    model = ModelPredictbySex()
    y_pred = [model.predict(s) for s in X_test['Sex'].values]
    acc = (y_pred == y_test).mean()
    assert acc >= 0.6, f"{model.__class__.__name__} failed"

def test_model_predict_by_sex_pclass_embarked(dataset):
    X_train, X_test, y_train, y_test = dataset
    model = ModelSexPclassEmbarked()
    y_pred = [model.predict(*s) for s in zip(X_test['Sex'], X_test['Embarked'], X_test['Pclass'])]
    acc = (y_pred == y_test).mean()
    assert acc >= 0.7, f"{model.__class__.__name__} failed"


from sklearn.linear_model import (LinearRegression,
                                    LogisticRegression,
                                    Perceptron,
                                    SGDClassifier,
)
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import (SVC,
                        LinearSVC,)
from sklearn.naive_bayes import GaussianNB
    
@pytest.mark.parametrize('model', [LinearRegression(),
                                    LogisticRegression(),
                                    Perceptron(),
                                    SGDClassifier(),
                                    RandomForestClassifier(),
                                    KNeighborsClassifier(),
                                    SVC(),
                                    LinearSVC(),
                                    GaussianNB(),
                                    ])
def test_model(model, dataset):
    X_train, X_test, y_train, y_test = dataset
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)
    print(f"{model.__class__.__name__} score: {score}")
    assert score >= 0.7, f"{model.__class__.__name__} failed"