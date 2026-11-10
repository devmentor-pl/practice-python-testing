def validate_user(data):
    email = data.get("email", "")
    if not email or "@" not in email:
        return False  
    elif not data.get("email").endswith((".pl", ".com")):
        return False
    elif not isinstance(data.get("age"), int):
        return False
    elif data.get("age") <18:
        return False
    elif not all(character.isalpha() or character == " " for character in data.get("name")):
        return False
    return True
