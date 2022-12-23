from turtle import Turtle


class Ball(Turtle):

    # Initialize ball
    def __init__(self):
        super().__init__()
        self.color("White")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    # Set movement of ball
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    # Bounce the ball from top and bottom of screen ( wall)
    def bounce_y(self):
        self.y_move *= -1

    # Bounce the ball from left and right paddle
    def bounce_x(self):
        self.x_move *= -1
