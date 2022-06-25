from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self, x):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.pu()
        self.goto(x, 250)
        self.pd()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"{self.score}",
                   align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
