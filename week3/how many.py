def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    big = 0
    big_i = 0
    for i in aDict.keys():
        if len(aDict[i]) > big:
            big = len(aDict[i])
            big_i = i
    return big_i

print(how_many({'B': [15], 'u': [10, 15, 5, 2, 6]}))
