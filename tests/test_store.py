import pytest
from src.store import Product, Smartphone, LawnGrass, Category


@pytest.fixture(autouse=True)
def reset_counters():
    Category.product_count = 0


def test_smartphone_initialization():
    smartphone = Smartphone(
        "Iphone 15", 210000.0, "512GB, Gray space", 8, 98.2, "15", 512, "Gray space"
    )
    assert smartphone.efficiency == 98.2
    assert smartphone.model == "15"
    assert smartphone.memory == 512
    assert smartphone.color == "Gray space"


def test_lawn_grass_initialization():
    grass = LawnGrass(
        "Газонная трава",
        500.0,
        "Элитная трава для газона",
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )
    assert grass.country == "Россия"
    assert grass.germination_period == "7 дней"
    assert grass.color == "Зеленый"


def test_addition_with_same_class():
    product1 = Product("Test1", 10.0, "Desc1", 5)
    product2 = Product("Test2", 20.0, "Desc2", 3)
    assert product1 + product2 == 10 * 5 + 20 * 3


def test_addition_with_different_classes():
    product = Product("Test", 10.0, "Desc", 5)
    smartphone = Smartphone("Iphone", 500.0, "128GB", 2, 95.0, "X", 128, "Black")
    with pytest.raises(TypeError):
        product + smartphone


def test_category_add_product():
    category = Category("Test Category", "Description")
    smartphone = Smartphone(
        "Iphone 15", 210000.0, "512GB, Gray space", 8, 98.2, "15", 512, "Gray space"
    )
    category.add_product(smartphone)
    assert len(category._Category__products) == 1
    assert Category.product_count == 8


def test_category_add_invalid_product():
    category = Category("Test Category", "Description")
    with pytest.raises(TypeError):
        category.add_product("Not a product")


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
