import pytest
from src.main import Product, Category


@pytest.fixture(autouse=True)
def reset_counters():
    """Сбрасывает счетчики перед каждым тестом."""
    Category.category_count = 0
    Category.product_count = 0


@pytest.fixture
def sample_product():
    return Product("Test Product", "Test Description", 100.0, 10)


@pytest.fixture
def sample_category(sample_product):
    return Category("Test Category", "Test Category Description", [sample_product])


def test_add_product(sample_category, sample_product):
    """Тест добавления продукта в категорию."""
    new_product = Product("New Product", "New Desc", 50.0, 3)
    sample_category.add_product(new_product)
    assert len(sample_category.products.split("\n")) == 3  # 2 товара + пустая строка


def test_products_property(sample_category):
    """Тест геттера для products."""
    expected_output = "Test Product, 100.0 руб. Остаток: 10 шт.\n"
    assert sample_category.products == expected_output


def test_new_product():
    """Тест класс-метода new_product."""
    product_data = {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5
    }
    new_product = Product.new_product(product_data)
    assert new_product.name == "Samsung Galaxy S23 Ultra"
    assert new_product.price == 180000.0


def test_price_setter(sample_product):
    """Тест сеттера для цены."""
    sample_product.price = -100
    assert sample_product.price == 100.0  # Цена не должна измениться
    sample_product.price = 200
    assert sample_product.price == 200.0


def test_category_counters(sample_category):
    """Тест счетчиков категорий и продуктов."""
    assert Category.category_count == 1  # Только одна категория создана
    assert Category.product_count == 1  # Только один продукт в категории