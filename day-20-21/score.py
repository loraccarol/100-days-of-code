from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.goto(0, 260)
        self.hideturtle()
        self.score = 0
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", False, "center",  font=('Comic Sans MS', 20, 'normal'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over.", False, "center",  font=('Comic Sans MS', 20, 'normal'))