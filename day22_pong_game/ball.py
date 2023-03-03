from time import sleep
from turtle import Turtle

class Ball(Turtle):
    """This class represents the ball."""
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        """Move the ball."""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """Bounce the ball off the wall."""
        self.y_move *= -1
        
    def bounce_x(self):
        """Bounce the ball off the paddle."""
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        """Reset the ball position."""
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()