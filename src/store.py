class Product:
    def __init__(self, name: str, price: float, description: str, quantity: int):
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, value: float):
        if not isinstance(value, (int, float)):
            raise TypeError("Цена должна быть числом.")
        if value <= 0:
            raise ValueError("Цена не должна быть нулевой или отрицательной.")
        self.__price = value

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(self) != type(other):
            raise TypeError("Нельзя складывать объекты разных типов.")
        return (self.price * self.quantity) + (other.price * other.quantity)


class Smartphone(Product):
    def __init__(
        self,
        name: str,
        price: float,
        description: str,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ):
        super().__init__(name, price, description, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    def __init__(
        self,
        name: str,
        price: float,
        description: str,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ):
        super().__init__(name, price, description, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


class Category:
    product_count = 0

    def __init__(self, name: str, description: str, products=None):
        self.name = name
        self.description = description
        self.__products = [] if products is None else products
        Category.product_count += sum(product.quantity for product in self.__products)

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError(
                "Можно добавлять только объекты класса Product или его наследников."
            )
        for existing_product in self.__products:
            if existing_product.name == product.name:
                existing_product.quantity += product.quantity
                if product.price > existing_product.price:
                    existing_product.price = product.price
                return
        self.__products.append(product)
        Category.product_count += product.quantity

    @property
    def products(self) -> str:
        return "\n".join(str(product) for product in self.__products)

    def __str__(self):
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."


