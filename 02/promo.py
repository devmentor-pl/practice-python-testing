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
    if not any(char.isdigit() for char in code):
        return False

    return True
