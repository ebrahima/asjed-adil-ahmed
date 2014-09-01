__author__ = 'asjed'

from pylab import *

from geometry_formulae import *

def boring_triangle(length):
    return triangle_area(1, length)


v_circle_area = np.vectorize(circle_area)
v_circle_perimeter = np.vectorize(boring_triangle)

S = np.linspace(0,10) # our side lengths

A = v_circle_area(S)  # the areas
P = v_circle_perimeter(S)  # the perimeters

plot(S, A, '-r', label="Area")
plot(S, P, ':b', label="Perimeter")


xlabel('radius')
ylabel('geo values')
title('c Geo Properties')
legend(loc='upper right')

show()
v_rectangle_area = np.vectorize(rectangle_area)
v_rectangle_perimeter = np.vectorize(rectangle_perimeter)

S = np.linspace(0,10) # our side lengths

A = v_rectangle_area(S)  # the areas
P = v_rectangle_perimeter(S)  # the perimeters

plot(S, A, '-r', label="Area")
plot(S, P, ':b', label="Perimeter")


xlabel('base')
ylabel('geo values')
title('c Geo Properties')
legend(loc='upper right')
show()length
