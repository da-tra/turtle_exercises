from turtle import Turtle, Screen
from random import randint

screen = Screen()
tim = Turtle()
tim.shape("turtle")

# for side in range(0, 4):
#     tim.right(90)
#     tim.forward(100)

""" dotted line
tim.pu()
tim.goto(-300,0)
tim.pd()

for _ in range (0, 51):
    tim.forward(5)
    tim.penup()
    tim.forward(5)
    tim.pendown()
 """

""" different polygons stacked: from 3 to 10 corners
screen.colormode(255)

# for _ in range(3, 9):
    # tim.color(
    #     randint(0, 255),
    #     randint(0, 255),
    #     randint(0, 255))
#     sides = int(_)
#     angle = 360 / sides
#     for line in range(0, sides):
#         tim.forward(100)
#         tim.right(angle)


def draw_shape(num_sides):
    angle = 360/ num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

max_corners = 10
for i in range(3, max_corners + 1):
    tim.color(
        randint(0, 255),
        randint(0, 255),
        randint(0, 255))
    draw_shape(i) """


# random walk: 

screen.colormode(255)
# set speed
tim.speed(9)

# define distance, set angle to 90, set number of lines, 
stride = 25
angle = 60
extent = 200
thickness = 8
# choose color palette, set line shape and thickness
color_palette = [(23,126,126), (126,23,126), (174,189,55), (35,191,191), (6,37,37)]


# print(random_color)

tim.pensize(thickness)
tim.forward(stride)

for n in range(0, extent):
    random_angle = (angle * randint(-4, 4))
    random_color = color_palette[randint(0, len(color_palette) - 1)]
    tim.color(random_color)    
    tim.right(random_angle)
    tim.forward(stride)
    







screen.exitonclick()