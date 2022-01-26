from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 1


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.cars_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            self.new_car = Turtle("square")
            self.new_car.penup()
            self.new_car.shapesize(stretch_wid=1, stretch_len=2)
            self.new_car.setx(300)
            self.new_car.sety(random.randint(-250, 250))
            self.new_car.color(random.choice(COLORS))
            self.all_cars.append(self.new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(self.cars_speed)

    def increase_speed(self):
        self.cars_speed += MOVE_INCREMENT
