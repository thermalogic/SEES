# 8.1 Abstract Data Types and Classes

# 0

# Page 93, Figure 8.1

class IntSet(object):
    """An intSet is a set of integers"""
    # Information about the implementation (not the abstraction)
    # The value of the set is represented by a list of ints, self.vals.
    # Each int in the set occurs in self.vals exactly once.

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

    def getMembers(self):
        """Returns a list containing the elements of self.
           Nothing can be assumed about the order of the elements"""
        return self.vals[:]

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        result = ''
        for e in self.vals:
            result = result + str(e) + ','
        return('{' + result[:-1] + '}')  # -1 omits trailing comma

# Page 92
print(type(IntSet), type(IntSet.insert))

# Page 94
s = IntSet()
s.insert(3)
print(s.member(3))

# Page 95
s = IntSet()
s.insert(3)
s.insert(4)
print(s)
