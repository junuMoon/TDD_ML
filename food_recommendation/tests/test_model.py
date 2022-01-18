from src.model import Model
import pytest

def test_model_random_selection():
    """
    Test the random selection of the food
    """
    model = Model()
    assert model.recommend() is not None