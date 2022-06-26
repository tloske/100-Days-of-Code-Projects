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
        with open('highscore.txt') as file:
            self.highscore = int(file.read())
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.highscore}",
                   align="center", font=("Arial", 24, "normal"))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open('highscore.txt', 'w') as file:
                file.write(f'{self.highscore}')
        self.score = 0
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"Game Over",
                   align="center", font=("Arial", 48, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
