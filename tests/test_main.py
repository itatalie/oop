import pytest
from src.store import Product, Smartphone, LawnGrass, Category


@pytest.fixture(autouse=True)
def reset_counters():
    Category.product_count = 0


def test_product_initialization():
    product = Product("Test Product", 100.0, "Test Description", 10)
    assert product.name == "Test Product"
    assert product.price == 100.0
    assert product.quantity == 10


def test_category_counters():
    product1 = Product("Product1", 10.0, "Desc1", 5)
    category1 = Category("Category1", "Description for Category1")
    category1.add_product(product1)
    assert len(category1._Category__products) == 1
    assert Category.product_count == 5


def test_duplicate_product_handling():
    category = Category("Электроника", "Описание категории")
    product1 = Product("Телефон", 10000, "Смартфон", 5)
    product2 = Product("Телефон", 12000, "Смартфон", 3)
    category.add_product(product1)
    category.add_product(product2)
    assert len(category._Category__products) == 1
    assert category._Category__products[0].quantity == 8
    assert category._Category__products[0].price == 12000
    assert Category.product_count == 5
