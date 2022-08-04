from turtle import Turtle

ALIGNMENT = "center"
FONT = "courier"


class Score(Turtle):
    def __init__(self, xcor, player):
        super().__init__()
        self.player = player
        self.xcor = xcor
        self.score = 0
        self.hideturtle()
        self.penup()
        self.pencolor("white")
        self.write_score()

    # increases score when opposing player misses. called in main
    def add(self):
        self.clear()
        self.score += 1
        self.write_score()

    # called by add to write score
    def write_score(self):
        self.goto(self.xcor, 250)
        self.write(f"{self.score}", False, ALIGNMENT, (FONT, 24, "normal"))

    # called by main if score == 11
    def win(self):
        self.goto(0, 50)
        self.write(
            f"Player {self.player} wins!", False, ALIGNMENT, (FONT, 30, "normal")
        )

    # called by main if other player score == 11
    # def win(self):
    #     self.goto(0, -50)
    #     self.write(f"Player {self.player} loses", False, ALIGNMENT, (FONT, 30, "normal"))
