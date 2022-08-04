from turtle import Turtle, Screen, penup


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed(6)

    def direction(self, direction):
        self.setheading(direction)

    def move(self):
        self.forward(20)

    def next_round(self):
        self.goto(0, 0)
