import pytest
from user import validate_user


@pytest.fixture
def sample_data():
    return {
        'user': {'email': 'test@test.com',
                 'age': 18,
                 'name': 'Jakub'}
    }


def test_valid_user_data(sample_data):
    email = sample_data['user']['email']
    age = sample_data['user']['age']
    name = sample_data['user']['name']
    assert '@' in email
    assert email.endswith('.pl') or email.endswith('.com')
    assert isinstance(age, int)
    assert age >= 18
    assert name.isalpha()
