import pytest
from src.store import Product, Category


def test_product_price():
    """Проверка геттера и сеттера цены."""
    product = Product("Телефон", 10000, "Смартфон", 5)
    assert product.price == 10000, "Геттер цены работает некорректно."

    product.price = 15000
    assert product.price == 15000, "Сеттер цены работает некорректно."

    product.price = -5000
    assert product.price == 15000, "Цена не должна изменяться при отрицательном значении."


def test_category_add_product():
    """Проверка добавления продукта в категорию."""
    category = Category("Электроника")
    product = Product("Ноутбук", 50000, "Ультрабук", 3)

    category.add_product(product)
    assert len(category._Category__products) == 1, "Продукт не был добавлен в категорию."

    with pytest.raises(TypeError):
        category.add_product("Не продукт")


def test_category_products_getter():
    """Проверка геттера для списка товаров."""
    category = Category("Электроника")
    product1 = Product("Телефон", 10000, "Смартфон", 5)
    product2 = Product("Наушники", 2000, "Беспроводные", 10)

    category.add_product(product1)
    category.add_product(product2)

    expected_output = (
        "Телефон, 10000 руб. Остаток: 5 шт.\n"
        "Наушники, 2000 руб. Остаток: 10 шт."
    )
    assert category.products == expected_output, "Геттер списка товаров работает некорректно."


def test_new_product_classmethod():
    """Проверка класс-метода new_product."""
    product_data = {
        "name": "Планшет",
        "price": 25000,
        "description": "Планшет для работы",
        "quantity": 2,
    }
    product = Product.new_product(product_data)
    assert product.name == "Планшет", "Имя продукта не соответствует ожидаемому."
    assert product.price == 25000, "Цена продукта не соответствует ожидаемой."


def test_duplicate_product_handling():
    """Проверка обработки дубликатов продуктов."""
    category = Category("Электроника")
    product1 = Product("Телефон", 10000, "Смартфон", 5)
    product2 = Product("Телефон", 12000, "Смартфон", 3)

    category.add_product(product1)
    category.add_product(product2)

    assert len(category._Category__products) == 1, "Дубликаты не были объединены."
    assert category._Category__products[0].quantity == 8, "Количество не было обновлено."
    assert category._Category__products[0].price == 12000, "Цена не была обновлена."