import turtle as t
import random


turtle = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    return (r,g,b)


turtle.pensize(5)

directions = [0, 90, 180, 270]

def random_walk():
    turtle.pencolor(random_color())
    turtle.setheading(random.choice(directions))
    turtle.forward(50)

for _ in range(100):
    random_walk()
