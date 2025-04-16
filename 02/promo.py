import string


def is_valid_promo(code):
    if not isinstance(code, str):
        return False
    if not len(code) == 10:
        return False
    if not code.isalnum():
        return False
    if not code.isupper():
        return False
    digits_count = sum(char.isdigit() for char in code)
    if digits_count < 2:
        return False

    return True
