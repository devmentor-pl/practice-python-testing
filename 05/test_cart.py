import pytest
from cart import Cart

@pytest.fixture
def cart():
    return Cart()

def test_add_product(cart):
    cart.add({'name': 'apple', 'price': 3.5})
    assert cart.items() == [{'name': 'apple', 'price': 3.5}]

def test_remove_product(cart):
    cart.add({'name': 'apple', 'price': 3.5})
    cart.add({'name': 'apple', 'price': 5.0})
    cart.add({'name': 'banana', 'price': 4.5})
    cart.remove("apple")
    assert cart.items() == [
        {'name': 'apple', 'price': 5.0},
        {'name': 'banana', 'price': 4.5},
    ]

def test_total_price(cart):
    cart.add({'name': 'apple', 'price': 3.5})
    cart.add({'name': 'banana', 'price': 4.5})
    assert cart.total() == 8.0

def test_empty_cart_total(cart):
    assert cart.total() == 0.0

def test_remove_nonexistent_product(cart):
    cart.remove("orange")
    assert cart.items() == []
    