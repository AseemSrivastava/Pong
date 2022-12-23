from turtle import Turtle


class Ball(Turtle):

    # Initialize ball
    def __init__(self):
        super().__init__()
        self.color("White")
        self.shape("circle")
        self.penup()

    # Set movement of ball
    def move(self):
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10
        self.goto(new_x, new_y)
