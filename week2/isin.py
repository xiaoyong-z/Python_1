def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    start = 0
    end = len(aStr)
    middle = (start + end) // 2
    if len(aStr) == 0:
        return False
    if len(aStr) == 1:
        return aStr[0] == char
    if aStr[middle] == char:
            return True
    elif aStr[middle] > char:
            return isIn(char, aStr[:middle])
    elif aStr[middle] < char:
            return isIn(char, aStr[middle:])

if isIn('w', 'eeefffffffffffffffffwwwwwwwwwwwwwzzzzzzzzzz'):
    print("YES")
else:
    print("NO")