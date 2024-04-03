import turtle
import random
import time

# Set up the screen
screen = turtle.Screen()
screen.title("X Snake Game")
screen.bgcolor("black")
screen.setup(width=900, height=900)
screen.tracer(0)  # Turn off automatic screen updates

# Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.goto(-290, 290)
border_pen.pendown()
border_pen.pensize(3)
for _ in range(4):
    border_pen.fd(580)
    border_pen.rt(90)
border_pen.hideturtle()







































# Snake head
head = turtle.Turtle()
head.speed(0)  # Animation speed (0=fastest)
head.shape("square")
head.color("white")
head.penup()  # Don't draw lines while moving
head.goto(0, 0)
head.direction = "stop"  # Initially, the snake doesn't move


