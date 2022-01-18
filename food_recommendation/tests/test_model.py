from src.model import Model
import pytest
import random

@pytest.fixture
def one_person_data():
    """
    Fixture for a one person data
    """
    return [random.randint(0, 5) for _ in range(10)]

def test_model_recommend_food(one_person_data):
    """
    Test the random selection of the food
    """
    model = Model(one_person_data)
    assert type(model.recommend()) == str

def test_model_recommend_most_common(one_person_data):
    """
    Test the recommendation of the most common food
    """
    model = Model(one_person_data)
    most_common = model.menu[max({i: one_person_data.count(i) for i in range(0, 5)}.items(), key=lambda x: x[1])[0] - 1]
    assert model.recommend() == most_common

@pytest.fixture
def two_person_data():
    """
    Fixture for a two person data
    """
    data = {'Jason': [random.randint(0, 5) for _ in range(5)],
            'Kim': [random.randint(0, 5) for _ in range(5)]}
    for _ in range(5):
        data['Jason'].append(1)
        data['Kim'].append(5)

    return data

def test_model_recommend_food(two_person_data):
    """
    Test the random selection of the food
    """
    model = Model(two_person_data)
    assert type(model.recommend('Jason')) == str

def test_model_recommend_most_common(two_person_data):
    """
    Test the recommendation of the most common food
    """
    model = Model(two_person_data)
    assert model.recommend('Jason') == 'pasta'

@pytest.fixture
def ten_people_data():
    """
    Fixture for a ten person data
    """
    return {'Jason': [random.randint(0, 5) for _ in range(10)],
            'Kim': [random.randint(0, 5) for _ in range(10)],
            'Linda': [random.randint(0, 5) for _ in range(10)],
            'Mason': [random.randint(0, 5) for _ in range(10)],
            'Nathan': [random.randint(0, 5) for _ in range(10)],
            'Olivia': [random.randint(0, 5) for _ in range(10)],
            'Pam': [random.randint(0, 5) for _ in range(10)],
            'Quinn': [random.randint(0, 5) for _ in range(10)],
            'Riley': [random.randint(0, 5) for _ in range(10)],
            'Sam': [random.randint(0, 5) for _ in range(10)]}


def test_model_recommend_his_favorite_menu(ten_people_data):
    """
    Test model recommend his favorite menu
    favorite menu is calculated by the most common food / the number all people choice that menu
    """
    model = Model(ten_people_data)
    menu_count_1dim = {i: ten_people_data['Jason'].count(i) for i in range(0, 5)}
    flat_data = []
    [flat_data.extend(data) for data in ten_people_data.values()]
    menu_count_2dim = {i: flat_data.count(i) for i in range(0, 5)}
    favorite_menu_idx = max({i: menu_count_1dim[i] / menu_count_2dim[i] for i in range(0, 5)}.items(), key=lambda x: x[1])[0] - 1
    assert model.recommend('Jason') == model.menu[favorite_menu_idx]
