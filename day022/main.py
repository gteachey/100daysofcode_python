from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

game_screen = Screen()
game_screen.setup(width=800, height=600)
game_screen.bgcolor("black")
game_screen.title("Pong Game")
game_screen.tracer(0)
right_paddle = Paddle(x_pos=350, y_pos=0)
left_paddle = Paddle(x_pos=-350, y_pos=0)
ball = Ball()
score_keeper = ScoreBoard()
game_screen.tracer(1)

game_screen.listen()
game_screen.onkeypress(left_paddle.move_paddle_up, "w")
game_screen.onkeypress(left_paddle.move_paddle_down, "s")

game_screen.onkeypress(right_paddle.move_paddle_up, "Up")
game_screen.onkeypress(right_paddle.move_paddle_down, "Down")

game_is_on = True
while game_is_on:
    ball.move_ball(left_paddle, right_paddle)
    score_keeper.point_scored(ball.ball_missed())

game_screen.exitonclick()
