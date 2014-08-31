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
    calculate area of a rectangle from side length.

    :param side: side of rectangle
    :param length: length of rectangle
    :return: the area(unit^2 as side)

    >>> rectangle_area(3, 2)

    """
    return side*length
if __name__ == "__main__":
    sampleside = 3
    samplelength = 2
print("area:",
      rectangle_area(sampleside, samplelength))


def triangle_area(base, height):
    """
    calculate area of a triangle.from base height.

    :param base: base of triangle
    :param height: height of triangle
    :return: the area (unit^2 from base)

    >>>triangle_area(2, 4)
    """
    return 0.5 * base*height
if __name__ == "__main__":
    samplebase = 2
    sampleheight = 4
print("area:",
      triangle_area(samplebase, sampleheight))


def sphere_volume(radius):
    """
    calculate volume of a sphere from radius.

    :param radius: radius of sphere
    :return: the volume (unit^3 from radius)

    >>>sphere_volume(4)
    """
    return 4*pi*radius*radius*radius/3
if __name__ == "__main__":
    samplradius = 4
print("volume:",
      sphere_volume(sampleradius))


def cylinder_volume(radius, height):
    """
    calculate volume of a cylinder.

    :param radius: radius of cylinder
    :param height: height of cylinder

    :return: the volume (unit^3 from radius)
    >>>cylinder_volume(2, 3)
    """
    return pi*radius**2*height
if __name__ == "__main__":
    sampleraidus = 2
    sampleheight = 3
print("volume:",
      cylinder_volume(sampleradius, sampleheight))


def cone_volume(radius, height):
    """
    calculate the volume of cone.from radius height

    :param radius: radius of cone
    :param height: height of cone

    :return: the volume (units^3)
    >>>cone_volume(2, 5)
    """
    return 4*radius*radius*height/3
if __name__ == "__main__":
    sampleradius = 2
    sampleheight = 5
print("volume:",
      cone_volume(sampleradius, sampleheight))


def disk_ambient(quarter):
    """
    calculate the ambient of disk from quarter.

    :param quarter: quarter of disk

    :return: the ambient (units from quarter)
    >>>disk_ambient(7)
    """
    return pi*quarter
if __name__ == "__main__":
    samplequarter = 7
print("ambient:",
      disk_ambient(samplequarter))


def trapezium_area(b1, b2, height):
    """
    calculate the area of trapezium from b1 b2 height

    :param b1: upper side of trapezium
    :param b2: lower side of trapezium
    :param height: height of trapezium

    :return:the area (units^2)
    >>>trapezium_area(2, 3, 4)
    """
    return 0.5*(b1+b2)*height
if __name__ == "__main__":
    sampleb1 = 2
    sampleb2 = 3
    sampleheight = 4
print("area:",
      trapezium_area(sampleb1, sampleb2, sampleheight))


def pentagon_area(side, height):
    """
    calculate the area of pentagon from side height.

    :param side: side of pentagon
    :param height: height of pentagon

    :return:the area (units^2)
    >>>pentagon_area(6, 4)
    """
    return 0.5*side*height*5
if __name__ == "__main__":
    sampleside = 6
    samplegeight = 4
print("area:",
     pentagon_area(sampleside, sampleheight))


def pyramid_volume(length, weight, height):
    """
    calculate the volume phyramidg from length weight height.

    :param length: length of pyramid
    :param weight: weigth of pyramid
    :param height: height of pyramid

    :return: the volume (units^3)
    >>> pyramid_volume(8, 12, 6)
    """
    return length*weight*height/3
if __name__=="__main__":
    samplelength = 8
    sampleweight = 12
    sampleheight = 6
    print("volume",
          pyramid_volume(samplelength, sampleweight, sampleheight))



