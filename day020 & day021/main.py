import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scorekeeper = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True


def game_restart():
    snake.reset_snake()
    # food = Food()
    # snake = Snake()
    scorekeeper.reset_score()


while game_is_on:
    screen.update()
    time.sleep(0.1)
    # if not snake.move_snake():
    #    game_is_on = False
    snake.move_snake()

    if snake.snakes[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scorekeeper.update_score()

    if -280 > snake.snakes[0].xcor() or \
            snake.snakes[0].xcor() > 280 or \
            -280 > snake.snakes[0].ycor() or \
            snake.snakes[0].ycor() > 280:
        # game_is_on = False
        game_restart()
        # scorekeeper.game_over()

    # Detect collision with tail
    for segment in snake.snakes[1:]:
        if snake.snakes[0].distance(segment) < 5:
            # game_is_on = False
            # scorekeeper.game_over()
            game_restart()
