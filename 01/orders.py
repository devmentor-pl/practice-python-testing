def validate_order(order):
    if not isinstance(order.get("user_id"), int):
        raise ValueError("Nieprawidłowy user_id")
    # uzupełnij resztę przypadków

    return True
