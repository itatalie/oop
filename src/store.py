class Product:
    def __init__(self, name: str, price: float, description: str, quantity: int):
        """
        Инициализация продукта.
        :param name: Название продукта.
        :param price: Цена продукта.
        :param description: Описание продукта.
        :param quantity: Количество товара на складе.
        """
        self.name = name
        self.__price = price  # Приватный атрибут цены
        self.description = description
        self.quantity = quantity

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, value: float):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value

    def __str__(self):
        """
        Строковое представление продукта.
        """
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """
        Магический метод сложения для расчета общей стоимости товаров.
        """
        if isinstance(other, Product):
            return (self.__price * self.quantity) + (other.price * other.quantity)
        raise TypeError("Нельзя складывать объекты разных типов.")


class Category:
    product_counter = 0  # Класс-атрибут для подсчета продуктов

    def __init__(self, name: str, description: str):
        """
        Инициализация категории.
        :param name: Название категории.
        :param description: Описание категории.
        """
        self.name = name
        self.description = description
        self.__products = []  # Приватный атрибут списка товаров

    def add_product(self, product):
        """
        Добавляет продукт в категорию.
        """
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product.")

        for existing_product in self.__products:
            if existing_product.name == product.name:
                existing_product.quantity += product.quantity
                if product.price > existing_product.price:
                    existing_product.price = product.price
                return

        self.__products.append(product)
        Category.product_counter += 1  # Увеличиваем счетчик только при успешном добавлении

    @property
    def products(self) -> str:
        """
        Геттер для вывода списка товаров.
        """
        return "\n".join(str(product) for product in self.__products)

    def __str__(self):
        """
        Строковое представление категории.
        """
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."