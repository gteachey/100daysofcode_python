import colorgram
from turtle import Turtle, Screen
import random

# Extract 6 colors from an image.
colors = colorgram.extract('image.jpeg', 10)

# print(colors)


#
# print(color_list)
screen = Screen()
screen.colormode(255)
t = Turtle()


def make_some_dots():
    color_list = []
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        color_tuple = (r, g, b)
        color_list.append(color_tuple)

    xpos = -300
    ypos = -300
    t.speed(0)
    t.hideturtle()
    for _ in range(10):
        t.penup()
        t.setposition(xpos, ypos)

        for _ in range(10):
            t.dot(20, random.choice(color_list))
            # t.penup()
            t.forward(50)
            # t.pendown()
        ypos += 50


make_some_dots()
screen.exitonclick()
