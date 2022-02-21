# Model

## First Implementation
- LinearRegression: Failed, 0.4
- LogisticRegression: Passed, 0.81
- Perceptron: Failed, 0.72
- SGDClassfifer: Passed, 0.80
- RandomForestClassifier: Passed, 0.80
- KNeighborsClassifier: Failed, 0.67
- SVC: Failed, 0.65
- LinearSVC: Passed, 0.80
- GaussianNB: Passed, 0.80

## RandomForest
- No accuracy increase found in RandomForestClassifier trained with selected feature
   - both accuracy 0.8
- Via RandomizedSearchCV, accuracy increased to 0.82
   - n_estimators: 400
   - min_samples_split: 16
   - min_samples_leaf: 1
   - criterion: gini
- Confusion Matrix
    - TP: 58
    - FP: 14
    - FN: 15
    - TN: 91
- acc: 0.83
- prec: 0.80
- rec: 0.78
- f1: 0.79
- Kaggle score: 0.77990