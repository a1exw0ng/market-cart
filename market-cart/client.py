from constants import product_catalog
from models import Cart, Product


class Client(object):
    def __init__(self):
        self.cart = Cart()

    @staticmethod
    def _get_product(product_code):
        if product_code in product_catalog.keys():
            return product_catalog[product_code]
        else:
            # TODO test this
            raise IOError("Product '{}' was not found.")

    def add_items(self, code_list):
        self.cart.batch_add_item(code_list)

    def clear_cart(self):
        self.cart = Cart()

    # TODO @apply_discounts
    def get_total(self):
        total = 0

        for code, quantity in self.cart.contents.iteritems():

            product = self._get_product(code)

            # TODO create concrete class that inherits from base b/c schema dependency
            # We don't want to repeat DB lookups when discounts are applied, so create a context
            context = dict()
            context[code] = Product(code,
                                    product["description"],
                                    product["price"],
                                    quantity)

            for i in range(quantity):
                total += product["price"]

        if total < 0:
            raise SystemError("Negative total generated: {}. Contents: {}".format(
                total, str(self.cart.contents)))

        return total
