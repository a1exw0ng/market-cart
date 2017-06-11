import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

product_catalog = {
    "CH1": {"description": "Chai",
            "price": 311},

    "AP1": {"description": "Apples",
            "price": 600},

    "CF1": {"description": "Coffee",
            "price": 1123},

    "MK1": {"description": "Milk",
            "price": 475},

    "OM1": {"description": "Oatmeal",
            "price": 369},
}


discounts = {
    "BOGO": {"description": "Buy-One-Get-One-Free Special on Coffee.",
             "type": "bogo",
             "related": "CF1",
             "limit": -1},

    "APPL": {"description": "If you buy 3 or more bags of Apples, the price drops to $4.50.",
             "related": "AP1",
             "type": "bulk",
             "limit": 1},

    "CHMK": {"description": "Purchase a box of Chai and get milk free. (Limit 1)",
             "related": "CH1,MK1",
             "type": "combination",
             "limit": 1}
}
