import pytest
from praktikum.burger import Burger


class TestBurger:

    # Тест проверяет модель бургера без булок и ингредиентов
    def test_burger_create(self):
        burger = Burger()
        assert burger.bun is None
        assert len(burger.ingredients) == 0


    # Тест проверяет модель бургера только с булкой
    def test_set_buns(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun


    # Тест проверяет модель бургера с добавлением ингредиента
    def test_add_ingredient(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients[0] == mock_ingredient


    # Тест проверяет удаление ингредиента
    def test_remove_ingredient(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0


    # Тест проверяет перемешивание ингредиентов
    def test_move_ingredient(self, mock_ingredient, mock_second_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_second_ingredient)

        # Перемещаем второй ингредиент на первое место
        burger.move_ingredient(1, 0)
        assert burger.ingredients[0] == mock_second_ingredient
        assert burger.ingredients[1] == mock_ingredient


    # Тест проверяет добавление цены ингредиента в чек
    def test_get_price(self, bun_1, ingredient_1, ingredient_2):
        burger = Burger()
        burger.set_buns(bun_1)
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        sum_price = bun_1.price * 2 + ingredient_1.price + ingredient_2.price

        # Проверяем общую цену (булочка * 2 + ингредиенты)
        assert burger.get_price() == sum_price


    # Тест проверяет возможность распечатать чек о бургере
    def test_get_receipt(self, bun_1, ingredient_1, ingredient_2):
        burger = Burger()
        burger.set_buns(bun_1)
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)
        expected_receipt = (
            f"(==== {bun_1.name} ====)\n"
            f"= {str(ingredient_1.type).lower()} {ingredient_1.name} =\n"
            f"= {str(ingredient_2.type).lower()} {ingredient_2.name} =\n"
            f"(==== {bun_1.name} ====)\n"
            f"\nPrice: {bun_1.price * 2 + ingredient_1.price + ingredient_2.price}"
        )
        assert burger.get_receipt() == expected_receipt


