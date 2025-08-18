import pytest
from cart import Cart

@pytest.fixture
def sample_product():
    return {"product": "woda", "price": 4.99}

def test_add_product():
    cart = Cart()
    cart.add_to_cart("woda", 4.99) 

    assert len(cart.cart_list) == 1
    assert cart.cart_list[0]["product"] == "woda"
    assert cart.cart_list[0]["price"] == 4.99

def test_remove_product():
    cart = Cart()
    cart.add_to_cart("woda", 4.99)
    cart.add_to_cart("ziemniaki", 8.00)
    cart.add_to_cart("woda", 4.99)

    cart.remove_from_cart("woda")

    assert len(cart.cart_list) == 2
    assert cart.cart_list[0]["product"] == "ziemniaki"

def test_total_price():
    cart = Cart()
    cart.add_to_cart("woda", 4.99)
    cart.add_to_cart("ziemniaki", 8.00)
    cart.add_to_cart("woda", 4.99)

    assert cart.total_cart() == 17.98

def test_empty_cart_total():
    cart = Cart()

    assert cart.total_cart() == 0.00

def test_remove_nonexistent_product():
    cart = Cart()
    cart.add_to_cart("woda", 4.99)
    cart.remove_from_cart("ziemniaki")
    assert len(cart.cart_list) == 1