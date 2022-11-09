"""ZapModuel"""


def zap(list1: list, list2: list) -> list[tuple]:
    """Returns a list of tuples consiting of the elements of the two
    input lists

    Args:
        list1 (list): list of any values
        list2 (list): list of any values

    Returns:
        list[tuple]: list of tuples
    """
    return [(list1[i], list2[i]) for i in range(min(len(list1), len(list2)))]
