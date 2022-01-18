class Model:

    def __init__(self, data):
        """
        Initialize the model
        """
        self.menu = ['pizza', 'pasta', 'ramen', 'fried_rice', 'ttoeokbokki']
        self.data = data

    def recommend(self, name):
        """
        Recommend a food
        """
        assert name in self.data.keys(), \
            'The name is not in the data'
        menu_idx = max({i: self.data[name].count(i) for i in range(1, 6)}.items(), key=lambda x: x[1])[0] - 1
        return self.menu[menu_idx]