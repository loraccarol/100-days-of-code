import turtle as t
import random

turtle = t.Turtle()
t.colormode(255)

turtle.speed("fastest")

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    return (r,g,b)

def draw(size_of_gap):
    for _ in range(int(360/ size_of_gap)):
        turtle.color(random_color())
        turtle.circle(50)
        turtle.setheading(turtle.heading() + size_of_gap)

draw(20)