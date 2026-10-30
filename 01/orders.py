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