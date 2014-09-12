__author__ = 'asjed'
from  math import *
import math


def bisection(f, a, b, TOL=0.001, NMAX=100):
    n=1
    while n<=NMAX:
        c = (a+b)/2.0
        if f(c)==0 or (b-a)/2.0 < TOL:
            return c
        else:
            n = n+1
            if f(c)*f(a) > 0:
                a=c
            else:
                b=c
    return False


def fun(x):
      return x**3

if __name__ == "__main__":

    def func(x):
        """
        Function x^2
    We will calculate the root of this function using different methods.
    """
        return x**2


    def func_(x):
        """
        Function 1/x
    We will calculate the root of this function using different methods.
    """
        return 1/x

    def func(x):
        """
        Function x**3
    We will calculate the root of this function using different methods.
    """
        return x**2


    #Invoking Bisection Method
    ren = bisection(func,-2,2)
    ree= bisection(func,-2,2)
    ren= bisection(func,0.1,0.2)
    ren= bisection(func,1,1)
    print (ren,ren,ren,ren)


