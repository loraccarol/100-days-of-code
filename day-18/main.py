# import colorgram

# colors = colorgram.extract('painting.jpg', 6)

# color_list = []
# for i in range(len(colors)):
#     rgb = colors[i].rgb
#     red = rgb[0]
#     green = rgb[1]
#     blue = rgb[2]
#     color_list.append((red,green,blue))

import turtle as t
import random

color_list = [(249, 248, 243), (250, 245, 248), (243, 250, 246), (241, 246, 250), (234, 225, 83), (195, 8, 69)]

turtle = t.Turtle()
screen = t.Screen()
t.colormode(255)

turtle.speed("fastest")
turtle.penup()
turtle.hideturtle()

altura = -250
turtle.sety(altura)

for h in range(10):

    turtle.setx(-200)

    for _ in range(10):
        turtle.color(random.choice(color_list))
        turtle.dot(20)
        turtle.forward(50)

    altura += 50
    turtle.sety(altura)

screen.exitonclick()