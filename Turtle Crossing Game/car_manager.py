import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.cars = []
        self.car_speed = 0.1

    def generate_cars(self):
        random_chance = random.randint(1,5) #the frequency of the cars are more hence this is done to reduce the number of cars generated
        if random_chance == 1:
            car = Turtle()
            car.shape("square")
            car.penup()
            car.shapesize(stretch_wid=1,stretch_len=2)
            car.color(random.choice(COLORS))
            new_y = random.randint(-250,250)
            car.goto(300,new_y)
            self.cars.append(car)

    def moving_left(self):
        for car in self.cars:
            car.backward(MOVE_INCREMENT)

    def inc_car_speed(self):
        self.car_speed *= 0.95        

