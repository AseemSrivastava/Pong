import turtle
from turtle import Screen
from turtle import Turtle
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

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()
