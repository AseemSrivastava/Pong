from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        # Set Position of Paddle
        self.setposition(position)
        # Set Paddle color
        self.color("white")
        # Set Paddle shape
        self.shape("square")
        # Set paddle size
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()

    # Move paddle up
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    # Move paddle down
    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

