from turtle import Turtle


class Snake:
    segments = []

    def __init__(self):
        self.head = Turtle('square')
        self.head.color('white')
        self.head.pu()

    def grow(self):
        new_segment = Turtle('square')
        new_segment.color('white')
        new_segment.pu()
        new_segment.goto(400,0)
        self.segments.append(new_segment)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def move(self):
        new_pos = (self.head.pos())
        self.head.forward(20)
        for segment in self.segments:
            temp = segment.pos()
            segment.setpos(new_pos)
            new_pos = temp
        if abs(self.head.xcor()) > 300:
            self.head.goto(-self.head.xcor(), self.head.ycor())
        elif abs(self.head.ycor()) > 300:
            self.head.goto(self.head.xcor(), -self.head.ycor())
