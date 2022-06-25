from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x):
        super().__init__('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color('white')
        self.pu()
        self.goto(x, 0)
        self.speed = 10

    def move_up(self):
        self.goto(self.xcor(), self.ycor()+self.speed)

    def move_down(self):
        self.goto(self.xcor(), self.ycor()-self.speed)

    def set_pos(self, x, y):
        self.goto(x, y)

    def decide_move_dir(self, ball):
        if self.ycor() < ball.ycor():
            return self.move_up
        elif self.ycor() > ball.ycor():
            return self.move_down
        else:
            return
