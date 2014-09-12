__author__ = 'asjed'

from  math import *

def secant(f,x0,x1, TOL=1e-6, NMAX=100):
    """
    Takes a function f, start values [x0,x1], tolerance value(optional) TOL and
    max number of iterations(optional) NMAX and returns the root of the equation
    using the secant method.
    """
    n=1
    while n<=NMAX:
        x2 = x1 - f(x1)*((x1-x0)/(f(x1)-f(x0)))
        if x2-x1 < TOL:
            return x2
        else:
            x0 = x1
            x1 = x2
    return False

def newtonraphson(f, f_, x0, TOL=1e-6, NMAX=100):
    """
    Takes a function f, its derivative f_, initial value x0, tolerance value(optional) TOL and
    max number of iterations(optional) NMAX and returns the root of the equation
    using the newton-raphson method.
    """
    n=1
    while n<=NMAX:
        x1 = x0 - (f(x0)/f_(x0))
        if x1 - x0 < TOL:
            return x1
        else:
            x0 = x1
    return False

if __name__ == "__main__":

    def func(x):
        """
        Function sin(x)+cos(x)
    We will calculate the root of this function using different methods.
    """
        return sin(x)+cos(x)

    def funcc(x):
        """
        Function x**3
    We will calculate the root of this function using different methods.
    """
        return x**3

    def func_(x):
        """
        Derivative of the function f(x) = sin(x)
        This will be used in Newton-Rahson method.
        """
        return cos(x)+sin(x)

    def funcc_(x):
        """
        Derivative of the function f(x) = x**3
        This will be used in Newton-Rahson method.
        """
        return 3*x**2




    #Invoking Secant Method
    res =secant(func,pi/2,3*(pi/2), 1e-6)
    rees = secant(func,-pi/2,pi/2, 1e-6)
    rms = res =secant(funcc,5,6, 1e-9)
    print (res, rees,rms)


    #Invoking Newton Raphson Method
    nes = newtonraphson(func,func_,pi/2,1e-6)
    nees= newtonraphson(func,func_,-pi/2,1e-6)
    nms = newtonraphson(funcc,funcc_,5,1e-9)
    print (nes,nees,nms)