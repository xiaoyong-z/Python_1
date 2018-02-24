#decompostion and abstration
1. decompostion : function, class
2. abstration: a blank box

##function

example:

````
def is_even(i):
    ```
    input: int
    output: boolean
    ```
    print("hi")
    return i % 2 == 0
is_even(3)
````

=========================================================================


> 1 :  We can't change the global value outside the function(If the variable is defined after the function). We can only look at them.

***WRONG***
````

def h(y):
    x = x + 1
x = 5
h(2)
print(x)
````

***OK***
````
x = 12
def g(x):
   x = x + 1
   def h(y):
      return x + y
   return h(6)
g(x)
````
===========================================================================


>  2 : You can choose to reverse the parameter in the call like the following case.

````
def printName(firstName, lastName, reverse):
    if reverse:
        print(lastName + ', ' + firstName)
    else:
        print(firstName, lastName)
printName(lastName = 'Grimson', firstName = 'Eric', reverse = False)
````
### DIVIDE AND CONQUER ALOGORITHM
***The answer is Eric Grimson***

>  3 : ***FIBONACCI*** 
* base case fib(0) = 0 fib(1) = 0
* fib(n) = fib(n - 1) - fib(n - 2)

>  4 : ***alindrome***
````
def isPalindrome(s):
    def toChars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcedfghijklmnopqrstuvwxyz':
                ans = ans + c
    def isPal(s):
        if len(s) <= 1:   #BASE CASE
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1]) #RECURSIVE STEPS
    return isPal(toChars(s))
````


###module
* we have circle.py
* **import circle** (circle.pi)
* from circle import *  (pi)(you can use it if it's not collided)

### FILES
***write***
````
nameHandle = open('Kids', 'w')
for i in range(2):
    name = input('Enter name:')
    nameHandle.write(name + '\')
nameHandle.close()
````
***read***
````
nameHandle = open('Kids','r')
for line in nameHandle:
    print(line)
nameHandle.close()
````