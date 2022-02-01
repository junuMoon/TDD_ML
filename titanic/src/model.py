class ModelPredictAllDied:
    def predict(self, X):
        return 0

class ModelPredictbySex:
    def predict(self, sex):
        if sex == 'male':
            return 0
        elif sex == 'female':
            return 1

class ModelSexPclassEmbarked:

    def __init__(self) -> None:
        self.sex = {'male': -3, 'female': +2}
        self.embarked = {'S':-1, 'C': 0, 'Q': +1}
        self.pclass = {1: +2, 2: 0, 3: -2}

    def predict(self, sex, embarked, pclass):
        return self.sex[sex] + self.embarked[embarked] + self.pclass[pclass] >= 0
