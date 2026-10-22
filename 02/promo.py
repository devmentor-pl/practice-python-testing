import string

def character_verifier(text):
    wrong_characters = 0
    for i in text:
        if not (i.isupper() or i.isdigit()):
            wrong_characters += 1
    return wrong_characters

def digit_count(text):
    digits = 0
    for i in text:
        if i.isdigit():
            digits += 1
    return digits

def is_valid_promo(code):
    if not isinstance(code, str):
        return False
    elif len(code) != 10:
        return False
    elif character_verifier(code) > 0:
        return False
    elif digit_count(code) < 2:
        return False
    return True

promo = "P!IAKISĄ22"

print(is_valid_promo(promo))