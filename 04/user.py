def validate_user(data):

    email = sample_data['user']['email']
    age = sample_data['user']['age']
    name = sample_data['user']['name']

    if '@' not in email:
        return False
    if not (email.endswith('.pl') or email.endswith('.com')):
        return False
    if not isinstance(age, int):
        return False
    if age < 18:
        return False
    if not name.isalpha():
        return False

    return True
