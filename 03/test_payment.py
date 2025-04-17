import unittest
from unittest.mock import Mock
from payment import send_payment


class TestSendPayment(unittest.TestCase):
    def test_successful_payment(self):
        payment_data = {"amount": 100, "currency": "PLN"}
        gateway = Mock()
        gateway.pay.return_value = True

        result = send_payment(payment_data, gateway)
        self.assertTrue(result)

    def test_failed_payment(self):
        payment_data = {"amount": 100, "currency": "PLN"}
        gateway = Mock()
        gateway.pay.return_value = False

        result = send_payment(payment_data, gateway)
        self.assertFalse(result)

    def test_payment_exception(self):
        payment_data = {"amount": 100, "currency": "PLN"}
        gateway = Mock()
        gateway.pay.side_effect = Exception('Error')
        gateway.pay.return_value = False

        result = send_payment(payment_data, gateway)
        self.assertFalse(result)
      # sprawdzenie wyjątku  self.assertRaises


if __name__ == '__main__':
    unittest.main()
