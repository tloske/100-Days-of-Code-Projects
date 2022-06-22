from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.pu()
        self.goto(0, 250)
        self.pd()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score}",
                   align="center", font=("Arial", 24, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"Game Over",
                   align="center", font=("Arial", 48, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
