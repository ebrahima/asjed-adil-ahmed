__author__ = 'asjed'
import math
from numpy import *
def circle_area(radius):
    """
    calculate area of a circle
    :param radius: radius of a circle
    :return:
    """
    r2 = radius**2
    return math.pi*r2
print(circle_area(5))

def calculate_area_square(side):
    r = side
    return r*r

print(calculate_area_square(2))

def calculate_area_triangle(base, heigt):
    b = base
    h = heigt
    return 1/2*b*h

print(calculate_area_triangle(2, 4))

def calculate_area_rectangle(length, width):
    l = length
    w = width
    return l*w

print(calculate_area_rectangle(2, 4))
