from turtle import Turtle


FONT = ("Courier", 22, "normal")
POSITION = (-380, 250)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.speed(0)
        self.penup()
        self.goto(POSITION)
        self.update()

    
    def update(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update()
    
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)