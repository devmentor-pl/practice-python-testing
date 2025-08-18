import string

def is_valid_promo(code):
    if not type(code) == str:
        raise ValueError("Bledny kod promocyjny - zly typ kodu")
    
    if not len(code) == 10:
        raise ValueError("Bledny kod promocyjny - zlej dlugosci kod")
    
    if any(char.islower() for char in code):
        raise ValueError("Bledny kod - male litery")

    if not code.isalnum():
        raise ValueError("Bledny kod - niedozwolone znaki")
    
    number_of_digits = 0
    for char in code:
        if char.isdigit():
            number_of_digits += 1
    if not number_of_digits >= 2:
        raise ValueError("Bledny kod promocyjny, za malo cyfr")

    return True
    