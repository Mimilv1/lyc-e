# Créé par emili, le 08/06/2021 en Python 3.7
from turtle import *
speed(0)
color('chartreuse')
tracer(50)
bgcolor('black')
for i in range(180):
    circle(i-185)
    right(91)
for i in range(140):
    tracer(70)
    circle(i-185)
    right(91)
color('red')
for r in range(360):
    penup()
    goto(0,0)
    pendown()
    tracer(70)
    forward(200)
    right(91)
color("#FD3F92")
penup()
goto(0,0)
pendown()
for i in range(90):
    forward(300)
    right(30)
    forward(70)
    left(60)
    forward(150)
    right(30)
    color('chartreuse')
    pensize(2)
    circle(16)

    penup()
    setposition(0, 0)
    pendown()
    pensize(0)
    color("#FD3F92")

    right(4)
penup()
goto(0,0)

done()
