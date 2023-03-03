"""Paddle class for Pong game."""
from turtle import Turtle

class Paddle(Turtle):
    """This class represents the paddle."""
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        """Move the Paddle up."""
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
         
    def go_down(self):
        """Move the Paddle down."""
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)