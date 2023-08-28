import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
scoreboard = Scoreboard()

screen.onkeypress(player.move, "Up")
cars = CarManager()

count = 0
game_is_on = True
while game_is_on:
    time.sleep(cars.move_speed)
    screen.update()

    if player.check_win():
        scoreboard.level_up()
        cars.add_speed()

    cars.move()

    if cars.check_distance(player):
        game_is_on = False
        scoreboard.game_over()

    if count % 6 == 0:
        cars.add_car()
    count += 1

screen.exitonclick()
