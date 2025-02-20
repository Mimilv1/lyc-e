
from turtle import *
speed(0)
penup()
goto(0,0)
def star(x):
    color('black', 'blue')
    begin_fill()
    for i in range(18):
        forward(x)
        left(170)
    end_fill()
def cercle(x):
    color('grey', 'red')
    begin_fill()
    for i in range(360):
        forward(x)
        left(1)
    end_fill()
for i in range(10):
    goto(50*i,50*i)
    star(100)
    pendown()
    circle(70/1)
    penup()
goto(-100,-100)
for i in range(-10):
    goto(50*i,50*i)
    star(100)
    pendown()
    circle(70/1)
    penup()


done()
