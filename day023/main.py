import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()

carmgr = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkeypress(fun=player.move_player_up, key="Up")
screen.onkeypress(fun=player.move_player_down, key="Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    carmgr.create_car()
    carmgr.move_cars()
    if player.level_up():
        scoreboard.update_score()
        carmgr.new_level()
    for car in carmgr.all_cars:
        if car.distance(player) < 25:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
