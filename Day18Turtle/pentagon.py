from turtle import *

t=Turtle()

def move():
    t.forward(100)
    t.left(72)
    
 
for i in range(6):
    move()

screen=Screen()
screen.exitonclick()