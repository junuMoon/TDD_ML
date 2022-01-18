from src.model import Model
import pytest
import random

@pytest.fixture
def one_person_data():
    """
    Fixture for a one person data
    """
    return [random.randint(1, 5) for _ in range(10)]

def test_model_random_selection(one_person_data):
    """
    Test the random selection of the food
    """
    model = Model(one_person_data)
    assert model.recommend() is not None