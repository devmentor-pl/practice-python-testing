from unittest.mock import Mock
from payment import send_payment

payment_data = {"amount": 100, "currency": "PLN"}

def test_successful_payment():
   gateway = Mock()
   gateway.pay.return_value = True

   result_1 = send_payment(payment_data, gateway)
   assert result_1 is True

def test_unsuccessful_payment():
   gateway = Mock()
   gateway.pay.return_value = False

   result_2 = send_payment(payment_data, gateway)
   assert result_2 is False

def test_exception_payment():
   gateway = Mock()
   gateway.pay.side_effect = Exception("Gateway error")
   result_3 = send_payment(payment_data, gateway)
   assert result_3 is False
