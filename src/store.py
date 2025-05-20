class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        if quantity <= 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, value: float):
        if value <= 0:
            raise ValueError("Цена должна быть больше нуля")
        self.__price = value

    def __add__(self, other):
        if type(self) != type(other):
            raise TypeError("Нельзя складывать товары разных классов.")
        return self.price * self.quantity + other.price * other.quantity

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."


class Smartphone(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 efficiency: float, model: str, memory: int, color: str):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 country: str, germination_period: str, color: str):
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
        Category.category_count += 1
        Category.product_count += sum(p.quantity for p in self.__products)

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только экземпляры класса Product")
        if product.quantity <= 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")

        for existing in self.__products:
            if existing.name == product.name:
                existing.quantity += product.quantity
                if product.price > existing.price:
                    existing.price = product.price
                return

        self.__products.append(product)
        Category.product_count += product.quantity

    def middle_price(self) -> float:
        if not self.__products:
            return 0.0
        total_price = sum(p.price for p in self.__products)
        count = len(self.__products)
        try:
            return total_price / count
        except ZeroDivisionError:
            return 0.0

    @property
    def products(self) -> str:
        return "\n".join(str(product) for product in self.__products)

    def __str__(self):
        total_quantity = sum(p.quantity for p in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."