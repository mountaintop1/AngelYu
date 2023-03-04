from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    """A class to represent the player in the game."""
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("white")
        self.go_to_start()
        self.setheading(90)

    def move(self):
        """Move the player forward."""
        self.forward(MOVE_DISTANCE)
        
    def go_to_start(self):
        """Move the player back to the start line."""
        self.goto(STARTING_POSITION)
        
    def is_at_finish_line(self):
        """Return True if the player has reached the finish line."""
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False