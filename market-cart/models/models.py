from collections import Counter
from dao_products import get_product


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
        """ Adds the desired quantity of a product by product code. Pricing is not requested until
        the user is ready to view the total. """

        try:
            # Check if product exists in database
            product = get_product(product_code)
            self.contents[product_code] += quantity
        except IOError, e:
            print(e.message)

    def batch_add_item(self, code_list):
        counter = Counter(code_list)
        for code, value in counter.iteritems():
            self.add_item(code, quantity=value)
