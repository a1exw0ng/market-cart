""" Implements pricing features for a shopping cart, with a variety of discounting functions and
schema for defining current discounts.
TODO: exception handling for invalid schemas
"""


def get_base_total(cart_contents_with_prices):
    total = 0

    for product in cart_contents_with_prices.values():
        total += product.quantity * product.price

    return total


def get_discounted_total(cart_contents_with_prices):
    total = get_base_total(cart_contents_with_prices)

    for f in discounts.values():
        arguments = f['arguments']
        discount = f['function'](cart_contents_with_prices, arguments)
        total -= discount

    if total < 0:
        total = 0

    return total


def bogo(cart_contents_with_prices, arguments):
    """ Buy One Get One Free
    If customer purchases an item, the next item is free, up to limit.

    :param cart_contents_with_prices: (dict of str: Product) Product instances with current price
    and quantity
    :param arguments: (dict of str)
        Required keys:
            'limit': (int) The number of times the discount may be applied.
            'products': (list of str) The product to apply discount to.

    :returns int: The amount to be discounted.
    """
    product = arguments['products'][0]
    discount = 0

    if len(arguments['products']) == 1 and product in cart_contents_with_prices:
        discount = 0
        limit = arguments['limit']
        product = arguments['products'][0]

        if product in cart_contents_with_prices:
            quantity = cart_contents_with_prices[product].quantity
            applicable_purchases = quantity // 2
            discount = max(applicable_purchases, limit) * cart_contents_with_prices[product].price
            print 'BOGO applied to {}: {} of {} times. Discount: {}'\
                .format(product, max(applicable_purchases, limit),
                        limit,
                        discount)
    return discount


def bulk(cart_contents_with_prices, arguments):
    """ Bulk Pricing
    If customer purchases n units of item, the unit price for the item is discounted.

    :param cart_contents_with_prices: (dict of str: Product) Product instances with current price
    and quantity
    :param arguments: (dict of str)
        Required keys:
            'limit': (int) The minimum number of times the user must purchase.
            'products': (list of str) The product to apply discount to.
            'bulk_price': (int) The bulk pricing of the item.

    :returns int: The amount to be discounted.
    """
    product = arguments['products'][0]
    discount = 0

    if len(arguments['products']) == 1 and product in cart_contents_with_prices:
        required_minimum = arguments['limit']
        bulk_price = arguments['bulk_price']
        base_price = cart_contents_with_prices[product].price
        quantity = cart_contents_with_prices[product].quantity

        if quantity >= required_minimum:
            discount = (base_price - bulk_price) * quantity

        print "BULK applied, {} with quantity {} and discount {}"\
            .format(product, quantity, discount)

    return discount


def combo(cart_contents_with_prices, arguments):
    """ Combo Pricing
    If customer purchases one product_a, customer may get one product_b free.

    :param cart_contents_with_prices: (dict of str: Product) Product instances with current price
    and quantity
    :param arguments: (dict of str)
        Required keys:
            'limit': (int) The minimum number of times the discount may be applied.
            'products': (list of str) ['product_a', 'product_b']

    :returns int: The amount to be discounted.
    """

    discount = 0

    if len(arguments['products']) == 2:
        products = arguments['products']
        limit = arguments['limit']
        discount_product_a = products[0]
        discount_product_b = products[1]

        if discount_product_a in cart_contents_with_prices \
                and discount_product_b in cart_contents_with_prices:
            cart_product_a = cart_contents_with_prices[discount_product_a]
            cart_product_b = cart_contents_with_prices[discount_product_b]

            applicable_purchases = min(cart_product_a.quantity, cart_product_b.quantity)
            discounted_products = max(applicable_purchases, limit)
            discount = discounted_products * cart_product_b.price
            print "COMBO applied, discount {}".format(discount)

    return discount


discounts = {
    'BOGO': {'description': "Buy-One-Get-One-Free Special on Coffee.",
             'function': bogo,
             'arguments': {
                 'products': ['CF1'],
                 'limit': -1}
             },

    'APPL': {'description': "If you buy 3 or more bags of Apples, the price drops to $4.50.",
             'function': bulk,
             'arguments': {
                 'products': ['AP1'],
                 'limit': 3,
                 'bulk_price': 450}
             },

    'CHMK': {'description': "Purchase a box of Chai and get milk free. (Limit 1)",
             'function': combo,
             'arguments': {
                 'products': ['CH1', 'MK1'],
                 'limit': 1}
             }
}
