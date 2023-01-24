
from turtle import *
import turtle
tur = turtle.Turtle()
ws =turtle.Screen()
ws.title("Pythontpoint")
turtle.screensize(800,400)
ws.bgcolor("white")
tur.pencolor("red")
tur.pensize(4)
Python=0
Cpp=0
tur.speed(0)
tur.penup()
tur.goto(0,260)
tur.pendown()
while True:
    tur.forward(Python)
    tur.right(Cpp)
    Python+=3
    Cpp+=1
    if Cpp==210:
        break
    tur.hideturtle()
turtle.done()
