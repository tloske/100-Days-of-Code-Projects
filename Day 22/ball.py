from turtle import Turtle
from random import randint


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.pu()
        self.set_params()

    def set_params(self):
        self.speed = 0.125
        self.x_move = randint(0, 10)
        self.y_move = randint(0, 10)

    def reset(self):
        self.goto(0, 0)
        self.set_params()

    def move(self):
        new_x = self.xcor() + self.x_move * self.speed
        new_y = self.ycor() + self.y_move * self.speed
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move += randint(0, 2)
        self.y_move *= -1

    def bounce_x(self):
        self.x_move += randint(0, 2)
        self.x_move *= -1
        self.speed *= 1.1
