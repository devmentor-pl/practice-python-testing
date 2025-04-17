def validate_order(order):
    if not isinstance(order.get("user_id"), int):
        raise ValueError("Nieprawidłowy user_id")
    if not order['items']:
        raise KeyError('Zamówienie jest puste')
    if order['delivery']['method'] not in ['courier', 'pickup', 'drone']:
        raise IndexError('Wybierz poprawny rodzaj dostawy')
    if not order['delivery']['address']:
        raise KeyError('Podaj adres wysyłki')

    return True


order = {
    "user_id": 101,
    "items": ["keyboard", "mouse", "monitor"],
    "delivery": {
        "method": "courier",
        "address": "ul. Polna 10, 00-001 Warszawa"
    }
}

print(validate_order(order))
