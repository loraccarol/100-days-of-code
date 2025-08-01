from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def turn_right():
    tim.right(10)

def turn_left():
    tim.left(10)

def clear_screen():
    tim.reset()

screen.listen()
screen.onkey(key="w",fun=move_forward)
screen.onkey(key="s",fun=move_backwards)
screen.onkey(key="a",fun=turn_left)
screen.onkey(key="d",fun=turn_right)

screen.onkey(key="c",fun=clear_screen)
screen.exitonclick()