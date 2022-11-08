import pytest
from min import min


@pytest.mark.parametrize("test_input,expected", [("odd", "d"), ("i", "i"), ("C++", "+")])
def test_odd_length(test_input, expected):
    assert min(test_input) == expected


@pytest.mark.parametrize("test_input,expected", [("even", ""), ("PYTHON", ""), ("!§$%&()}", "")])
def test_even_length(test_input, expected):
    assert min(test_input) == expected


def test_empty_length():
    string = ""
    result = min(string)
    assert result == ""


def test_int():
    with pytest.raises(Exception):
        min(0)
