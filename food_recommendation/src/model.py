class Model:

    def __init__(self, data):
        """
        Initialize the model
        """
        self.menu = ['pizza', 'pasta', 'ramen', 'fried_rice', 'ttoeokbokki']
        self.data = data

    def recommend(self):
        """
        Recommend a food
        """
        menu_idx = max({i: self.data.count(i) for i in range(1, 6)}.items(), key=lambda x: x[1])[0] - 1
        return self.menu[menu_idx]