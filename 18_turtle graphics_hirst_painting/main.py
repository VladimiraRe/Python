import turtle
from turtle import Turtle, Screen
from random import choice

# import colorgram
#
# colors = colorgram.extract('image.jpg', 20)
#
# colors_rgb = []
#
# for i in colors:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     colors_rgb.append((r, g, b))
#
# print(colors_rgb)

color_list = [(173, 43, 52), (219, 213, 124), (101, 158, 114), (103, 168, 225), (129, 18, 34),
              (200, 153, 76), (174, 141, 188), (43, 42, 40), (3, 153, 171), (1, 52, 92),
              (121, 118, 161), (82, 168, 99), (127, 59, 58), (101, 9, 23), (24, 160, 176), (187, 84, 94)]

t = Turtle()
turtle.colormode(255)
t.speed("fastest")
t.penup()
t.hideturtle()

t.setheading(225)
t.forward(350)
t.setheading(0)

for _ in range(10):

    for _ in range(10):
        t.dot(20, choice(color_list))
        t.forward(50)

    t.setheading(90)
    t.forward(50)
    t.setheading(180)
    t.forward(500)
    t.setheading(0)

screen = Screen()
screen.exitonclick()
