"""TestsMidModuel
    """

import pytest
from only_ints import only_ints


@pytest.mark.parametrize("test_input1,test_input2,expected", [(1, 2, True), (-1, 200, True), (0, 0, True), (-2360, -2970, True)])
def test_both_ints(test_input1, test_input2, expected):
    """Test True for test inputs beeing integers"""
    assert only_ints(test_input1, test_input2) == expected


@pytest.mark.parametrize("test_input1,test_input2,expected", [(1, "2", False), ("-1", 200, False), ("0", 0, False), ("-2360", "-2970", False), (1.2, 1, False)])
def test_not_both_ints(test_input1, test_input2, expected):
    """Test True for test inputs beeing integers"""
    assert only_ints(test_input1, test_input2) == expected
