from math import floor
from src.utils import sigmoid

class Model:

    def __init__(self, menu, data=None):
        """
        Initialize the model
        """
        self.menu = menu
        self.data = data if data else {}

    def add_data(self, data):
        self.data = data

    def count_last_eaten(self, data, days=7):
        """
        Count the last eaten days
        """
        self.scale_num = floor(days/2)
        data = data[:-days:-1]
        count_days = {}
        for i, menu in enumerate(self.menu):
            try:
                count_days[menu] = data.index(i) - self.scale_num
            except ValueError:
                count_days[menu] = days
        return count_days

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
        last_eaten_days = self.count_last_eaten(self.data[name])
        return {menu: person_menu_count.get(menu, 0) * sigmoid(last_eaten_days[menu], self.scale_num) \
                                                        / one_menu_count \
                                for menu, one_menu_count in all_menu_count.items()}

    def recommend(self, name):
        """
        Recommend a food
        """
        assert name in self.data.keys(), \
            'The name is not in the data'
        preferences = self.preferences(name)
        return sorted(preferences.items(), key=lambda x: x[1], reverse=True)[0][0]