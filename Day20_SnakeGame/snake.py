from turtle import Turtle, setheading
POSITIONS=[(0,0), (-20,0),(-40,0)]
MOVE_DISTANCE=20
UP=90
DOWN=270
LEFT=180 
RIGHT=360

class Snake:

    def __init__(self):
        self.new_segments=[]
        self.create_snake()
        self.head= self.new_segments[0]

    def create_snake(self):
        for pos in POSITIONS:
            segment=Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(pos)
            self.new_segments.append(segment)

    def move(self):
        for seg in range(len(self.new_segments)-1,0,-1):
            new_x= self.new_segments[seg-1].xcor()
            new_y=self.new_segments[seg-1].ycor()
            self.new_segments[seg].goto(new_x,new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading()!= DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading()!= UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading()!= RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading()!= LEFT:
            self.head.setheading(RIGHT)