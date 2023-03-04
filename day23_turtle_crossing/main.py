import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.bgcolor("black")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(player.move, "Up")

GAME_IS_ON = True
while GAME_IS_ON:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move()

    # detect collision with car
    for car in car_manager.car_list:
        if car.distance(player) < 20:
            GAME_IS_ON = False
            scoreboard.game_over()
    # detect successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_score()

screen.exitonclick()