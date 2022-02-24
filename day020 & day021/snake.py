from turtle import Turtle
import random

COLORS = ['red', 'blue', 'green']
MOVE_DISTANCE = 10
STARTING_POSITIONS = [(-20, -280), (0, -280), (20, -280)]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.snakes = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        snake = Turtle("square")
        snake.shapesize(stretch_len=0.5, stretch_wid=0.5)
        snake.setpos(position)
        snake.fillcolor(random.choice(COLORS))
        self.snakes.append(snake)

    def extend(self):
        self.add_segment(self.snakes[-1].position())

    def move_snake(self):
        for seq_num in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[seq_num - 1].xcor()
            new_y = self.snakes[seq_num - 1].ycor()
            self.snakes[seq_num].goto(new_x, new_y)
        self.snakes[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.snakes[0].heading() != DOWN:
            self.snakes[0].setheading(UP)

    def down(self):
        if self.snakes[0].heading() != UP:
            self.snakes[0].setheading(DOWN)

    def left(self):
        if self.snakes[0].heading() != RIGHT:
            self.snakes[0].setheading(LEFT)

    def right(self):
        if self.snakes[0].heading() != LEFT:
            self.snakes[0].setheading(RIGHT)

    def reset_snake(self):
        for snake in self.snakes:
            snake.goto(1000, 1000)
        self.snakes.clear()
        self.create_snake()
