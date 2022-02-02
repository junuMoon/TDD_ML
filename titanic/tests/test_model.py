from statistics import LinearRegression
import pytest

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

@pytest.mark.skip('Already tested')
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
def test_various_model_performance(model, dataset):
    X_train, X_test, y_train, y_test = dataset
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)
    print(f"{model.__class__.__name__} score: {score}")
    assert score >= 0.7, f"{model.__class__.__name__} failed"

@pytest.mark.skip('No difference found')
def test_random_forest_drop_unimportant_feature(dataset):
    X_train, X_test, y_train, y_test = dataset
    model_orig = RandomForestClassifier(n_estimators=100, oob_score=True)
    model_orig.fit(X_train, y_train)
    score_orig = model_orig.score(X_test, y_test)
    print(f"{model_orig.__class__.__name__} score: {score_orig}")
    print(f"{model_orig.__class__.__name__} oob score: {model_orig.oob_score_}")
    assert score_orig >= 0.8, f"{model_orig.__class__.__name__} failed"

    X_train = X_train.drop(columns=['Alone'])
    X_test = X_test.drop(columns=['Alone'])
    model = RandomForestClassifier(n_estimators=100, oob_score=True)
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)
    print(f"{model.__class__.__name__} score: {score}")
    print(f"{model.__class__.__name__} oob score: {model.oob_score_}")
    assert score > score_orig, "Model trained with selected feature score is not better than original"

@pytest.fixture
def random_forest_best_param():
    return RandomForestClassifier(oob_score=True, **{'n_estimators': 400,
                                'min_samples_split': 16,
                                'min_samples_leaf': 1,
                                'criterion': 'gini'})

def test_best_rf_model(random_forest_best_param, dataset):
    X_train, X_test, y_train, y_test = dataset
    model = random_forest_best_param
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)
    print(f"{model.__class__.__name__} score: {score}")
    print(f"{model.__class__.__name__} oob score: {model.oob_score_}")
    assert score > 0.8, f"{model.__class__.__name__} failed"