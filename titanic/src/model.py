class ModelPredictAllDied:
    def predict(self):
        return 0

class ModelPredictbySex:
    def predict(self, sex):
        if sex == 'male':
            return 0
        elif sex == 'female':
            return 1