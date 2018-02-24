def oddTuples(aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup.
    '''
    i = 0
    tu = ()
    length = len(aTup)
    while i < length:
        tu = tu + (aTup[i],)
        i = i + 2
    return tu