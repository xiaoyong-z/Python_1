# OBJECTS

* type
* an internal data representation
* a set of procedures for interaction with the object



## OOP

* DATA
* INTERFACE

1. DATA ATTRIBUTES

````python
class Coordinate(object):
	def __init__(self, x, y):(constructive  function)
		self.x = x
		self.y = y
Coordinate(3, 4) (create an Coordinate object and its x is 3 its y is 4)
# ATTRIBUTES INCLUDE DATA ATTRIBUTES AND METHODS
````

2. METHODS（FUNCTION）

````python
class Coordinate(object):
	def __init__(self, x, y):(constructive  function)
		self.x = x
		self.y = y
	def distance(self, other):
		x_diff_sq = (self.x - other.x) ** 2
		y_diff_sq = (self.y - other.y) ** 2
		return (x_diff_sq + y_diff_sq) ** 0.5
    def __str__(self):
      	return "<" + str(self.x) + "," + str(self.y) + ">" # use for print
c.distance(origin)
Coordinate.distance(c, origin)
print(isinstance(c, Coordinate))
````



## EXAMPLE: FRACTIONS

````python
class fraction(object):
    tag = 1(class variable)
	def __init__(self, numer, denom):
		self.numer = numer(INSTANCE VARIABLE)
		self.denom = denom
	def __str__（self):
		return str(self.numer) + ' / ' + str(self.denom)
	def getNumer(self):
		return self.numer
	def getDenom(self):
		return self.denom
	def __add__(self, other)
		...
oneHalf = fraction(1, 2)
twoThirds = fraction(2, 3)
````

###GENERATOR
````python
def genTest():
    yield 1
    yield 2
foo = genTest()
foo.__next__()
1
foo.__next__()
2
foo.__next__()
raise StopIteration

def genFib():
    fibn_1 = 1
    fibn_2 = 0
    while True:
        next = fibn_1 + fibn_2
        yield next
        fibn_2 = fibn_1
        fibn_1 = next
fib = genFib()
fib.__next__()
1
fib.__next__()
2
fib.__next__()
3
# return something you need
````



