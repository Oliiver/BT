"""TestsFormatNumberModuel
    """
import pytest
from app.internal.format_number import format_number


@pytest.mark.parametrize("test_input,expected", [(123456, "123.456"), (0, "0"), (12, "12"), (100, "100"), (000000, "0"), (12345, "12.345"), (1234, "1.234")])
def test_numbers(test_input, expected):
    """Test different lengths of numbers"""
    assert format_number(test_input) == expected
