# Créé par emili, le 08/06/2021 en Python 3.7
from turtle import *
penup()
goto(0,0)
speed(0)
def serpent(x,y):
    if x==0:
        fd(10)
        return
    pendown()
    lt(y)
    fd(5)
    rt(y)
    fd(5)
    rt(8)
    serpent(x-1,-y*2)
serpent(965,16)
serpent(965,-16)
done()