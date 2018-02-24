def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    if exp == 0:
        return 1.0
    else:
        return base * recurPower(base, exp - 1)


def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    result = 1.0
    if exp == 0:
        return result
    while exp > 0:
        result *= base
        exp -= 1
    return result