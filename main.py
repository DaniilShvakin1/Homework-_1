class Product:
    def __init__(self, name: str, price: float, kolizestvo: int):
        self.name = name
        self.price = price
        self.kolizestvo = kolizestvo


class Cklad:
    def __init__(self):
        self.products = []

    def dobavit_product(self, product: Product):
        self.products.append(product)




    def total_stoumost(self):
        total = 0
        for product in self.products:
            total += product.price * product.kolizestvo
        return total

cklad = Cklad()

product1 = Product("Apple", 7.50, 100)
product2 = Product("Banana", 0.79, 900)

cklad.dobavit_product(product1)
cklad.dobavit_product(product2)

print("Общая стоимость товаров на складе:", cklad.total_stoumost())

