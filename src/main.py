from src.store import Product, Smartphone, LawnGrass, Category


if __name__ == "__main__":
    try:
        invalid_product = Product("Брак", "Нулевое количество", 1000.0, 0)
    except ValueError as e:
        print(f"Ошибка при создании продукта с нулевым количеством: {e}")

    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(str(product1))
    print(str(product2))
    print(str(product3))

    category1 = Category("Смартфоны", "Высокотехнологичные смартфоны", [product1, product2, product3])
    print(str(category1))

    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)
    print(str(category1))

    print(category1.products_list)

    try:
        print(product1 + product2)
    except TypeError as e:
        print(f"Ошибка: {e}")