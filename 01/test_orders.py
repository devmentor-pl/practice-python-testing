import unittest
from orders import validate_order

class TestValidateOrder(unittest.TestCase):
    def test_valid_items(self):
        order = {
            "user_id": 101,
            "items": [],
            "delivery": {
                "method": "courier",
                "address": "ul. Polna 10, 00-001 Warszawa"
            }
        }
        with self.assertRaises(KeyError):
            validate_order(order)

    def test_invalid_delivery_method(self):
        order = {
            "user_id": 101,
            "items": ["keyboard", "mouse", "monitor"],
            "delivery": {
                "method": "bird",
                "address": "ul. Polna 10, 00-001 Warszawa"
            }
        }
        with self.assertRaises(IndexError):
            validate_order(order)

    def test_missing_delivery_address(self):
        order = {
            "user_id": 101,
            "items": ["keyboard", "mouse", "monitor"],
            "delivery": {
                "method": "courier",
                "address": ""
            }
        }
        with self.assertRaises(KeyError):
            validate_order(order)

   # pass

if __name__ == "__main__":
    unittest.main()
