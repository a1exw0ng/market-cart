product_catalog = {
    'CH1': {'description': 'Chai',
            'price': 311},

    'AP1': {'description': 'Apples',
            'price': 600},

    'CF1': {'description': 'Coffee',
            'price': 1123},

    'MK1': {'description': 'Milk',
            'price': 475},

    'OM1': {'description': 'Oatmeal',
            'price': 369},
}


def get_product(product_code):
    if product_code in product_catalog.keys():
        return product_catalog[product_code]
    else:
        # TODO test this
        raise IOError("Product '{}' was not found.")
