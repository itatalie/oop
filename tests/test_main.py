from src.store import Product, Smartphone, LawnGrass, Category


if __name__ == "__main__":
    try:
        # Тестирование ошибки при создании продукта с нулевым количеством
        invalid_product = Product("Брак", "Описание", 1000.0, 0)
    except ValueError as e:
        print(f"Ошибка при создании продукта с нулевым количеством: {e}")
    else:
        print("Не было ошибки при нулевом количестве")

    # Создание продуктов
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    # Создание категории
    category_smartphones = Category("Смартфоны", "Высокотехнологичные смартфоны")
    category_smartphones.add_product(product1)
    category_smartphones.add_product(product2)
    category_smartphones.add_product(product3)

    # Средняя цена
    print(f"Средняя цена: {category_smartphones.middle_price()}")

    # Пустая категория
    empty_category = Category("Пустая категория", "Категория без продуктов")
    print(f"Средняя цена в пустой категории: {empty_category.middle_price()}")