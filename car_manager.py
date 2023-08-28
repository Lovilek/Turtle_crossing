from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 0.1


class CarManager:
    def __init__(self):
        self.cars = []
        self.move_speed = MOVE_INCREMENT
        self.add_car()

    def add_car(self):
        new_car = Turtle()
        new_car.shape("square")
        new_car.color(random.choice(COLORS))
        new_car.penup()
        new_car.speed(50)
        new_car.setheading(180)
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.goto(250, random.randint(-240, 240))
        self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE)

    def add_speed(self):
        self.move_speed *= 0.8

    def check_distance(self, player):
        for car in self.cars:
            if player.distance(car) < 25:
                return True
