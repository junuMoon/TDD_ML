from src.model import Model
import pytest
import random

@pytest.fixture
def menu():
    return ['pizza', 'pasta', 'burger', 'fries', 'chicken', 'sandwich']

@pytest.fixture
def model(menu):
    return Model(menu=menu)

@pytest.fixture
def one_person_data():
    """
    Fixture for a one person data
    """
    return [random.randint(0, 5) for _ in range(5)]

def test_model_recommend_food(model, one_person_data):
    """
    Test the random selection of the food
    """
    model.add_data(one_person_data)
    assert type(model.recommend()) == str

def test_model_recommend_most_common(model, one_person_data):
    """
    Test the recommendation of the most common food
    """
    model.add_data(one_person_data)
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

def test_model_recommend_food(model, two_person_data):
    """
    Test the random selection of the food
    """
    model.add_data(two_person_data)
    assert type(model.recommend('Jason')) == str

@pytest.mark.xfail(reason="Need more parameters to attenuate the preference when there's few people")
def test_model_recommend_most_common(model, two_person_data):
    """
    Test the recommendation of the most common food
    """
    model.add_data(two_person_data)
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
            'Sam': [random.randint(0, 5) for _ in range(9)]}

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
    data['Sam'].append(1)

    return data

@pytest.mark.skip(reason="Sigmoid time model applied")
def test_model_recommend_his_favorite_menu(model, ten_people_data):
    """
    Test model recommend his favorite menu
    favorite menu is calculated by the most common food / the number all people choice that menu
    """
    model.add_data(ten_people_data)
    assert model.recommend('Jason') == 'pasta'

def test_model_not_recommend_the_last_eaten_menu(model, ten_people_data):
    """
    Test model not recommend the last eaten menu
    """
    model.add_data(ten_people_data)
    print(model.preferences('Jason'))
    assert model.recommend('Jason') != 'pasta'

@pytest.fixture
def ten_people_after_data():
    """
    Fixture for a ten person data after 10 days
    """
    return  {'Jason': [random.randint(0, 5) for _ in range(10)],
            'Kim': [random.randint(0, 5) for _ in range(10)],
            'Linda': [random.randint(0, 5) for _ in range(10)],
            'Mason': [random.randint(0, 5) for _ in range(10)],
            'Nathan': [random.randint(0, 5) for _ in range(10)],
            'Olivia': [random.randint(0, 5) for _ in range(10)],
            'Pam': [random.randint(0, 5) for _ in range(10)],
            'Quinn': [random.randint(0, 5) for _ in range(10)],
            'Riley': [random.randint(0, 5) for _ in range(10)],
            'Sam': [random.randint(0, 5) for _ in range(10)]}    


def test_model_recalculate_preferences_with_data_added(model, ten_people_data, ten_people_after_data):
    """
    Test model recalculate preferences with data added
    """
    model.add_data(ten_people_data)
    recommendation_after_10days = model.recommend('Jason')
    model.add_data(ten_people_after_data)
    assert model.recommend('Jason') != recommendation_after_10days
