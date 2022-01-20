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
        return {menu: data.count(i) for i, menu in enumerate(self.menu) if data.count(i) > 0}

    def preferences(self, name):
        """
        Get the preferences of the people
        """
        all_menu_count = self.count_menu(self.flat_data)
        person_menu_count = self.count_menu(self.data[name])
        return {menu: person_menu_count.get(menu, 0) / one_menu_count \
                for menu, one_menu_count in all_menu_count.items()}

    def recommend(self, name):
        """
        Recommend a food
        """
        assert name in self.data.keys(), \
            'The name is not in the data'
        preferences = self.preferences(name)
        return sorted(preferences.items(), key=lambda x: x[1], reverse=True)[0][0]