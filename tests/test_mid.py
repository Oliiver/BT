"""Tests for mid moduel
    """

import pytest
from mid import mid


@pytest.mark.parametrize("test_input,expected", [("odd", "d"), ("i", "i"), ("C++", "+")])
def test_odd_length(test_input, expected):
    """Test correct middle letter gets returned for strings of odd length"""
    assert mid(test_input) == expected


@pytest.mark.parametrize("test_input,expected", [("even", ""), ("PYTHON", ""), ("!§$%&()}", "")])
def test_even_length(test_input, expected):
    """Test empty string gets returned for strings of even lengths"""
    assert mid(test_input) == expected


def test_empty_length():
    """Test empty string gets returned for the empty string"""
    string = ""
    result = mid(string)
    assert result == ""


def test_int():
    """Test Exception raised for wrong type."""
    with pytest.raises(Exception):
        mid(0)
