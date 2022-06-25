from random import randint
from turtle import Turtle


class Car(Turtle):
    def __init__(self):
        super().__init__('square')
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(self.get_color())
        self.pu()
        self.setheading(180)

    def reset(self, position):
        self.goto(position)

    def get_color(self):
        return (randint(0, 255), randint(0, 255), randint(0, 255))

    def move(self):
        self.forward(20)
