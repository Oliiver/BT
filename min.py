def min(string: str) -> str:
    return "" if len(string) % 2 == 0 else string[len(string)//2]
