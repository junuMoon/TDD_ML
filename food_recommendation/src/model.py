from enum import Enum

class Menu(Enum):
    """
    Enum for the different menus
    """
    pizza = 1
    pasta = 2
    ramen = 3
    fried_rice = 4
    ttoeokbokki = 5

class Model:

    def __init__(self, data):
        """
        Initialize the model
        """
        self.data = data

    def recommend(self):
        """
        Recommend a food
        """
        return max({i: self.data.count(i) for i in range(1, 6)}.items(), key=lambda x: x[1])[0]