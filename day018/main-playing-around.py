from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()
screen = Screen()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("green")

# for _ in range(4):
#    for _ in range(5):
#        timmy_the_turtle.forward(10)
#        timmy_the_turtle.penup()
#        timmy_the_turtle.forward(10)
#        timmy_the_turtle.pendown()
#    timmy_the_turtle.left(90)


colors = ["red", "green", "blue", "purple", "black", 'gainsboro', 'dark magenta', 'orange red', 'cyan', 'spring green']
heading = [0, 90, 180, 270]


# directions = [timmy_the_turtle.right(90), timmy_the_turtle.left(90), timmy_the_turtle.right(270), timmy_the_turtle.left(270) ]

def draw_figures():
    sides = 3

    while sides < 11:
        angle = 360 / sides
        timmy_the_turtle.pencolor(random.choice(colors))
        for _ in range(sides):
            timmy_the_turtle.forward(10)
        #            random.choice(directions)
        sides += 1


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def rand_walk(num_moves):
    timmy_the_turtle.speed(10)
    timmy_the_turtle.pensize(10)
    for i in range(num_moves):
        timmy_the_turtle.color(random_color())
        timmy_the_turtle.forward(30)
        timmy_the_turtle.setheading(random.choice(heading))


def draw_circle():
    heading = 0
    timmy_the_turtle.speed(0)
    for _ in range(72):
        timmy_the_turtle.color(random_color())
        timmy_the_turtle.setheading(heading)
        timmy_the_turtle.circle(100, extent=None, steps=None)
        heading += 5


screen.colormode(255)
draw_circle()
# rand_walk(200)

screen.screensize()
screen.exitonclick()
