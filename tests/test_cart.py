from models import Cart


def test_add_item():
    cart = Cart()
    cart.add_item("AP1")
    cart.add_item("AP1")
    cart.add_item("CH1")

    assert len(cart.contents.keys()) == 2
    assert cart.contents["CH1"] == 1
    assert cart.contents["AP1"] == 2
    assert sum(cart.contents.values()) == 3

    cart.batch_add_item(["CF1", "CF1", "CF1"])
    assert cart.contents["CF1"] == 3
    assert sum(cart.contents.values()) == 6
