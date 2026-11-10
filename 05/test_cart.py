import pytest
from cart import Cart

apple = {"name": "apple", "price": 3.5}
banana = {"name": "banana", "price": 7}

def test_add_product():
    cart_1 = Cart()
    cart_1.add(apple)
    assert cart_1.items() == [{"name": "apple", "price": 3.5}]

def test_remove_product():
    cart_2 = Cart()
    cart_2.add(apple)
    cart_2.add(banana)
    cart_2.remove("apple")
    assert cart_2.items() == [{"name": "banana", "price": 7}]

def test_total_price():
    cart_3 = Cart()
    cart_3.add(apple)
    cart_3.add(banana)
    assert cart_3.total() == 10.5

def test_empty_cart_total():
    cart_4 = Cart()
    assert cart_4.total() == 0

def test_remove_nonexistent_product():
    cart_5 = Cart()
    cart_5.add(apple)
    cart_5.add(banana)
    cart_5.remove("lemon")
    assert cart_5.items() == [{"name": "apple", "price": 3.5}, {"name": "banana", "price": 7}]