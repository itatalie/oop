class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self._price = price  # Приватный атрибут цены
        self.quantity = quantity

    @property
    def price(self):
        """Геттер для цены."""
        return self._price

    @price.setter
    def price(self, value: float):
        """Сеттер для цены с проверкой на положительное значение."""
        if value > 0:
            self._price = value
        else:
            print("Цена не должна быть нулевая или отрицательная")

    @classmethod
    def new_product(cls, product_data: dict):
        """
        Класс-метод для создания нового продукта из словаря.
        :param product_data: Словарь с данными продукта.
        :return: Экземпляр класса Product.
        """
        return cls(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"]
        )


class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product]):
        self.name = name
        self.description = description
        self.__products = products  # Приватный атрибут списка товаров

        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, product: Product):
        """
        Метод для добавления продукта в категорию.
        :param product: Экземпляр класса Product.
        """
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        """
        Геттер для вывода списка товаров в виде строки.
        :return: Строка со всеми товарами.
        """
        result = ""
        for product in self.__products:
            result += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return result