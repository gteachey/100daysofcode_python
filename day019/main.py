import random
import turtle
from turtle import Turtle, Screen

t = Turtle()
screen = Screen()


def move_forward():
    t.forward(10)


def move_backward():
    t.back(10)


def move_left():
    t.left(10)


def move_right():
    t.right(10)


def clear():
    t.clear()
    t.penup()
    t.setposition(0, 0)
    t.pendown()


screen.listen()

turtle.onkey(key="w", fun=move_forward)
turtle.onkey(key="s", fun=move_backward)
turtle.onkey(key="a", fun=move_left)
turtle.onkey(key="d", fun=move_right)
turtle.onkey(key="c", fun=clear)

screen.exitonclick()
