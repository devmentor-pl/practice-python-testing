def validate_order(order):
    if not isinstance(order.get("user_id"), int):
        raise ValueError("Nieprawidłowy user_id")
    if not order["items"]:
        raise ValueError("Pusta lista zakupów")
    if order["delivery"]["method"] not in ["courier", "pickup", "drone"]:
        raise ValueError("Nieprawidłowa metoda dostawy")
    if not order["delivery"]["address"]:
        raise ValueError("Nieprawidłowy adres")

    return True
