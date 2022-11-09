"""Test Convert Module"""

import pytest
from app.internal.convert import convert


@pytest.mark.parametrize("test_input,expected", [([1.2, 1, 3.14, 2000000000], ["1.2", "1", "3.14", "2000000000"])])
def test_mixed_list(test_input, expected):
    """Test correct list return for input list of mixed values"""
    assert convert(test_input) == expected


@pytest.mark.parametrize("test_input,expected", [([], [])])
def test_empty_list(test_input, expected):
    """Test empty list return for input empty list"""
    assert convert(test_input) == expected


@pytest.mark.parametrize("test_input,expected", [([1, 2, 3, 4, 5, 10000000000000000000000000000, 232302302391283], ["1", "2", "3", "4", "5", "10000000000000000000000000000", "232302302391283"])])
def test_numbers_only_list(test_input, expected):
    """Test correct list return for input list of only number values"""
    assert convert(test_input) == expected
