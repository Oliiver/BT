"""ConverModuel"""


def convert(list: list[int] | list[float]) -> list[str]:
    """takes in a list of numbers and returns a list of strings of each number

    Args:
        list (list): list of numbers

    Returns:
        list[str]: list of strings of the original numbers
    """
    return [str(i) for i in list if (isinstance(i, int) or isinstance(i, float))]
