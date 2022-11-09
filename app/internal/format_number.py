"""FormatNumberModuel"""


def format_number(number: int) -> str:
    """Returns a list of tuples consiting of the elements of the two
    input lists 
    Side note: to do it this way:
                return "{:,}".format(number) 
    felt like cheating.

    Args:
        list1 (list): list of any values
        list2 (list): list of any values

    Returns:
        list[tuple]: list of tuples
    """
    number = str(
        number)                                      # Runtime: 26 ms, faster than 93.84%
    for i in range(len(number)-3, 0, -3):
        number = str(number)[:i] + "." + str(number)[i:]
    return number
