"""Extract colors from an image."""
# import colorgram
# comment out the code below after running it once
# rgb_color = []
# colors = colorgram.extract(r'C:\Users\Olalekan\Desktop\Python\Angela_Yu\painting\my_image.jpg', 60)
# for colo in colors:
#     r = colo.rgb.r
#     g = colo.rgb.g
#     b = colo.rgb.b
#     new_color = (r, g, b)
#     rgb_color.append(new_color)
# print(rgb_color)
import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

color_list = [
    (124, 180, 210), (234, 243, 238), (198, 174, 16), (29, 119, 167),
    (176, 14, 45), (235, 150, 76), (236, 204, 90), (217, 124, 163),
    (26, 144, 74), (215, 80, 123), (9, 171, 210), (212, 61, 27),
    (237, 77, 45), (245, 157, 187), (64, 21, 53), (12, 183, 150),
    (13, 31, 75), (161, 57, 106), (76, 27, 22), (129, 209, 233),
    (161, 192, 164), (15, 48, 132), (102, 116, 181), (250, 159, 152),
    (168, 24, 19), (121, 216, 209), (3, 88, 57), (179, 184, 212),
    (6, 70, 47), (239, 203, 11), (13, 83, 107), (67, 77, 50)
]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(30, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)









screen = turtle_module.Screen()
screen.exitonclick()
