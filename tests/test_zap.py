"""TestsMidModuel
    """

import pytest
from app.internal.zap import zap


@pytest.mark.parametrize("test_input1,test_input2,expected", [(["a", "b", "c"], [1, 2, 3], [("a", 1), ("b", 2), ("c", 3)])])
def test_both_ints(test_input1, test_input2, expected):
    """Test True for test inputs beeing integers"""
    assert zap(test_input1, test_input2) == expected
