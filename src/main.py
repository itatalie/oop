from src.store import Category, Product

def main():
    # Создаем категорию
    electronics = Category("Электроника")

    # Создаем продукты
    phone = Product("Телефон", 10000, "Смартфон", 5)
    headphones = Product("Наушники", 2000, "Беспроводные", 10)

    # Добавляем продукты в категорию
    electronics.add_product(phone)
    electronics.add_product(headphones)

    # Выводим список товаров
    print("Список товаров:")
    print(electronics.products)

    # Обновляем цену продукта
    phone.price = 12000
    print("\nОбновленная цена телефона:", phone.price)

if __name__ == "__main__":
    main()