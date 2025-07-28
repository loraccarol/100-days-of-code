from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x = 10
        self.y = 10

    def move(self):
        self.goto(self.xcor() + self.x, self.ycor() + self.y)

    def detect_collision(self, obj):
        if obj == "wall":
            self.y *= -1
        if obj == "paddle":
            self.x *= -1

    def reset_game(self):
        self.goto(0, 0)
        self.x *= -1