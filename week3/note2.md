# DICTIONARY

````python
my_dict = {}
grades = {'Ana':'B', 'John':'A+','Denise':'A','Katy':'A'}
grades['John']
grades['Ana']
grades['Sylvan'] = 'A' (add a item)
'John' in grades(True)
'Daniel' in grades(False)
del(grades['Ana'])(Delete an entry)
grades.keys()(Give back the keys)
grades.values()(Give back the values)
````



# FIBONACCI

* fibonacci isn't efficient in recursive solve

  ````
  def fib_efficient(n,d):
  	if n in d:
  		return d[n]
  	else:
  		ans = fib_efficient(n-1,d) + fib_efficient(n-2,d)
  		d[n] = ans
  		return ans
  d = {1:1, 2:2}
  ````

# GLOBAL_VARIABLE

* You can track the times of the function called using the global_variable.

