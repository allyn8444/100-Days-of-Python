import turtle
from turtle import Turtle, Screen
from random import Random

timmy = Turtle()
screen = Screen()
rand = Random()

# timmy.color("white")
timmy.shape("turtle")


def rand_color():
    r = round(rand.random(), 2)
    g = round(rand.random(), 2)
    b = round(rand.random(), 2)
    random_color = (r, g, b)
    return random_color


# # ====== CHALLENGE 1: SQUARE ========= #
# for i in range(4):
#     timmy.forward(100)
#     timmy.right(90)

# ===== CHALLENGE 2: DASHED LINE ===== #
# for i in range(10):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()
#     timmy.forward(10)


# CHALLENGE 3: triangle (3), square (4), pentagon (5) until decagon (10)
# def draw_shape(shape_sides):
#     r = round(rand.random(), 2)
#     g = round(rand.random(), 2)
#     b = round(rand.random(), 2)
#     timmy.pencolor(r, g, b)  # generates random color each shape
#     angle = 360 / shape_sides
#     for i in range(shape_sides):
#         timmy.right(angle)
#         timmy.forward(100)
#
#
# for shape in range(3, 11):
#     draw_shape(shape)


# ==== CHALLENGE 4: Generate Random Walk ==== #
# angles = [0, 90, 180, 270]
# for i in range(50):
#     r = round(rand.random(), 2)
#     g = round(rand.random(), 2)
#     b = round(rand.random(), 2)
#     timmy.pensize(5)
#     timmy.speed("fast")
#     timmy.pencolor(r, g, b)  # generates random color each shape
#     # angle = int(rand.random() * 360)  # this is totally random
#     timmy.right(rand.choice(angles))  # contains defined angles
#     timmy.forward(20)


# ===== CHALLENGE 5: Spirograph ===== #
# circles_count = 100
# for i in range(circles_count):
#     timmy.color(rand_color())
#     timmy.speed("fastest")
#     timmy.penup()
#     timmy.right(360/circles_count)
#     timmy.pendown()
#     timmy.circle(100)

# ====== DAY 18 PROJECT: The Hirst Painting ======= #
timmy.speed("fastest")
turtle.colormode(255)  # so that it won't throw an error
timmy.penup()  # to make line hidden
timmy.hideturtle()  # to make turtle icon hidden
color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]

# set starting position:
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)

number_of_dots = 100
for dot_count in range(1, number_of_dots + 1):
    timmy.dot(20, rand.choice(color_list))
    timmy.forward(50)

    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)


# screen code should be after the turtle code
# screen.bgcolor("black")
screen.exitonclick()



