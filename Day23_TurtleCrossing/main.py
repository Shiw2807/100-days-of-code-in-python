import turtle
import time
from scoreboard import Scoreboard
from carmanager import Carmanager
from player import Player


screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.tracer(0)

player= Player()
cars= Carmanager()
score= Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")



game_is_over = False
while not game_is_over:
    time.sleep(0.1)
    screen.update()

    cars.create()
    cars.move_forward()

    for car in cars.all_cars:
        if car.distance(player) < 20:
            score.game_over()
            game_is_over= True
    
    if player.is_at_finish_line():
        player.got_to_start()
        cars.level_up()
        

screen.exitonclick()