"""FormatNumberModuel"""


def format_number(number: int) -> str:
    """Returns a

    Side note: to do it this way: return "{:,}".format(number) 
    felt like cheating.

    Args:
        number: must be integer

    Returns:
        string of number with dot at each 10^3 position
    """
    if number < 0:
        raise Exception
    number = str(
        number)
    for i in range(len(number)-3, 0, -3):
        number = str(number)[:i] + "." + str(number)[i:]
    return number
