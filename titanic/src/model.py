class ModelPredictAllDied:
    def predict(self, X):
        return 0

class ModelPredictbySex:
    def predict(self, sex):
        return not sex

class ModelSexPclassEmbarked:

    def __init__(self) -> None:
        self.sex = {1: -3, 0: +2}
        self.embarked = {2:-1, 0: 0, 1: +1}
        self.pclass = {0: +2, 1: 0, 2: -2}

    def predict(self, sex, embarked, pclass):
        return self.sex[sex] + self.embarked[embarked] + self.pclass[pclass] >= 0
