import pytest
from user import validate_user

@pytest.fixture
def valid_user_data():
    return {"email": "abc@abc.com", "age": 19, "name": "Łukasz"}
 
def test_validate_user(valid_user_data):
    assert validate_user(valid_user_data) is True
    
def test_validate_user_email_at(valid_user_data):
    data = valid_user_data.copy()
    data["email"]="abcabc.com"
    assert validate_user(data) is False
    
def test_validate_user_email_end(valid_user_data):
    data = valid_user_data.copy()
    data["email"]="abc@abc.dev"
    assert validate_user(data) is False
    
def test_validate_user_email_end_2(valid_user_data):
    data = valid_user_data.copy()
    data["email"]="abc@abc.pl"
    assert validate_user(data) is True
    
def test_validate_user_age_int(valid_user_data):
    data = valid_user_data.copy()
    data["age"]=19.5
    assert validate_user(data) is False
    
def test_validate_user_age_adult(valid_user_data):
    data = valid_user_data.copy()
    data["age"]=17
    assert validate_user(data) is False
    
def test_validate_user_age_18(valid_user_data):
    data = valid_user_data.copy()
    data["age"] = 18
    assert validate_user(data) is True
    
def test_validate_user_name_digit(valid_user_data):
    data = valid_user_data.copy()
    data["name"]="Łukasz9"
    assert validate_user(data) is False
    
def test_validate_user_name_special_char(valid_user_data):
    data = valid_user_data.copy()
    data["name"]="Łukasz!"
    assert validate_user(data) is False
    
def test_validate_user_empty_name(valid_user_data):
    data = valid_user_data.copy()
    data["name"] = ""
    assert validate_user(data) is False