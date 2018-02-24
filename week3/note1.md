# TUPLES

>how to create

````python
te = ()
t = (2,"one",3)
t[0]
(2,"one",3) + (5,6)
t[1] = 4 (warning, we can not change the tuple)
('one',) (is a tuple)
('one') (is not a tuple)
t[0:1] = (2,)
````

>exchange

````python
#way 1
temp = x
x = y
y = temp
#way 2
(x, y) = (y, x)
````

```
x = (1, 2, (3, 'John', 4), 'Hi')
```

# LIST

>List is mutable, while tuples not.

````python
a_list = []
b_list = [2,'a',4,True]
L = [2, 1, 3]
````

## OPERATION

````python
L = [2,1,3]
L.append(5)
L1 = [2,1,3]
L2 = [4,5,6]
L3 = L1 + L2 (L3 = [2,1,3,4,5,6])
L1.extend([0,6])(L1 = [2,1,3,0,6])

del(L1[3])(L1 = [2,1,3,6])
s = 'abc'
list(s) (['a', 'b', 'c'])

L = [9,6,0,3]
sorted（L）（L itself is not sorted, only return a sorted copy of L)
L.sort()(L itself is sorted)
L.reverse()(L is reversed)
L[0:1] = [9]
````

```
listB = ['x', 'z', 't', 'q']
```

# ALIASES

````python
warm = ['red', 'yellow', 'orange']
hot = warm
hot.append('pink') (warm is also appended)

cool = ['blue', 'green', 'grey']
chill = ['blue', 'green', 'grey']
(they are not pointed to a same list)

cool = ['blue', 'green', 'grey']
chill = cool[:]
(chill is a copy of cool. Like the example two)

warm = ['yellow', 'orange']
hot = ['red']
brightcolors = [warm]
birghtcolors.append(hot)(alias)
hot.append('pink')
print(hot + warm)
````



````python
def remove_dups(L1,L2):
	for e in L1:
		if e in L2:
			L1.remove(e)
L1 = [1,2,3,4]
L2 = [1,2,5,6]
remove_dups(L1, L2)
# it's wrong. When the remove happens. It decreses the size of the list. On account of this, it skips the 2 in L1.
````

**You should write it this way in python**

````python
def remove_dups(L1,L2):
	L1_copy = L1[:]
	for e in L1_copy:
		if e in L2:
			L1.remove(e)
L1 = [1,2,3,4]
L2 = [1,2,5,6]
remove_dups(L1, L2)
# this exmple is ok!!!
````



# MAPS

````python
map(abs, [1,-2,3,-4])
for elt in map(abs, [1,-2,3,-4]):
	print(elt)
([1,2,3,4])
map(min, L1, L2) generizes a smaller list
````

