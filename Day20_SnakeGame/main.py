from turtle import Screen
import time
from scoreboard import Scoreboard
from food import Food
from snake import Snake
from scoreboard import Scoreboard


screen = Screen()
screen.tracer(0)
screen.setup(width=600, height= 500)
screen.bgcolor("black")
screen.title("Shiwanshi and Waqar")


snake= Snake()
food=Food()
scorebaord=Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

is_game_on= True
while is_game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.distance(food)<15:
        food.refresh()
        scorebaord.increase_score()


screen.exitonclick()