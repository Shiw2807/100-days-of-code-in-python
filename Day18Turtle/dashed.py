from turtle import *

t=Turtle()
for i in range(10):
    t.forward(15)
    t.penup()
    t.forward(5)
    t.pendown()
    

screen=Screen()
screen.exitonclick()