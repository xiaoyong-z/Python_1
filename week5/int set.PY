class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'

    def intersect(self, other):
        """Assumes other is an intSet
                   Returns a new intSet containing elements that appear in both sets."""
        newSet = intSet()
        for i in self.vals:
            if i in other.vals:
                newSet.insert(i)
        return newSet

    def __len__(self):
        return len(self.vals)

setA = {-19,-14,-2,5,6,8,10,15,19}
setB = {-20,-18,-10,-6,-4,1,4,6,7,18}
setA.intersect(setB)