from src.store import Product, Smartphone, LawnGrass, Category

# Создание продуктов
product1 = Product(
    "Samsung Galaxy S23 Ultra", 180000.0, "256GB, Серый цвет, 200MP камера", 5
)
product2 = Product("Iphone 15", 210000.0, "512GB, Gray space", 8)
product3 = Product("Xiaomi Redmi Note 11", 31000.0, "1024GB, Синий", 14)

print(str(product1))
print(str(product2))
print(str(product3))

# Создание категории
category1 = Category(
    "Смартфоны", "Смартфоны как средство коммуникации", [product1, product2, product3]
)
print(str(category1))

# Добавление нового продукта
product4 = Product('55" QLED 4K', 123000.0, "Фоновая подсветка", 7)
category1.add_product(product4)
print(str(category1))

print(category1.products)
