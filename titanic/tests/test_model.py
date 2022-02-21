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

@pytest.mark.skip(reason="can't run because category encodded in frequency")
def test_model_predict_by_sex(dataset):
    X_train, X_test, y_train, y_test = dataset
    model = ModelPredictbySex()
    y_pred = [model.predict(s) for s in X_test['Sex'].values]
    acc = (y_pred == y_test).mean()
    assert acc >= 0.6, f"{model.__class__.__name__} failed"

@pytest.mark.skip(reason="can't run because category encodded in frequency")
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
from sklearn.metrics import f1_score

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

def pytest_configure():
    pytest.base_model = 0.0

def test_base_model(dataset):
    X_train, X_test, y_train, y_test = dataset
    model = RandomForestClassifier(n_estimators=100, oob_score=True)
    model.fit(X_train, y_train)
    score = f1_score(y_test, model.predict(X_test))
    assert score > 0.7, f"base model failed"
    pytest_configure.base_model = score

@pytest.mark.skip('No difference found')
def test_random_forest_drop_unimportant_feature(dataset):
    X_train, X_test, y_train, y_test = dataset
    X_train = X_train.drop(columns=['Alone'])
    X_test = X_test.drop(columns=['Alone'])
    model = RandomForestClassifier(n_estimators=100, oob_score=True)
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)
    assert score > pytest_configure.base_model, "Model trained with selected feature score is not better than original"
    pytest_configure.drop_model = score

from sklearn.model_selection import StratifiedKFold, RandomizedSearchCV

def test_best_rf_model(dataset):
    X_train, X_test, y_train, y_test = dataset
    params = {
            'max_depth': [3, 4, 5],
            'n_estimators': [100, 200, 300],
            'n_jobs': [-1],
            }
    model = RandomForestClassifier()
    random_search = RandomizedSearchCV(model, params, cv=StratifiedKFold(n_splits=10, shuffle=True),
                                        scoring='f1', n_jobs=-1, verbose=1)
    random_search.fit(X_train, y_train)
    score = random_search.best_score_

    pytest_configure.best_model = score
    pytest_configure.rf = random_search.best_estimator_
    print(f"{model.__class__.__name__} score: {score}")
    print(f"{model.__class__.__name__} best params: {random_search.best_params_}")
    
    assert score > pytest_configure.base_model, f"{model.__class__.__name__} failed"


@pytest.fixture
def age_categorization(train_data):
    train_data['Age_bin'] = train_data['Age'].apply(lambda age: age // 10)
    return train_data

@pytest.mark.skip('No difference found')
def test_age_categorization_improves_acc(random_forest_best_param, train_data, age_categorization, dataset):
    X_train, X_test, y_train, y_test = dataset
    model = random_forest_best_param
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)
    assert score > pytest_configure.best_model, f"{model.__class__.__name__} failed"

from xgboost import XGBClassifier

@pytest.mark.skip('No difference found')
def test_xgb_model(dataset):
    X_train, X_test, y_train, y_test = dataset
    model = XGBClassifier(n_estimators=100, learning_rate=0.1, max_depth=3, n_jobs=-1)
    model.fit(X_train, y_train)
    score = f1_score(y_test, model.predict(X_test))
    assert score > pytest_configure.best_model, f"{model.__class__.__name__} has no improvement than random forests"
    print(f"{model.__class__.__name__} score: {score}")


@pytest.mark.skip('No difference found')
def test_tuned_xgb_model(dataset):
    X_train, X_test, y_train, y_test = dataset
    params = {
            'max_depth': [3, 4, 5],
            'learning_rate': [0.1, 0.05, 0.01],
            'n_estimators': [100, 200, 300],
            'n_jobs': [-1],
            }
    model = XGBClassifier(use_label_encoder=False, eval_metric='logloss')
    random_search = RandomizedSearchCV(model, params, cv=StratifiedKFold(n_splits=10, shuffle=True),
                                        scoring='f1', n_jobs=-1, verbose=1)
    random_search.fit(X_train, y_train)
    score = random_search.best_score_
    # import pdb; pdb.set_trace()
    assert score > pytest_configure.best_model, f"{model.__class__.__name__} has no improvement than random forests"
    print(f"{model.__class__.__name__} score: {score}")
    print(f"{model.__class__.__name__} best params: {random_search.best_params_}")

from pytorch_tabnet.tab_model import TabNetClassifier
from pytorch_tabnet.pretraining import TabNetPretrainer
from pytorch_tabnet.metrics import Metric
from torch.nn import functional as F
import torch.optim as optim

@pytest.fixture
def tabnet_pretrained(dataset):
    X_train, X_test, y_train, y_test = dataset
    pretrain_model = TabNetPretrainer()
    pretrain_model.fit(
        X_train=X_train,
        eval_set=[X_test],
        pretraining_ratio=0.8,
    )

def test_tabnet_accuracy_gt_rf(tabnet_pretrained, dataset):
    X_train, X_test, y_train, y_test = dataset
    EPOCH = 20
    BATCH_SIZE = 8
    model = TabNetClassifier()
    model.fit(X_train, y_train,
            eval_set=[(X_test, y_test)],
            max_epochs=EPOCH,
            batch_size=BATCH_SIZE,
            patience=500,
            from_unsupervised=tabnet_pretrained
    )
    tb_score = f1_score(y_test, model.predict(X_test))
    rf_score = f1_score(y_test, pytest_configure.rf.predict(X_test))
    pytest_configure.tb = model
    assert tb_score > rf_score, "TabNet model is not better than Random Forest"

import numpy as np

def test_ensemble_tabnet_rf_hard_vt(dataset):
    X_train, X_test, y_train, y_test = dataset
    estimators=[pytest_configure.tb, pytest_configure.rf]

    Y = np.zeros([X_test.shape[0], len(estimators)], dtype=int)
    for i, clf in enumerate(estimators):
        Y[:, i] = clf.predict(X_test)
    y = np.zeros(X_test.shape[0], dtype=int)
    for i in range(X_test.shape[0]):
        y[i] = np.argmax(np.bincount(Y[i, :]))
    
    vt_score = f1_score(y_test, y)
    rf_score = f1_score(y_test, pytest_configure.rf.predict(X_test))
    
    assert vt_score > rf_score, "Voting Classifier(hard) is not better than Random Forest"

def test_ensemble_tabnet_rf_soft_vt(dataset):
    X_train, X_test, y_train, y_test = dataset
    rf_prob = pytest_configure.rf.predict_proba(X_test)
    tb_prob = pytest_configure.tb.predict_proba(X_test)
    vt_prob = rf_prob * tb_prob
    vt_pred = np.argmax(vt_prob, axis=1)
    rf_score = f1_score(y_test, pytest_configure.rf.predict(X_test))
    vt_score = f1_score(y_test, vt_pred)

    assert vt_score > rf_score, "Voting Classifier(soft) is not better than Random Forest"
