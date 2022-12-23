import time
from turtle import Screen

from ball import Ball
from paddle import Paddle

screen = Screen()
# Set Screen Color to black
screen.bgcolor("black")
# Set screen size to 800 x 600
screen.setup(800, 600)
# Set screen title to Pong
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
# Controls for right paddle
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
# Controls for left paddle
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

screen.exitonclick()
