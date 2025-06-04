import pytest
from src.store import Product, Smartphone, LawnGrass, Category


def test_price_validation():
    with pytest.raises(TypeError):
        Product("Ошибка", "Строка вместо цены", "строка", 10)

    with pytest.raises(ValueError):
        Product("Ошибка", "Цена 0", 0, 10)

    with pytest.raises(ValueError):
        Product("Ошибка", "Отрицательная цена", -100, 10)


def test_category_add_product():
    Category.category_count = 0
    Category.product_count = 0

    category = Category("Смартфоны", "Высокотехнологичные смартфоны")
    product1 = Product("Iphone", "Флагман", 210000.0, 8)
    product2 = Product("Samsung", "Флагман", 180000.0, 5)
    category.add_product(product1)
    category.add_product(product2)

    assert len(category._Category__products) == 2
    assert Category.category_count == 1
    assert Category.product_count == 2


def test_duplicate_handling():
    Category.category_count = 0
    Category.product_count = 0

    category = Category("Электроника", "Описание категории")
    product1 = Product("Телефон", "Смартфон", 30000.0, 10)
    product2 = Product("Телефон", "Обновленное описание", 35000.0, 5)
    category.add_product(product1)
    category.add_product(product2)

    assert len(category._Category__products) == 1
    assert category._Category__products[0].quantity == 15
    assert category._Category__products[0].price == 35000.0
    assert Category.product_count == 1


def test_middle_price():
    category = Category("Электроника", "Телефоны и планшеты")
    product1 = Product("Телефон", "Смартфон", 30000.0, 10)
    product2 = Product("Планшет", "Дисплей", 40000.0, 3)
    category.add_product(product1)
    category.add_product(product2)

    assert category.middle_price() == (30000 + 40000) / 2