from unittest.mock import Mock
from payment import send_payment

data = {
    "amount": 100,
    "currency": "PLN",
}

def test_successful_payment():
   gateway = Mock()
   gateway.pay.return_value = True
   assert send_payment(data, gateway) is True

def test_failed_payment():
   gateway = Mock()
   gateway.pay.return_value = False
   assert send_payment(data, gateway) is False
   
def test_payment_exception():
   gateway = Mock()
   gateway.pay.side_effect = Exception("Error")
   assert send_payment(data, gateway) is False
   