def validate_user(data):
    try:
        at = 0
        for char in data.get("email"):
            if char == "@":
                at += 1
        if not at == 1:
            raise ValueError("Blad maila - zla ilosc @")
        
        if not data.get("email").endswith((".pl", ".com")):
            raise ValueError("Blad maila -zla domena")
        
        if not isinstance(data.get("age"),int):
            raise ValueError("Blad wieku - to nie jest liczba")
        if not data.get("age") >= 18:
            raise ValueError("Blad wieku - nie masz 18 lat")
        
        if not data.get("name").isalnum():
            raise ValueError("Blad nazwy - niedozwolone znaki specjalne")
        
        if any(char.isdigit() for char in data.get("name")):
            raise ValueError("Blad nazwy - nazwa nie moze zawierac cyfr")
        
        print("udalo sie zalogowac")
        return True
    except Exception as error:
        print(error)
        return False