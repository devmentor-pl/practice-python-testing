import pytest
from user import validate_user

@pytest.fixture
def correct_user_data():
    return {
    "email": "jacek@gmail.com",
    "age": 18,
    "name": "jacek"
    }
    

def test_validate_user(correct_user_data): 
    assert validate_user(correct_user_data) == True


@pytest.fixture
def valid_user_data_email():
    return {
    "email": "jacekgmail.com",
    "age": 18,
    "name": "jacek"
    }
    

def test_validate_user_email(valid_user_data_email): 
    assert validate_user(valid_user_data_email) == False

@pytest.fixture
def valid_user_data_age():
    return {
    "email": "jacekgmail.com",
    "age": 16,
    "name": "jacek"
    }
    

def test_validate_user_age(valid_user_data_age): 
    assert validate_user(valid_user_data_age) == False

@pytest.fixture
def valid_user_data_name():
    return {
    "email": "jacekgmail.com",
    "age": 19,
    "name": "Maciek!"
    }
    

def test_validate_user_name(valid_user_data_name): 
    assert validate_user(valid_user_data_name) == False

