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

def rectangle_area(side, length):
    """
    calculate area of a rectangle.

    @param side: side of rectangle
    @param length: length of rectangle
    @return: the area(different units as side length)

    >>> rectangle_area(3,2)

    """
    return sids*length

print(rectangle_area(3, 2))


def triangle_area(base, height):
    """
    calculate area of a triangle.
    @param base: base of triangle
    @param height: height of triangle
    @return: the area (same unite as base height)
    >>>triangle_area(2, 4)
    """
    return 0.5 * base*height

print(triangle_area(2, 4))


def sphere_volume(radius):
    """
    calculate volume of a sphere.
    @param radius: radius of sphere
    @return: the volume (unit^3 from radius)
    >>>sphere_volume(4)
    """
    return 4*pi*radius*radius*radius/3

print(sphere_volume(4))


def cylinder_volume(radius, height):
    """
    calculate volume of a cylinder.
    @param radius: radius of cylinder
    @param height: height of cylinder
    @return: the volume (same units as radius height)
    """
    return pi*radius**2*height

print(cylinder_volume(2, 3))


