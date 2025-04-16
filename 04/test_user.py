import pytest
from user import validate_user


@pytest.fixture
def sample_data():
    return {
        'user1': {'email': 'test@test.com',
                  'age': 18,
                  'name': 'Jakub'},
        'user2': {'email': 'testtest.com',
                  'age': 17,
                  'name': 'Jakub'}
    }


def test_valid_user_data(sample_data):
    email = sample_data['user1']['email']
    age = sample_data['user1']['age']
    name = sample_data['user1']['name']
    assert validate_user(email, age, name) == True


def test_invalid_user_data(sample_data):
    email = sample_data['user2']['email']
    age = sample_data['user2']['age']
    name = sample_data['user2']['name']
    assert validate_user(email, age, name) == False
