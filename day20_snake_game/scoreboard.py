"""scoreboard"""
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

# FILE_PATH = r'C:\Users\Olalekan\Desktop\Python\Angela_Yu\day20_snake_game\data.txt'
# with open(FILE_PATH) as file:
#     content = file.read()
class Scoreboard(Turtle):
    """This class represents the scoreboard."""
    def __init__(self):
        super().__init__()
        self.score = 0
        with open(r'C:\Users\Olalekan\Desktop\Python\Angela_Yu\day20_snake_game\data.txt') as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """Update the scoreboard."""
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        """Reset the scoreboard."""
        if self.score > self.high_score:
            self.high_score = self.score
            with open(r'C:\Users\Olalekan\Desktop\Python\Angela_Yu\day20_snake_game\data.txt', mode='w') as data:
                data.write(f'{self.high_score}')
        self.score = 0
        self.clear()
        self.update_scoreboard()

    # def game_over(self):
    #     """Display game over message."""
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """Increase the score."""
        self.score += 1
        self.update_scoreboard()
