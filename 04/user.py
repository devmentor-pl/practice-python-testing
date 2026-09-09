import string

def validate_user(data):
    if "@" not in data["email"]:
        return False
    if not data["email"].endswith((".com", ".pl")):
        return False
    if type(data["age"]) != int:
        return False
    if data["age"] < 18:
        return False
    if not data["name"]:
        return False
    polish_chars = "ĄĆĘŁŃÓŚŹŻąćęłńóśźż"
    allowed_ascii_chars = string.ascii_uppercase + string.ascii_lowercase
    allowed_chars = polish_chars + allowed_ascii_chars
    if any(char not in allowed_chars for char in data["name"]):
        return False
        
    return True
    