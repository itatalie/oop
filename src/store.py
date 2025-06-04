from abc import ABC, abstractmethod


class BaseProduct(ABC):
    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    @property
    @abstractmethod
    def price(self) -> float:
        pass

    @price.setter
    @abstractmethod
    def price(self, value: float):
        if not isinstance(value, (int, float)):
            raise TypeError("Цена должна быть числом.")
        if value <= 0:
            raise ValueError("Цена должна быть больше нуля.")


class Product(BaseProduct):
    def __init__(self, name: str, description: str, price: float, quantity: int):
        if quantity <= 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        if not isinstance(price, (int, float)):
            raise TypeError("Цена должна быть числом.")
        if price <= 0:
            raise ValueError("Цена не должна быть нулевой или отрицательной.")

        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float):
        if not isinstance(value, (int, float)):
            raise TypeError("Цена должна быть числом.")
        if value <= 0:
            raise ValueError("Цена должна быть больше нуля.")
        self._price = value

    def __add__(self, other):
        if type(self) != type(other):
            raise TypeError("Нельзя складывать товары разных классов.")
        return (self.price * self.quantity) + (other.price * other.quantity)

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."


class Smartphone(Product):
    def __init__(
        self, name: str, description: str, price: float, quantity: int,
        efficiency: float, model: str, memory: int, color: str
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    def __init__(
        self, name: str, description: str, price: float, quantity: int,
        country: str, germination_period: str, color: str
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products=None):
        self.name = name
        self.description = description
        self.__products = [] if products is None else products

        # Увеличиваем счетчики
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только экземпляры класса Product")

        if product.quantity <= 0:
            raise ValueError("Количество должно быть больше нуля")

        for existing in self.__products:
            if existing.name == product.name:
                existing.quantity += product.quantity
                if product.price > existing.price:
                    existing.price = product.price
                return

        self.__products.append(product)
        Category.product_count += 1  # Только при добавлении нового продукта

    @property
    def products_list(self):
        return self.__products

    def middle_price(self) -> float:
        if not self.products_list:
            return 0.0
        total_price = sum(p.price for p in self.products_list)
        return round(total_price / len(self.products_list), 2)

    def __str__(self):
        total_quantity = sum(p.quantity for p in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."