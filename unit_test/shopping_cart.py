class NotExistsProductError(Exception):
    pass

class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def code(self):
        return "{}-123456".format(self.name)

    def __str__(self):
        return self.name


class ShoppingCart:

    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def contains_products(self):
        return len(self.products) > 0

    def remove_products(self, product):
        self.products.remove(product)
    
    def total(self):
        return sum([ product.price for product in self.products ])

    def get_product(self, product):
        if product not in self.products:
            raise NotExistsProductError('Product does not exists')
        else:
            return self.products[ self.products.index(product) - 1 ]
