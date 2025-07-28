from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, xpos):
        super().__init__()
        self.xpos = xpos
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(xpos, 0)

    def up(self):
        newy = self.ycor()
        self.goto(self.xpos, newy+25)

    def down(self):
        newy = self.ycor()
        self.goto(self.xpos, newy-25)