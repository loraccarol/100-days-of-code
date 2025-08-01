from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.size = 3
        initial_pos = 0
        for _ in range(0, self.size):
            t = Turtle('square')
            t.penup()
            t.color("white")
            t.goto(initial_pos,0)
            initial_pos -= 20
            self.segments.append(t)
        self.head = self.segments[0]


    def add_segments(self, position):
        t = Turtle('square')
        t.penup()
        t.color("white")
        t.goto(position)
        self.segments.append(t)

    def extend(self):
        self.add_segments(self.segments[-1].position())
        
    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)