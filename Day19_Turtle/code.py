from turtle import Turtle, Screen
import random


screen = Screen()

is_game_on=False
screen.setup(width=600, height= 400)
user_bet=screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour: ")
colors=["red", 'orange', 'yellow', 'green', 'blue', 'purple']
y_positions=[-70,-40,-10,20,50,80]
all_turtles=[]

for turtle_index in range(0,6):
    new_turtles = Turtle(shape='turtle')
    new_turtles.color(colors[turtle_index])
    new_turtles.penup()
    new_turtles.goto(x=-280,y=y_positions[turtle_index])
    all_turtles.append(new_turtles)

if user_bet:
    is_game_on= True

while is_game_on:

    for turtle in all_turtles:
        if turtle.xcor()>270:
            is_game_on= False
            winning_turtle=turtle.pencolor()
            if winning_turtle==user_bet:
                print(f"You won the bet! The {winning_turtle} turtle is the winner! ")
            else:
                 print(f"You lost the bet! The {winning_turtle} turtle is the winner! ")
        random_dist=random.randint(0,10)
        turtle.forward(random_dist)


screen.exitonclick()
