__author__ = 'asjed'

from numpy import *
from numbers import Number

def circle_area(radius):
    """
    calculate area of a circle given the radius.

    :param radius: radius of a circle
    :return: the area (unit^2 given radius)

    >>>circle_area(2)
    """
    return pi*(radius**2)
if __name__ == "__main__":
    sampleradius = 2
    print("area:",
    circle_area(sampleradius))

def rectangle_area(side, length):
    """
    calculate area of a rectangle.

    :param side: side of rectangle
    :param length: length of rectangle
    :return: the area(different units as side length)

    >>> rectangle_area(3,2)

    """
    return side*length
if __name__ == "__main__":
    sampleside = 3
    samplelength = 2
print("area:",
      rectangle_area(sampleside,samplelength))


def triangle_area(base, height):
    """
    calculate area of a triangle.
    :param base: base of triangle
    :param height: height of triangle
    :return: the area (same unite as base height)
    >>>triangle_area(2, 4)
    """
    return 0.5 * base*height
if __name__=="__main__":
    samplebase = 2
    sampleheight = 4
print("area:",
      triangle_area(samplebase,sampleheight))


def sphere_volume(radius):
    """
    calculate volume of a sphere.
    :param radius: radius of sphere
    :return: the volume (unit^3 from radius)
    >>>sphere_volume(4)
    """
    return 4*pi*radius*radius*radius/3
if __name__=="__main__":
    samplradius = 4
print("volume:",
      sphere_volume(sampleradius))


def cylinder_volume(radius, height):
    """
    calculate volume of a cylinder.
    :param radius: radius of cylinder
    :param height: height of cylinder
    :return: the volume (same units as radius height)
    """
    return pi*radius**2*height
if __name__=="__main__":
    sampleraidus = 2
    sampleheight = 3
print("volume:",
      cylinder_volume(sampleradius,sampleheight))

def cone_volume(radius, height):
    """
    calculate the volume of cone.
    :param radius: radius of cone
    :param height: height of cone
    :return: the volume of the cone
    """
    return 4*radius*radius*height*0.333
if __name__=="__main__":
    sampleradius = 2
    sampleheight = 5
print("volume:",
      cone_volume(sampleradius,sampleheight))

def disk_ambient(quarter):
    """
    calculate the ambient of disk
    :param quarter: quarter of disk
    :return: the ambient of the disk
    """
    return pi*quarter
if __name__=="__main__":
    samplequarter = 7
print("ambient:",
      disk_ambient(samplequarter))



