class Model:

    def __init__(self, data):
        """
        Initialize the model
        """
        self.menu = ['pizza', 'pasta', 'ramen', 'fried_rice', 'ttoeokbokki', 'jjiigae']
        self.data = data

    @property
    def flat_data(self):
        return [item for sublist in self.data.values() for item in sublist]

    def count_menu(self, data):
        return {i: data.count(i) for i in range(len(self.menu))}

    def preferences(self, name):
        """
        Get the preferences of the people
        """
        all_menu_count = self.count_menu(self.flat_data)
        person_menu_count = self.count_menu(self.data[name])
        return {i: person_menu_count[i] / all_menu_count[i] for i in range(len(self.menu))}

    def recommend(self, name):
        """
        Recommend a food
        """
        assert name in self.data.keys(), \
            'The name is not in the data'
        preferences = self.preferences(name)
        return self.menu[max(preferences.items(), key=lambda x: x[1])[0]]