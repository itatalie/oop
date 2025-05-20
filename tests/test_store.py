import pytest
from src.store import Product, Smartphone, LawnGrass, Category


def test_middle_price():
    category = Category("Электроника", "Телефоны и планшеты")
    product1 = Product("Телефон", "Смартфон", 30000.0, 5)
    product2 = Product("Планшет", "Дисплей 10\"", 40000.0, 3)
    category.add_product(product1)
    category.add_product(product2)

    assert category.middle_price() == (30000.0 + 40000.0) / 2


def test_middle_price_empty_category():
    empty_category = Category("Пустышка", "Без продуктов")
    assert empty_category.middle_price() == 0.0


def test_add_product_with_zero_quantity():
    with pytest.raises(ValueError):
        Product("Брак", "Описание", 1000.0, 0)


def test_add_invalid_product_to_category():
    category = Category("Электроника", "Телефоны")
    with pytest.raises(TypeError):
        category.add_product("Не продукт")


def test_smartphone_inherits_from_product():
    smartphone = Smartphone("Iphone", "Описание", 210000.0, 8, 98.2, "15", 512, "Черный")
    assert isinstance(smartphone, Product)


def test_lawn_grass_inherits_from_product():
    grass = LawnGrass("Трава", "Зеленая", 500.0, 20, "Россия", "7 дней", "Зеленый")
    assert isinstance(grass, Product)