import unittest
from orders import validate_order

order = {
    "user_id": 101,
    "items": ["keyboard", "mouse", "monitor"],
    "delivery": {
        "method": "courier",         
        "address": "ul. Polna 10, 00-001 Warszawa"
    }
}

order_user_id = {
    "user_id": "101",
    "items": ["keyboard", "mouse", "monitor"],
    "delivery": {
        "method": "courier",         
        "address": "ul. Polna 10, 00-001 Warszawa"
    }
}

order_empty_list = {
    "user_id": 101,
    "items": [],
    "delivery": {
        "method": "courier",         
        "address": "ul. Polna 10, 00-001 Warszawa"
    }
}

order_wrong_delivery_method = {
    "user_id": 101,
    "items": ["keyboard", "mouse", "monitor"],
    "delivery": {
        "method": "abc",         
        "address": "ul. Polna 10, 00-001 Warszawa"
    }
}

order_empty_address = {
    "user_id": 101,
    "items": ["keyboard", "mouse", "monitor"],
    "delivery": {
        "method": "courier",         
        "address": ""
    }
}

class TestValidateOrder(unittest.TestCase): 

   def test_good(self):
      self.assertEqual(validate_order(order), True)   
      
   def test_user_id(self):
      with self.assertRaises(ValueError) as context:
         validate_order(order_user_id)
      self.assertEqual(str(context.exception), "Nieprawidłowy user_id")  
      
   def test_empty_list(self):
      with self.assertRaises(ValueError) as context:
         validate_order(order_empty_list)
      self.assertEqual(str(context.exception), "Pusta lista zakupów") 
      
   def test_wrong_delivery_method(self):
      with self.assertRaises(ValueError) as context:
         validate_order(order_wrong_delivery_method)
      self.assertEqual(str(context.exception), "Nieprawidłowa metoda dostawy") 
      
   def test_empty_address(self):
         with self.assertRaises(ValueError) as context:
            validate_order(order_empty_address)
         self.assertEqual(str(context.exception), "Nieprawidłowy adres") 

if __name__ == "__main__":
    unittest.main()
