import pytest
from src.store import Product, Smartphone, LawnGrass, Category, BaseProduct


@pytest.fixture(autouse=True)
def reset_counters():
    Category.category_count = 0
    Category.product_count = 0


def test_baseproduct_is_abstract():
    with pytest.raises(TypeError):
        class DummyProduct(BaseProduct):
            pass


def test_product_creation_logs(capsys):
    product = Product("Телефон", "Описание", 30000.0, 10)
    captured = capsys.readouterr()
    assert "Создан объект Product(Телефон, Описание, 30000.0, 10)" in captured.out


def test_smartphone_inherits_from_product():
    smartphone = Smartphone(
        "Iphone", "Флагман Apple", 210000.0, 8,
        98.2, "15", 512, "Gray space"
    )
    assert isinstance(smartphone, Product)


def test_lawn_grass_inherits_from_product():
    grass = LawnGrass(
        "Газонная трава", "Элитная для газона", 500.0, 20,
        "Россия", "7 дней", "Зеленый"
    )
    assert isinstance(grass, Product)


def test_addition_same_class():
    product1 = Product("Телефон", "Описание", 30000.0, 10)
    product2 = Product("Телефон", "Обновленное описание", 35000.0, 5)
    assert product1 + product2 == 30000 * 10 + 35000 * 5


def test_addition_different_class():
    product = Product("Телефон", "Описание", 30000.0, 10)
    grass = LawnGrass("Трава", "Зеленая", 500.0, 20, "Россия", "7 дней", "Зеленый")
    with pytest.raises(TypeError):
        product + grass


def test_price_validation():
    # Корректные значения
    product = Product("Телефон", "Описание", 30000.0, 10)
    assert product.price == 30000.0

    # Строка вместо цены
    with pytest.raises(TypeError):
        Product("Ошибка", "Строка вместо цены", "строка", 10)

    # Цена 0
    with pytest.raises(ValueError):
        Product("Ошибка", "Цена 0", 0, 10)

    # Отрицательная цена
    with pytest.raises(ValueError):
        Product("Ошибка", "Отрицательная цена", -100, 10)


def test_duplicate_handling():
    category = Category("Электроника", "Описание категории")
    product1 = Product("Телефон", "Смартфон", 30000.0, 10)
    product2 = Product("Телефон", "Обновленное описание", 35000.0, 5)
    category.add_product(product1)
    category.add_product(product2)

    assert len(category.products_list) == 1
    assert category.products_list[0].quantity == 15
    assert category.products_list[0].price == 35000.0


def test_category_counters():
    category = Category("Смартфоны", "Высокотехнологичные смартфоны")
    product1 = Product("Iphone", "Флагман", 210000.0, 8)
    product2 = Product("Samsung", "Флагман", 180000.0, 5)
    category.add_product(product1)
    category.add_product(product2)

    assert len(category.products_list) == 2
    assert Category.category_count == 1
    assert Category.product_count == 13


def test_str_representation():
    product = Product("Телефон", "Описание", 30000.0, 10)
    assert str(product) == "Телефон, 30000.0 руб. Остаток: 10 шт."