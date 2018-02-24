# EXCEPTIONS(control flows) AND ASSERTIONS (input, output)

* trying to access beyond list limits
* trying to convert an inappropriate types
* ...

WHAT TO DO WITH EXCEPTIONS

* RETURN AN ERROR VALUE
* STOP EXEmylist = [10, 20, 30] 
  mylist.index(11)
* CUTION, SIGNAL ERROR CONDITION

````
try:
	execution codes(if succeed, skip the except. Otherwise, jump immediately to the except)
except:
	exception raises
````



````
try:
	codes...
except ValueError: 
	codes...
except ZeroDivisonError:
	codes...
except:
	codes...
else: (try works correctly)
finally: (always executed after try,else,except, even if they raise an error or executed a break,continue, return)
````





````
raise <exceptionName> <arguments>
raise ValueError ""
````



## ASSERTIONS

````
assert not len(grades) == 0, 'no grades data'
raises an AssertionError if it is given an empty list for grades

````



* having assertion on both input and output of the function
  find debugs
* check type,constraints,violations(e.g. no duplicates), invariants(不变性)