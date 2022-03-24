from turtle import Turtle, Screen
import turtle
import random

color_list = [(159, 153, 149), (125, 104, 87), (213, 211, 207), (219, 220, 224), (168, 159, 162), (213, 208, 211), (53, 25, 11), (10, 28, 50), (157, 167, 177), (131, 79, 91), (155, 170, 161), (65, 100, 121), (62, 15, 24), (212, 219, 214), (16, 40, 25), (73, 111, 88), (156, 141, 70), (125, 26, 38), (200, 195, 173), (127, 34, 19), (166, 103, 117), (145, 119, 115), (200, 186, 190), (90, 76, 18), (35, 83, 47), (35, 59, 102), (188, 189, 199), (100, 145, 123), (205, 185, 182), (18, 81, 99)]

tim = Turtle()
turtle.colormode(255)

# tim.pensize(1)
tim.speed(4)


def dot_forward():
    for i in range(9):
        tim.dot(20, random.choice(color_list))
        tim.pu()
        tim.forward(50)


def dot_upf():
    tim.dot(20, random.choice(color_list))
    tim.seth(90)
    tim.pu()
    tim.forward(50)
    tim.seth(180)
    tim.pu()
    tim.forward(450)
    tim.seth(0)


for _ in range(10):
    dot_forward()
    dot_upf()


tim2 = Screen()
tim2.screensize(8000, 20000)
tim2.exitonclick()
