import pytest
from promo import is_valid_promo

@pytest.mark.parametrize("code, expected", [
    (int(1234567890), False),
    (float(1234567890), False),
    (True, False),
    ("Way_too_long", False),
    ("Too_short", False),
    ("Randomcode", False),
    ("RNDMCODE_!", False),
    ("RANDMCODE1", False),
    ("RNDMCODE01", True),
    ("RN09DMCODE", True),   
    ("1234567890", True),
])
def test_is_valid_promo(code, expected):
    assert is_valid_promo(code) == expected
