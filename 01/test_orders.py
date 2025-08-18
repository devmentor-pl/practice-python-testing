import unittest
from orders import validate_order

class TestValidateOrder(unittest.TestCase):

   def test_validaye_user_id(self):
        with self.assertRaises(ValueError) as context:
           validate_order({
    "user_id": "Marcin",
    "items": ["keyboard", "mouse", "monitor"],
    "delivery": {
        "method": "courier",         
        "address": "ul. Polna 10, 00-001 Warszawa"
    }})
        self.assertEqual(str(context.exception), "Nieprawidłowy user_id")

   def test_validaye_items_list(self):
        with self.assertRaises(ValueError) as context:
           validate_order({
    "user_id": 123,
    "items": [],
    "delivery": {
        "method": "courier",         
        "address": "ul. Polna 10, 00-001 Warszawa"
    }})
        self.assertEqual(str(context.exception), "Pusta lista zakupow")

   def test_validaye_delivery_method(self):
        with self.assertRaises(ValueError) as context:
           validate_order({
    "user_id": 123,
    "items": ["keyboard", "mouse", "monitor"],
    "delivery": {
        "method": "",         
        "address": "ul. Polna 10, 00-001 Warszawa"
    }})
        self.assertEqual(str(context.exception), "Nieprawidłowy sposób dostawy")

   def test_validaye_delivery_address(self):
        with self.assertRaises(ValueError) as context:
           validate_order({
    "user_id": 123,
    "items": ["keyboard", "mouse", "monitor"],
    "delivery": {
        "method": "courier",         
        "address": ""
    }})
        self.assertEqual(str(context.exception), "Brak adresu dostawy")

if __name__ == "__main__":
    unittest.main()
