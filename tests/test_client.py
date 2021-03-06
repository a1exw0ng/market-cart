import pytest
from client import Client

client = Client()


def test_clear_cart():
    client.add_items(["AP1"])
    assert sum(client.cart.contents.values()) == 1
    client.clear_cart()
    assert sum(client.cart.contents.values()) == 0


@pytest.mark.parametrize("product_list, expected", [
    (["CH1", "AP1", "CF1", "MK1"], 20.34),
    (["MK1", "AP1"], 10.75),
    (["CF1", "CF1"], 11.23),
    (["AP1", "AP1", "CH1", "AP1"], 16.61)])
def test_discounts(product_list, expected):
    client.clear_cart()
    client.add_items(product_list)
    assert client.get_total() == expected
