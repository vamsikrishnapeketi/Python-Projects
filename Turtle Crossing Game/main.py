import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


player = Player()
carmanager = CarManager()
scoreboard = Scoreboard()
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)

screen.listen()
screen.onkey(fun=player.up,key="Up")

game_is_on = True
while game_is_on:
    time.sleep(carmanager.car_speed)
    screen.update()
    carmanager.generate_cars()
    carmanager.moving_left()
    scoreboard.display()

    #condition for the turtle reaching the top edge
    if player.is_finish():
        player.finished()
        carmanager.inc_car_speed()
        scoreboard.lev_inc()


    #condition for turtle to hit one of the cars
    for car in carmanager.cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()




screen.exitonclick()
