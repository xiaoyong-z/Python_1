##Generating guesses

1. Exhaustive enumeration              (liner)
2. Bisection search                    (log)
3. Newton-Raphson                      ()
##the concrete code
````
#Bisection search
import math  
from math import sqrt  
  
def sqrt_binary(num):  
    x=sqrt(num)  
    y=num/2.0  
    low=0.0  
    up=num*1.0  
    count=1  
    while abs(y-x)>0.00000001:  
        print count,y  
        count+=1          
        if (y*y>num):  
            up=y  
            y=low+(y-low)/2  
        else:  
            low=y  
            y=up-(up-y)/2  
    return y  
  
print(sqrt_binary(5))  
print(sqrt(5))  
````


````
#Newton-Raphson
def cube_newton(num):  
    x=num/3.0  
    y=0  
    count=1  
    while abs(x-y)>0.00000001:  
        print count,x  
        count+=1  
        y=x  
        x=(2.0/3.0)*x+(num*1.0)/(x*x*3.0)  
    return x  
  
print(cube_newton(27))   ````



