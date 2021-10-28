from turtle import *

bgcolor('black')
speed(11)
hideturtle()
for i in range (120):
    color('blue')

    circle(i)
    color('magenta')
    circle(i*0.8)
    right(3)
    forward(3)
done()