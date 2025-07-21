from turtle import Turtle, Screen
import random

race = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput("your bet:", prompt="Which turtle will win the race?")
colors = ['blue','red','purple','pink','green','yellow']
turtles = []

y = -40
for i in colors:
    t = Turtle('turtle')
    t.penup()
    t.color(i)
    t.goto(-230, y)
    y += 25
    turtles.append(t)

if user_bet:
    race = True

while race:
    for t in turtles:
        if (t.pos()[0] > 230):
            race = False
            if (t.pencolor() == user_bet):
                print("You win")
            else:
                print(f"You lose. The winner was the {t.pencolor()}")
        random_distance = random.randint(0,10)
        t.forward(random_distance)


screen.exitonclick()