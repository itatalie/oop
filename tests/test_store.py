import pytest
from src.store import Product, Category


@pytest.fixture(autouse=True)
def reset_counters():
    """
    Сбрасывает глобальные счетчики перед каждым тестом.
    """
    Category.product_counter = 0


def test_product_initialization():
    """Проверка инициализации продукта."""
    product = Product("Test Product", 100.0, "Test Description", 10)
    assert product.name == "Test Product"
    assert product.price == 100.0
    assert product.quantity == 10


def test_product_string_representation():
    """Проверка строкового представления продукта."""
    product = Product("Test Product", 100.0, "Test Description", 10)
    assert str(product) == "Test Product, 100.0 руб. Остаток: 10 шт."


def test_category_initialization():
    """Проверка инициализации категории."""
    category = Category("Test Category", "Description")
    assert category.name == "Test Category"
    assert category.description == "Description"


def test_category_add_product():
    """Проверка добавления продукта в категорию."""
    category = Category("Test Category", "Description")
    product1 = Product("Product1", 10.0, "Desc1", 5)
    category.add_product(product1)

    assert len(category._Category__products) == 1
    assert Category.product_counter == 1


def test_category_string_representation():
    """Проверка строкового представления категории."""
    category = Category("Test Category", "Description")
    product1 = Product("Product1", 10.0, "Desc1", 5)
    product2 = Product("Product2", 20.0, "Desc2", 3)
    category.add_product(product1)
    category.add_product(product2)

    assert str(category) == "Test Category, количество продуктов: 8 шт."


def test_product_addition():
    """Проверка магического метода сложения для продуктов."""
    product1 = Product("Product1", 10.0, "Desc1", 5)
    product2 = Product("Product2", 20.0, "Desc2", 3)

    total_cost = product1 + product2
    assert total_cost == 110.0, "Сумма стоимостей товаров рассчитана некорректно."


def test_product_addition_with_invalid_type():
    """Проверка сложения продукта с объектом другого типа."""
    product = Product("Product1", 10.0, "Desc1", 5)
    with pytest.raises(TypeError):
        product + "Неверный тип"


def test_duplicate_product_handling():
    """Проверка обработки дубликатов при добавлении продукта."""
    category = Category("Test Category", "Description")
    product1 = Product("Product1", 10.0, "Desc1", 5)
    product2 = Product("Product1", 15.0, "Desc2", 3)

    category.add_product(product1)
    category.add_product(product2)

    assert len(category._Category__products) == 1
    assert category._Category__products[0].quantity == 8
    assert category._Category__products[0].price == 15.0
    assert Category.product_counter == 1