class Product:
    def __init__(self, name, price):
        self._name = name
        self._price = float(price)

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):  # setter
        self._price = float(value)

    def make_discount(self, discount):
        """discount: in percents"""
        self._price *= (100 - discount) / 100

    def to_html(self):
        return f'<h1>{self._name} <b>{self._price}</b></h1>'


class Notebook:
    def __init__(self, name, price):
        self._name = name
        self._price = float(price)

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):  # setter
        self._price = float(value)

    def make_discount(self, discount):
        """discount: in percents"""
        self._price *= (100 - discount) / 100

    def to_html(self):
        return f'<h1>{self._name} <b>{self._price}</b></h1>'


prod_1 = Product('iPhone', 1988.64)
prod_2 = Notebook('MacBook', 2789.64)
print(prod_1.price)
print(prod_2.price)
prod_1.make_discount(5)
prod_2.make_discount(5)
print(prod_1.price)
print(prod_2.price)