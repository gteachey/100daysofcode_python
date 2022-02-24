from turtle import Turtle

WIDTH = 20
HEIGHT = 100
MOVE = 20


class Paddle(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.setheading(90)
        self.shape("square")
        self.color("white")
        self.width = WIDTH
        self.height = HEIGHT
        self.shapesize(stretch_wid=int(WIDTH / 20), stretch_len=int(HEIGHT / 20))
        self.penup()
        x_pos = x_pos
        y_pos = y_pos
        self.setposition(x=x_pos, y=y_pos)
        self.showturtle()

    def move_paddle_up(self):
        self.forward(20)

    def move_paddle_down(self):
        self.backward(20)
