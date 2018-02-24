def applyF_filterG(L, f, g):
    """
    Assumes L is a list of integers
    Assume functions f and g are defined for you.
    f takes in an integer, applies a function, returns another integer
    g takes in an integer, applies a Boolean function,
        returns either True or False
    Mutates L such that, for each element i originally in L, L contains
        i if g(f(i)) returns True, and no other elements
    Returns the largest element in the mutated L or -1 if the list is empty
    """
    if len(L) == 0:
        return -1
    temp = L[:]
    for i in range(len(temp)):
        if not g(f(temp[i])):
            L.remove(temp[i])
    max = 0
    for i in range(len(L)):
        if L[i] > L[max]:
            max = i
    if len(L) == 0:
        return -1
    return L[max]


def f(i):
    return i + 2

def g(i):
    return i > 5

L = [-6,-2,-3]
print(applyF_filterG(L, f, g))
print(L)