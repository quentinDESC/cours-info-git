def f(x):
    return x+1

def g(x): 
    return 0
def f2(x):
    return 9

def f3(x):
    return 5

def sqrt (x):
    return x**(1/2)

import numpy as np
a,b=np.indices((10,10))

def rayures(n):
    a,b=np.indices((n,n))
    print (a%2)
    
    
def damier(n):
    a,b=np.indices((n,n))
    print((a+b)%2)
    

def escalier(n):
    a,b=np.indices((n,n))
    print (a<b)
    
def damier_par_bloc(n):
    a,b=np.indices((n,n))
    a=a%3
    b=b%3
    a= (a==0)
    b= (b==0)
    c= a +b
    print (c)
