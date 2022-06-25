from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__('turtle')
        self.pu()
        self.goto(0, -280)
        self.setheading(90)

    def move(self):
        self.forward(20)

    def reset(self):
        self.goto(0, -280)
