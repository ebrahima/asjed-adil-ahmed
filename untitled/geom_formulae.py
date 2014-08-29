__author__ = 'asjed'


import math
from numpy import *


def circle_area(radius):
    """
    calculate area of a circle
    :param radius: radius of a circle
    :return:area of a circle(in square units of radius)
    """
    r2 = radius**2
    return math.pi*r2
print(circle_area(5))

def rectangle_area(length, width):
    """
    calculate area of a rectangle
    :param length: length of a rectangle
    :param width: width of a rectangle
    :return:area of a rectangle
    >>> rectangle_area(3,2)
    6
    """
    return length*width

print(rectangle_area(3, 2))

def triangle_area(base, heigt):
    """
    calculate area of a triangle
    :param base: base of atringle
    :param heigt:
    :return:
    """
    b = base
    h = heigt
    return 1/2*b*h

print(calculate_area_triangle(2, 4))

def calculate_area_rectangle(length, width):
    l = length
    w = width
    return l*w

print(calculate_area_rectangle(2, 4))
