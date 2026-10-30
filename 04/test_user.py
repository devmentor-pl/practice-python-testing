import pytest
from user import validate_user

@pytest.fixture
def valid_user_data():
    return {
        1: {"email": "John@example.com", "age": 45, "name": "John"},
        2: {"age": 45, "name": "John"},
        3: {"email": "John.example.com", "age": 45, "name": "John"},
        4: {"email": "John@example.de", "age": 45, "name": "John"},
        5: {"email": "John@example.com", "age": 7, "name": "John"},
        6: {"email": "John@example.com", "age": 45.6, "name": "John"},
        7: {"email": "John@example.com", "age": 45, "name": "John5"},
        8: {"email": "John@example.com", "age": 45, "name": "John!"},
    }

def test_validate_user(valid_user_data):
    assert validate_user(valid_user_data.get(1)) == True
    assert validate_user(valid_user_data.get(2)) == False
    assert validate_user(valid_user_data.get(3)) == False    
    assert validate_user(valid_user_data.get(4)) == False
    assert validate_user(valid_user_data.get(5)) == False
    assert validate_user(valid_user_data.get(6)) == False
    assert validate_user(valid_user_data.get(7)) == False
    assert validate_user(valid_user_data.get(8)) == False

"""
Będąc uczciwym - nie wiem, czy rozwiąząłem ćwiczenie tak, jak powinno ono zostać rozwiązane. Na pewno "test_validate_user()" testuje wszystkie przypadki, które były wylistowane do weryfikacji. Natomiast nie mam pewności czy sposób budowy testów jest taki, jak było to oczekiwane. Mogę to popoprawiać po otrzymaniu uwag.
"""