def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return


def new_string(symbol, count=3):
    return symbol * count


def concatenatio(*params):
    res: str = ""  # res: int = 0
    for item in params:
        res += item
    return res
