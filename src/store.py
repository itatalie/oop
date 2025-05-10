class Product:
    def __init__(self, name: str, price: float, description: str, quantity: int):
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
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    @classmethod
    def new_product(cls, product_data: dict):
        return cls(
            name=product_data.get("name"),
            price=product_data.get("price"),
            description=product_data.get("description"),
            quantity=product_data.get("quantity", 0),
        )


class Category:
    product_counter = 0  # Класс-атрибут для подсчета продуктов

    def __init__(self, name: str):
        self.name = name
        self.__products = []  # Приватный атрибут списка товаров

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product.")

        for existing_product in self.__products:
            if existing_product.name == product.name:
                existing_product.quantity += product.quantity
                if product.price > existing_product.price:
                    existing_product.price = product.price
                return

        self.__products.append(product)
        Category.product_counter += 1

    @property
    def products(self) -> str:
        return "\n".join(str(product) for product in self.__products)

    def find_duplicate_product(self, new_product):
        for product in self.__products:
            if product.name == new_product.name:
                product.quantity += new_product.quantity
                if new_product.price > product.price:
                    product.price = new_product.price
                return True
        return False