__author__ = 'asjed'


import math
from numpy import *


def circle_area(radius: Number) -> Number:
    """
    calculate area of a circle given the radius.

    @param radius: radius of a circle
    @return: the area (unit^2 given radius)

    >>>circle_area(2)
    """
    return pi*radius**2
print(circle_area(2))

def rectangle_area(length, width):
    """
    calculate area of a rectangle
    :param length: length of a rectangle
    :param width: width of a rectangle
    :return:area of a rectangle
    >>> rectangle_area(3,2)
    6
    """
    return lenght * widgth

print(rectangle_area(3, 2))


def triangle_area(base, height):
    """
    calculate area of a triangle.
    :param base: base of a triangle
    :param height: height of a triangle
    :return:area of a triangle
    >>>triangle_area(2, 4)
    """
    return 0.5 * base * height

print(triangle_area(2, 4))


def sphere_volume(radius):
    """
    calculate volume of a sphere

