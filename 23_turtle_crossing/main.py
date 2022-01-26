import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=player.go_up, key="Up")
screen.onkey(fun=player.go_down, key="Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.move()
    cars.create_car()

    # Столкновение с машиной
    for car in cars.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    # Черепашка дошла до финиша
    if player.finish_line():
        player.go_to_start()
        cars.increase_speed()
        scoreboard.increase_lvl()

screen.exitonclick()
