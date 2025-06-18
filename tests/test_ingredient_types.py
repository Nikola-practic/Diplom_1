import pytest
from praktikum import ingredient_types


class TestIngredientsTypes:

    # Тест проверяет, что ожидаемое значение соответствует типу ингредиентов
    @pytest.mark.parametrize("ingredient_type, expected_value", [
        (ingredient_types.INGREDIENT_TYPE_SAUCE, 'SAUCE'),
        (ingredient_types.INGREDIENT_TYPE_FILLING, 'FILLING'),
    ])
    def test_ingredient_types(self, ingredient_type, expected_value):
        assert ingredient_type == expected_value

    # Тест проверяет, что типы ингредиентов являются строками
    @pytest.mark.parametrize("ingredient_type", [
        ingredient_types.INGREDIENT_TYPE_SAUCE,
        ingredient_types.INGREDIENT_TYPE_FILLING,
    ])
    def test_ingredient_types_are_strings(self, ingredient_type):
        assert isinstance(ingredient_type, str)
