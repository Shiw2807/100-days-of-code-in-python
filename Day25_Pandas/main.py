import turtle
from wsgiref.util import guess_scheme 
import pandas as pd

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pd.read_csv("50states.csv")
all_states = data.state.to_list()
guessed_state=[]

while len(guessed_state) < 50:
    answer_state = screen.textinput(f"{len(guessed_state)} / 50 States Correct", "What's another state name?").title()

    if answer_state=="Exit":
        missing_states=[state for state in all_states if state not in guessed_state]
        new_data=pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")

    if answer_state in all_states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer_state)

screen.exitonclick()