from collections import Counter
from constants import product_catalog


class Product(object):
    def __init__(self, code, description, price, quantity):
        self.code = code
        self.description = description
        self.price = price
        self.quantity = quantity


class Cart(object):
    def __init__(self):
        self.contents = Counter()

    def add_item(self, product_code, quantity=1):
        if product_code in product_catalog.keys():
            self.contents[product_code] += quantity

        else:
            # TODO test this
            raise IOError("Product '{}' was not found, cannot be added to cart.")

        # TODO verify product exists here or in controller

    def batch_add_item(self, code_list):
        counter = Counter(code_list)
        for code, value in counter.iteritems():
            self.add_item(code, quantity=value)
