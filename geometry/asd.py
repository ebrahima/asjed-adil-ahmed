__author__ = 'asjed'
import turtle

side = 50

i = 0;
while (i < 4):
    turtle.forward(side)
    turtle.left(90)
    i = i+1

turtle.done()

side = 150

i = 0;
while (i < 3):
    turtle.forward(side)
    turtle.left(120)
    i = i+1

turtle.done()

side = 180

i = 0;
while (i < 5):
    turtle.forward(side)
    turtle.left(72)
    i = i+1
turtle.done()

def draw_circle(radius):
    i = 0;
    while (i < 100):
        turtle.forward(radius)
        turtle.left(4)
        i = i+1
turtle.done()
if __name__ == "__main__":
    draw_circle(10)
turtle.done()

i = 0;
while (i < 1):
    turtle.forward(140)
    turtle.left(120)
    turtle.forward(60)
    turtle.left(60)
    turtle.forward(80)
    turtle.left(60)
    turtle.forward(60)
    i = i+1
turtle.done()







