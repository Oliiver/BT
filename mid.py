"""MidModuel"""


def mid(string: str) -> str:
    """Returns the middle letter of a string.

    Args:
        string (str): string to find the middle letter of

    Returns:
        str: middle letter if odd and the empty string if even
    """
    return "" if len(string) % 2 == 0 else string[len(string)//2]
