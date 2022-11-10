"""OnlyIntsModuel"""


def only_ints(num1: float | int, num2: float | int) -> bool:
    """Takes in two numbers. If they are both integers 
    return true else false.

    Args:
        num1 (int):
        num2 (int):

    Returns:
        bool: True if num1 and num2 are integers False otherwise
    """
    return (isinstance(num1, int) and isinstance(num2, int))