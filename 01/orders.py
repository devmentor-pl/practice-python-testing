def validate_order(order):
    if not isinstance(order.get("user_id"), int):
        raise ValueError("Nieprawidłowy user_id")
    # uzupełnij resztę przypadków
    if  not order.get("items"):
        raise ValueError("Pusta lista zakupow")
    
    if  order.get("delivery").get("method") not in ("courier", "pickup", "drone"):
        raise ValueError("Nieprawidłowy sposób dostawy")
    
    if not order.get("delivery").get("address"):
        raise ValueError("Brak adresu dostawy")

    return True

