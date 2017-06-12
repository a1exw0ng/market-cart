from dao_products import get_product
from models import Cart, Product
from pricing import get_discounted_total


class Client(object):
    def __init__(self):
        self.cart = Cart()

    def add_items(self, code_list):
        self.cart.batch_add_item(code_list)

    def clear_cart(self):
        self.cart = Cart()

    def get_total(self):
        cart_contents_with_prices = dict()

        for code, quantity in self.cart.contents.iteritems():
            product = get_product(code)

            # We don't want to repeat DB lookups when discounts are applied, so create a context
            # of the cart with current prices and quantities
            cart_contents_with_prices[code] = Product(code,
                                                      product["description"],
                                                      product["price"],
                                                      quantity)

        return get_discounted_total(cart_contents_with_prices)
