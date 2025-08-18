'''`{"amount": 100, "currency": "PLN"}`'''

    
def send_payment(payment_data, gateway):
    class PaySystem():
        def pay(self,data):
            if not isinstance(payment_data.get("amount"),int):
                raise ValueError("Blad kwoty")
            
            if not (payment_data.get("amount")) > 0:
                raise ValueError("Blad kwoty, nie moze byc mniejsza niz 0")
        
            if not isinstance(payment_data.get("currency"),str):
                raise ValueError("Blad waluty")
            return True
    try:        
        gateway = PaySystem()
        result = gateway.pay(payment_data)
        
        if not result:
            raise ValueError("Blad platnosci")
        
        print("Platnosc udana")
        return result is True
    
    
    except Exception as e:
        print(f"Cos poszlo nie tak - {e}")
        return False