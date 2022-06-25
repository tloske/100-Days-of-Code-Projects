from car import Car
from random import choice


class CarManager:

    def __init__(self, num_cars):
        self.spawn_points = [(400 + j * 40, i)
                             for i in range(-250, 250, 20) for j in range(0, 10)]
        self.num_cars = num_cars
        self.spawn_cars()

    def spawn_cars(self):
        self.car_list = []
        for _ in range(self.num_cars):
            self.add_car()

    def move_cars(self):
        for car in self.car_list:
            car.move()
            if car.xcor() <= -420:
                car.reset(choice(self.spawn_points))

    def check_collision(self, player):
        for car in self.car_list:
            if car.distance(player) < 20:
                return True

    def add_car(self):
        car = Car()
        car.reset(choice(self.spawn_points))
        self.car_list.append(car)
