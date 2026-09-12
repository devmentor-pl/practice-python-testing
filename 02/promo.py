import string

def is_valid_promo(code):
    if type(code) != str:
        return False
    
    if len(code) != 10:
        return False
    
    allowed_chars = string.ascii_uppercase + string.digits
    
    if any(char not in allowed_chars for char in code):
        return False
    
    i = 0
    for char in code:
        if char in string.digits:
            i += 1
    if i < 2:
        return False
    
    return True
