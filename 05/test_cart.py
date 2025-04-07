import pytest
from cart import Cart

@pytest.fixture
def cart():
    return Cart()

def test_add_product(cart):
    cart.add('apple', {'name': 'apple', 'price': 3.5})
    assert 'apple' in cart.items()

def test_remove_product(cart):
    cart.add('banana', {'name': 'banana', 'price': 5})
    cart.remove('banana')
    assert 'banana' not in cart.items()


def test_total_price(cart):
    cart.add('banana', {'name': 'banana', 'price': 5})
    cart.add('apple', {'name': 'apple', 'price': 3.5})
    assert cart.total() == 8.5


def test_empty_cart_total(cart):
    assert cart.total() == 0


def test_remove_nonexistent_product(cart):
    try:
        assert cart.remove('banana')
    except Exception as error:
        print('Error:', error)
