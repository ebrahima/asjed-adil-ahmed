__author__ = 'asjed'

from nose.tools import *
from geometry_formulae import *


def test_circle_area_int():
    assert circle_area(1) == pi*(1**2)
    assert circle_area(2) == pi*(2**2)


eps = 1e-9


def test_circle_area_double():
    assert 19.634954085 - eps < circle_area(2.5) < 19.634954085 + eps


@raises(TypeError)
def test_square_area_other():
    circle_area("a string")

###############ssss##############


def test_rectangle_area_int():
    assert rectangle_area(2, 3) == 6
    assert rectangle_area(1, 2) == 2


eps = 1e-4


def test_rectangle_area_double():
    assert 1/6 - eps < rectangle_area(1/2, 1/3) < 1/6 + eps


@raises(TypeError)
def test_rectangle_area_other():
    rectangle_area('a string', 'a string')

################sss###############33


def test_sphere_volume_int():
    assert sphere_volume(4) == (4/3)*pi*(4**3)
    assert sphere_volume(1) == 4/3*pi


eps = 1e-6


def test_sphere_double():
    assert 14.137166941 - eps < sphere_volume(1.5) < 14.137166941 + eps
################sss##############


def test_cylinder_volume_int():
    assert cylinder_volume(2, 3) == pi*(2**2)*3
    assert cylinder_volume(1, 1) == pi*(1**2)*1


eps = 1e-9


def test_cylinder_double():
    assert 144.764589477 - eps < cylinder_volume(3.2, 4.5) < 144.764589477 + eps


##############sss################
def test_cone_volume_int():
    assert cone_volume(2, 5) == (pi*(2**2)*5)/3
    assert cone_volume(1, 1) == (pi*(1**1)*1)/3

eps = 1e-9

def test_cone_double():
    assert 27.143360527 - eps < cone_volume(2.4, 4.5) < 27.143360527 + eps

###############sss#############


def test_trapezium_area_int():
    assert trapezium_area(2, 3, 4) == 0.5*(2+3)*4
    assert trapezium_area(1, 3, 5) == 0.5*(1+3)*5

eps = 1e-2


def test_trapezium_double():
    assert 31.95 - eps < trapezium_area(3.4, 5.6, 7.1) < 31.95 + eps


#################sss###################


def test_pentagon_area_int():
    assert pentagon_area(6, 4) == 0.5*6*4*5
    assert pentagon_area(3, 5) == 0.5*3*5*5


def test_pentagon_double():
    assert 20 - eps < pentagon_area(2.5, 3.2) < 20 + eps


##################sss###########

def test_pyramid_volume_int():
    assert pyramid_volume(8, 12, 6) == (8*12*6)/3
    assert pyramid_volume(5, 3, 4) == (5*3*4)/3

esp = 1e-2


def test_pyramid_double():
    assert 56.76 - eps < pyramid_volume(4.3, 5.5, 7.2) < 56.76 + eps

##############sss###########


def test_triangle_area_int():
    assert triangle_area(2, 4) == 0.5*2*4
    assert triangle_area(1, 2) == 0.5*1*2


eps = 1e-2


def test_triangle_area_double():
    assert 5.25 - eps < triangle_area(2.5, 4.2) < 5.25 + eps

################sss##############













