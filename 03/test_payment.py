import unittest
from unittest.mock import Mock
from payment import send_payment
import pytest



mock_gateway = Mock()

class TestPayment(unittest.TestCase):
   def test_successful_payment(self):
      mock_gateway.return_value = True
      payment_data = {"amount": 100, "currency": "PLN"}

      self.assertTrue(send_payment(payment_data, mock_gateway))
   
   def test_unsuccessful_payment_negative_amount(self):
      mock_gateway.return_value = False
      payment_data = {"amount": -100, "currency": "PLN"}
      self.assertFalse(send_payment(payment_data, mock_gateway))

if __name__ == "__main__":
   unittest.main()   