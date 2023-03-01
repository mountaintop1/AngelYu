"""Higher Order Functions and Decorators with Etch A Sketch project."""
from turtle import Turtle, Screen
import random


is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-160, -100, -40, 20, 80, 140]

# def create_turtle(x, y, color):
#     """Create a turtle."""
#     tim = Turtle(shape="turtle")
#     tim.color(color)
#     tim.penup()
#     tim.goto(x=x, y=y)
#     return tim

# turtle1 = create_turtle(x=-230, y=-160, color=colors[0])
# turtle2 = create_turtle(x=-230, y=-100, color=colors[1])
# turtle3 = create_turtle(x=-230, y=-40, color=colors[2])
# turtle4 = create_turtle(x=-230, y=20, color=colors[3])
# turtle5 = create_turtle(x=-230, y=80, color=colors[4])
# turtle6 = create_turtle(x=-230, y=140, color=colors[5])

all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0, 5)
        turtle.forward(rand_distance)

screen.exitonclick()





# tim = Turtle()
# screen = Screen()

# def move_forwards():
#     """Move the turtle forward."""
#     tim.forward(10)

# def move_backwards():
#     """Move the turtle backwards."""
#     tim.backward(10)
   
# def move_counter_clockwise():
#     """Move the turtle counter clockwise."""
#     tim.left(10)
#     # new_heading = tim.heading() + 10
#     # tim.setheading(new_heading)
    
# def move_clockwise():
#     """Move the turtle clockwise."""
#     tim.right(10)

# def clearscreen():
#     """Move the turtle clear the screen."""
#     tim.reset()
#     # tim.clear()
#     # tim.penup()
#     # tim.home()
#     # tim.pendown()

# screen.listen()
# screen.onkey(key="w", fun=move_forwards)
# screen.onkey(key="s", fun=move_backwards)
# screen.onkey(key="a", fun=move_counter_clockwise)
# screen.onkey(key="d", fun=move_clockwise)
# screen.onkey(key="c", fun=clearscreen)
# screen.exitonclick()







# class example
# tim = Turtle()
# screen = Screen()

# def move_forwards():
#     """Move the turtle forward."""
#     tim.forward(10)

# screen.listen()
# screen.onkey(key="space", fun=move_forwards)
# screen.exitonclick()
