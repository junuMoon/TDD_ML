from src.model import Model
import pytest
import random

@pytest.fixture
def one_person_data():
    """
    Fixture for a one person data
    """
    return [random.randint(1, 5) for _ in range(10)]

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
    print(one_person_data)
    most_common = model.menu[max({i: one_person_data.count(i) for i in range(1, 6)}.items(), key=lambda x: x[1])[0] - 1]
    assert model.recommend() == most_common

@pytest.fixture
def two_person_data():
    """
    Fixture for a two person data
    """
    return {'Jason': [random.randint(1, 5) for _ in range(10)],
            'Kim': [random.randint(1, 5) for _ in range(10)]}

