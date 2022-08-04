from turtle import Turtle

MOVEMENT_INCREMENT = 20


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.speed("fastest")

    def up(self):
        self.sety(self.ycor() + MOVEMENT_INCREMENT)

    def down(self):
        self.sety(self.ycor() - MOVEMENT_INCREMENT)
