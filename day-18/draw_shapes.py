from turtle import Turtle, Screen

turtle = Turtle()

def draw(number_of_sides):
    for _ in range(number_of_sides):
        turtle.forward(50)
        turtle.left(360/number_of_sides)


for i in range(3, 11):
    draw(i)


screen = Screen()
screen.exitonclick()