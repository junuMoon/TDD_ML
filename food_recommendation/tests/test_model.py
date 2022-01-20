from src.model import Model
import pytest
import random

@pytest.fixture
def one_person_data():
    """
    Fixture for a one person data
    """
    return [random.randint(0, 5) for _ in range(5)]

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
    print(model.preferences('Jason'))
    assert model.recommend('Jason') == 'pasta'
    # When Two person is there, if one person choose a food one time,
    # The preference will be 1 / 1 = 1.0
    # Need more parameters to attenuate the preference

@pytest.fixture
def ten_people_data():
    """
    Fixture for a ten person data
    """
    data = {'Jason': [random.randint(0, 5) for _ in range(10)],
            'Kim': [random.randint(0, 5) for _ in range(5)],
            'Linda': [random.randint(0, 5) for _ in range(5)],
            'Mason': [random.randint(0, 5) for _ in range(5)],
            'Nathan': [random.randint(0, 5) for _ in range(5)],
            'Olivia': [random.randint(0, 5) for _ in range(5)],
            'Pam': [random.randint(0, 5) for _ in range(5)],
            'Quinn': [random.randint(0, 5) for _ in range(5)],
            'Riley': [random.randint(0, 5) for _ in range(5)],
            'Sam': [random.randint(0, 5) for _ in range(5)]}

    for _ in range(5):
        data['Jason'].append(1)
        data['Kim'].append(0)
        data['Linda'].append(2)
        data['Mason'].append(3)
        data['Nathan'].append(4)
        data['Olivia'].append(5)
        data['Pam'].append(4)
        data['Quinn'].append(3)
        data['Riley'].append(2)
        data['Sam'].append(0)

    return data

def test_model_recommend_his_favorite_menu(ten_people_data):
    """
    Test model recommend his favorite menu
    favorite menu is calculated by the most common food / the number all people choice that menu
    """
    model = Model(ten_people_data)
    assert model.recommend('Jason') == 'pasta'
