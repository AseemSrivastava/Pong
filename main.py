import turtle
from turtle import Screen
from turtle import Turtle

screen = Screen()
# Set Screen Color to black
screen.bgcolor("black")
# Set screen size to 800 x 600
screen.setup(800, 600)
# Set screen title to Pong
screen.title("Pong")
screen.tracer(0)

paddle = Turtle()
# Set Position of Paddle
paddle.setposition(350, 0)
# Set Paddle color
paddle.color("white")
# Set Paddle shape
paddle.shape("square")
# Set paddle size
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()


# Move paddle up
def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)


# Move paddle down
def go_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)


screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()
