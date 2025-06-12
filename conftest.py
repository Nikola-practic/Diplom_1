import pytest
from unittest.mock import Mock
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE

@pytest.fixture
def mock_bun():
    mock = Mock()
    mock.get_bun.return_value = "Test bum"
    return mock

@pytest.fixture
def mock_ingredient():
    mock = Mock()
    mock.get_ingredient.return_value = "Test ingredient"
    return mock

@pytest.fixture
def mock_second_ingredient():
    mock = Mock()
    mock.get_ingredient.return_value = "Test second ingredient"
    return mock

@pytest.fixture
def bun_1():
    bun_1 = Bun("white bun", 200)
    return bun_1

@pytest.fixture()
def ingredient_1():
    ingredient_1 = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100)
    return ingredient_1

@pytest.fixture()
def ingredient_2():
    ingredient_2 = Ingredient(INGREDIENT_TYPE_SAUCE, "chili sauce", 300)
    return ingredient_2



