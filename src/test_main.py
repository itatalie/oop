import pytest
from src.main import Product, Category  # Используем абсолютный импорт


@pytest.fixture
def sample_product():
    return Product("Test Product", "Test Description", 100.0, 10)


def test_product_initialization(sample_product):
    assert sample_product.name == "Test Product"
    assert sample_product.price == 100.0


def test_category_counters():
    product1 = Product("Product1", "Desc1", 10.0, 5)
    category1 = Category("Category1", "Desc1", [product1])

    assert Category.category_count == 1
    assert Category.product_count == 1