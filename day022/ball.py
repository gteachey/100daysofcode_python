from turtle import Turtle

MOVE_SPEED = 40


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.setheading(45)
        self.fillcolor("white")
        self.penup()

    def move_ball(self, left_paddle, right_paddle):
        self.speed(MOVE_SPEED)
        self.forward(5)
        self.wall_bounce()
        self.bounce_ball(left_paddle, right_paddle)

    def wall_bounce(self):
        if self.ycor() >= 280 and self.heading() == 45:
            self.setheading(315)
        elif self.ycor() >= 280 and self.heading() == 135:
            self.setheading(225)
        elif self.ycor() <= -280 and self.heading() == 225:
            self.setheading(135)
        elif self.ycor() <= -280 and self.heading() == 315:
            self.setheading(45)

    def bounce_ball(self, left_paddle, right_paddle):
        if (-324 > self.xcor() or self.xcor() > 324) and \
                (self.distance(left_paddle) < 50 or self.distance(right_paddle) < 50):
            self.change_direction()

    def ball_missed(self):
        if self.xcor() > 380:
            self.speed(MOVE_SPEED + 15)
            self.goto(0, 0)
            self.change_direction()
            return "left"
        elif self.xcor() < -380:
            self.speed(MOVE_SPEED + 15)
            self.goto(0, 0)
            self.change_direction()
            return "right"

    def change_direction(self):
        if self.heading() == 315:
            self.setheading(225)
        elif self.heading() == 135:
            self.setheading(45)
        elif self.heading() == 45:
            self.setheading(135)
        else:
            self.setheading(315)
