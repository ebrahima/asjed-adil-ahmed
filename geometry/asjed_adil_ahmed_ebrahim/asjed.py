__author__ = 'asjed'
from dimension_validate import *


def square_perimeter(side):
    """
    Calculate perimeter of a square from side length.

    @param side: the side length
    @return: the perimeter (same units as side length)

    >>> square_perimeter(4)
    16
    """
    if (dim_validate(side)):
        return 4*side
    else:
        raise ValueError("side is less than 0: "+str(side))


def circle_area(radius):
    """
    calculate area of a circle given the radius.

    :param radius: radius of a circle
    :return: the area (unit^2 given radius)

    >>> circle_area(2)
    12.566370614359172
    """
    return pi*(radius**2)
 if (dim_validate(radius)):
        return pi*(radius**2)
    else:
        raise ValueError("radius is less than 0: "+str(radius))