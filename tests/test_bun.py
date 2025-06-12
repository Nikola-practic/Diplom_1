import pytest
from praktikum.bun import Bun

class TestBun:

    # Тест проверяет, что булочке можно дать название
    @pytest.mark.parametrize("name, price", [
        ("black bun", 100),
        ("white bun", 200),
        ("red bun", 300)
    ])
    def test_bun_get_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    # Тест проверяет, что булочке можно назначить цену
    @pytest.mark.parametrize("name, price", [
        ("black bun", 100),
        ("white bun", 200),
        ("red bun", 300)
    ])
    def test_bun_get_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price



