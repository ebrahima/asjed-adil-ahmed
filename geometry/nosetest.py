__author__ = 'asjed'


from geometry_formulae import *
from nose.tools import *


def test_circle_area_int():
    assert circle_area(1) == pi
    assert circle_area(2) == 4*pi
    s = 5
    assert circle_area(s*2) == 4*circle_area(s)


eps = 1e-6
def test_circle_area_double():
    assert 1/2 - eps < circle_area(2.5) < 1/2 + eps

def test_fail_circle_area():
    assert circle_area(2) == 4*pi

def test_rectangle_area_int():
    assert rectangle_area(2, 3) == 6
    assert rectangle_area(1, 2) == 2
    s = 4
    assert rectangle_area(s*2) == 4*rectangle_area(s)


eps = 1e-6
def test_rectangle_area_double():
    assert 1/2 - eps < rectangle_area(4) < 1/2 + eps

def test_fail_rectangle_area():
    assert rectangle_area(4) == 20

def test_sphere_volume_int():
    assert sphere_volume(4) == 268.08
    assert sphere_volume(1) == 4/3*pi
    s = 4
    assert sphere_volume(s*2) == 4*triangle_area(s)


eps = 1e-6
def test_sphere_double():
    assert 1/2 - eps < sphere_volume(4) < 1/2 + eps

def test_fail_sphere_volume():
    assert sphere_volume(4) == 268.08

def test_cylinder_volume_int():
    assert cylinder_volume(2, 3) == 37.7
    assert cylinder_volume(1, 1) == pi
    s = 4
    assert cylinder_volume(s*2) == 4*cylinder_volume(s)


eps = 1e-6
def test_cylinder_double():
    assert 1/2 - eps < cylinder_volume(4) < 1/2 + eps


def test_fail_cylinder_volume():
    assert cylinder_volume(4) == 268.08

def test_cone_volume_int():
    assert cone_volume(2, 5) == 20.94
    assert cone_volume(1, 1) == pi/3
    s = 4
    assert cone_volume(s*2) == 4*cone_volume(s)


eps = 1e-6
def test_cone_double():
    assert 1/2 - eps < cone_volume(4) < 1/2 + eps


def test_fail_cone_volume():
    assert cone_volume(2, 5) == 20.94

def test_trapezium_area_int():
    assert trapezium_area(2, 3, 4) == 10
    assert trapezium_area(1, 1, 1) == 1
    s = 4
    assert trapezium_area(s*2) == 4*trapezium_area(s)


eps = 1e-6
def test_trapezium_double():
    assert 1/2 - eps < trapezium_area(4) < 1/2 + eps


def test_fail_trapezium_area():
    assert trapezium_area(2, 3, 4) == 10
def test_fail_cone_volume():
    assert cone_volume(2, 5) == 20.94

def test_pentagon_area_int():
    assert pentagon_area(6, 4) == 60.0
    assert pentagon_area(1, 1) == 0.5
    s = 4
    assert pentagon_area(s*2) == 4*trapezium_area(s)


eps = 1e-6
def test_pentagon_double():
    assert 1/2 - eps < pentagon_area(6, 4) < 1/2 + eps


def test_fail_pentagon_area():
    assert pentagon_area(6, 4) == 60.0


def test_pyramid_volume_int():
    assert pyramid_volume(8, 12, 6) == 192.0
    assert pyramid_volume(1, 1, 1) == 1/3
    s = 4
    assert pyramid_volume(s*2) == 4*trapezium_area(s)


eps = 1e-6
def test_pyramid_double():
    assert 1/2 - eps < pyramid_volume(8, 12, 6) < 1/2 + eps


def test_fail_pyramid_volume():
    assert pyramid_volume(8, 12, 6) == 192.0















