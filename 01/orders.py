import unittest

delivery_method = ("courier", "pickup", "drone")

def validate_order(order):
    if not isinstance(order.get("user_id"), int):
        raise ValueError("Nieprawidłowy user_id")
    # uzupełnij resztę przypadków
    if order.get("items") == []:
        raise ValueError("Pusta lista items")
    if order.get("delivery").get("method") not in delivery_method:
        raise ValueError("Niepoprawna metoda wysyłki")
    if order.get("delivery").get("address") == "":
        raise ValueError("Brak adresu dostawy")
    return True

class TestValidateOrder(unittest.TestCase):
    def test_user_id(self):
        with self.assertRaises(ValueError) as context:
            validate_order(order_1)
        self.assertEqual(str(context.exception), "Nieprawidłowy user_id")
    def test_items(self):
        with self.assertRaises(ValueError) as context:
            validate_order(order_2)
        self.assertEqual(str(context.exception), "Pusta lista items")
    def test_delivery_method(self):
        with self.assertRaises(ValueError) as context:
            validate_order(order_3)
        self.assertEqual(str(context.exception), "Niepoprawna metoda wysyłki")
    def test_address(self):
        with self.assertRaises(ValueError) as context:
            validate_order(order_4)
        self.assertEqual(str(context.exception), "Brak adresu dostawy")

order_1 = {
    "user_id": "Marek7",
    "items": ["keyboard", "mouse", "monitor"],
    "delivery": {
        "method": "courier",         
        "address": "ul. Polna 10, 00-001 Warszawa"
    }
}

order_2 = {
    "user_id": 101,
    "items": [],
    "delivery": {
        "method": "courier",         
        "address": "ul. Polna 10, 00-001 Warszawa"
    }
}

order_3 = {
    "user_id": 101,
    "items": ["keyboard", "mouse", "monitor"],
    "delivery": {
        "method": "wysyłka",         
        "address": "ul. Polna 10, 00-001 Warszawa"
    }
}

order_4 = {
    "user_id": 101,
    "items": ["keyboard", "mouse", "monitor"],
    "delivery": {
        "method": "courier",         
        "address": ""
    }
}

if __name__ == "__main__":
    unittest.main()

