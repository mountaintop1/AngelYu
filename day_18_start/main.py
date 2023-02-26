"""Turn the turtle to the right by 90 degrees and draw a square. 
Repeat this 4 times to make a square,then turn the turtle 10 degrees
to the right and repeat the whole process 36 times to make a circle.
"""

import turtle as t
from turtle import Screen
import random


spiro = t.Turtle()
t.colormode(255)

def random_color():
    """Random color."""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

for _ in range(int(360 / 6)):
    spiro.speed("fastest")
    spiro.pensize(5)
    spiro.color(random_color())
    spiro.circle(200)
    # spiro.left(5)
    spiro.setheading(spiro.heading() + 6)

screen = Screen()
screen.exitonclick()



# walk = t.Turtle()
# t.colormode(255)

# def random_color():
#     """Random color."""
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return (r, g, b)

# # colours = [
# #     "CornflowerBlue", "DarkOrchid", "IndianRed",
# #     "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"
# #     ]

# direction = [0, 90, 180, 270]

# def randon_walk(colour, direction):
#     """Random walk."""
#     for _ in range(200):
#         walk.pensize(20)
#         walk.speed("fastest")
#         walk.color(colour())
#         walk.forward(30)
#         walk.setheading(random.choice(direction))
       
# randon_walk(random_color, direction)



# screen = Screen()
# screen.exitonclick()


# tim = t.Turtle()


# ########### Challenge 3 - Draw Shapes ########

# colours = [
#     "CornflowerBlue", "DarkOrchid", "IndianRed",
#     "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"
#     ]

# def draw_shape(num_sides):
#     """Draw a shape with the number of sides given."""
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)

# for shape_side_n in range(3, 10):
#     tim.pensize(10)
#     tim.color(random.choice(colours))
#     draw_shape(shape_side_n)

# screen = Screen()
# screen.exitonclick()
