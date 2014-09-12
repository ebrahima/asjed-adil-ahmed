__author__ = 'asjed'


import numpy as np



def simpsons(f, a, b, n):
    deltaX= (a-b)/ n
    points = np.linspace(a, b, n+1)
    fpoints = f(points)
    res = fpoints[0] + fpoints[-1]
    z = np.zero(n-1)
    z[0:n:2] = 4
    z[1:n:2] = 2
    res += np.sum(z*points[1:-1])
    return deltaX/3*res



    pass


def midpoint(f,a,b,n):
    deltaX = (a-b)/n
    print(deltaX)
    start = a + deltaX/2
    end = b - deltaX/2
    print(start, end)
    mid = np.linspace(start, end, n)
    print(mid)
    fs = f(mids)
    fsum = np.sum(fs)
    return deltaX*fsum


    pass


def trapezoid(f,a,b,n):
    delteX = (b-a)/n
    points = np.linspace(a, b, n+1)
    print (points)
    fpoints = f(points)

    res = fpoints[0]+fpoints[-1]+fpoints[1:-1]+2*fpoints[-1:1]
    return res * deltaX/2
 poly_coeffes
    pass
