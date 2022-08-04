from random import randint
import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


# create paddle instances
paddle_1 = Paddle()
paddle_2 = Paddle()

# create ball instance
ball = Ball()

# create score instances
score_1 = Score(xcor=-100, player=1)
score_2 = Score(xcor=100, player=2)

# move paddles into positon
paddle_1.goto(-350, 0)
paddle_2.goto(350, 0)


screen.listen()

# update screen so players dont see paddle turtles move
screen.update()
time.sleep(0.1)

# controller functions
screen.onkey(paddle_1.up, "w")
screen.onkey(paddle_1.down, "s")
screen.onkey(paddle_2.up, "Up")
screen.onkey(paddle_2.down, "Down")


game_is_on = True

INITIAL_DIRECTION = randint(0, 360)

direction = INITIAL_DIRECTION

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.setheading(direction)
    ball.move()

    # establish screen boundaries
    if paddle_1.ycor() >= 250:
        paddle_1.goto(paddle_1.xcor(), 250)
    if paddle_1.ycor() <= -250:
        paddle_1.goto(paddle_1.xcor(), -250)

    if paddle_2.ycor() >= 250:
        paddle_2.goto(paddle_2.xcor(), 250)
    if paddle_2.ycor() <= -250:
        paddle_2.goto(paddle_2.xcor(), -250)

    # establish wall bounce conditions
    # bounce toward player 1 from top
    if ball.ycor() >= 250 and ball.xcor() < 0:
        direction = randint(200, 250)  # west to south

    # bounce toward player 1 from bottom
    if ball.ycor() <= -250 and ball.xcor() < 0:
        direction = randint(110, 160)  # north to west

    # bounce toward player 2 from top
    if ball.ycor() >= 250 and ball.xcor() > 0:
        direction = randint(290, 340)  # south to east

    # bounce toward player 2 from bottom
    if ball.ycor() <= -250 and ball.xcor() > 0:
        direction = randint(20, 70)  # east to north

    # establish paddle bounce conditions
    # bounce off player 1
    if ball.distance(paddle_1) < 40:
        direction = randint(290, 430)  # north east south
    # bounce off player 2
    if ball.distance(paddle_2) < 40:
        direction = randint(110, 250)  # north west south

    # establish point conditions
    if ball.xcor() > 410:
        ball.next_round()
        score_1.add()
        # player 1 point
    if ball.xcor() < -410:
        ball.next_round()
        score_2.add()
        # player 2 point

    # win/lose conditions
    if score_1.score == 11:
        score_1.win()
        game_is_on = False
    if score_2.score == 11:
        score_2.win()
        game_is_on = False


screen.exitonclick()
