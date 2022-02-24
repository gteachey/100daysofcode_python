from turtle import Turtle, Screen
import random
import time

screen = Screen()
screen.register_shape("tmbkr.bmp")
SHAPES = ["arrow", "turtle", "circle", "square", "triangle", "classic", "tmbkr.gif"]
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2


class CarManager(Turtle):
    def __init__(self):
        self.all_cars = []
        self.new_distance = STARTING_MOVE_DISTANCE

    def create_car(self):
        if random.randint(1, 6) == 1:
            car = Turtle()
            # car.hideturtle()
            # car.shape("square")
            car.shape(random.choice(SHAPES))
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.fillcolor(random.choice(COLORS))
            car.penup()
            car_y_cor = random.randint(-240, 240)
            car.goto(330, car_y_cor)
            self.all_cars.append(car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.new_distance)

    def new_level(self):
        self.new_distance += MOVE_INCREMENT
