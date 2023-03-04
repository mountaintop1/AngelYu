"""Scoreboard class to keep track of the score and high score."""
from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    """A class to represent the scoreboard."""
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-280, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        """Update the scoreboard."""
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="left", font=FONT)
        
    def increase_score(self):
        """Increase the score."""
        self.score += 1
        self.update_scoreboard()
    def game_over(self):
        """Display game over message."""
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
        
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()