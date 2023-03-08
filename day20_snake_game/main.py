"""snake game"""
from turtle import Screen # Turtle
import time
from snake import Snake
from scoreboard import Scoreboard
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

GAME_IS_ON = True
while GAME_IS_ON:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # if head collides with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # if head collides with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # if head collides with tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()


# x_position = 0
# for turtle_index in range(0, 3):
#     new_turtle = Turtle(shape="square")
#     new_turtle.color('white')
#     new_turtle.penup()
#     new_turtle.goto(x=x_position, y=0)
#     x_position -= 20