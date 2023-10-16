"""Turtle Tutorial."""

from turtle import Turtle, colormode, done
colormode(255)
leo: Turtle = Turtle()
leo.speed(50)

leo.penup()
leo.goto(-150, -100)
leo.pendown()

leo.color(249, 174, 242)
side_length: int = 300
leo.begin_fill()
i: int = 0
while (i < 3):
    leo.forward(side_length)
    leo.left(120)
    i += 1
leo.end_fill()

bob: Turtle = Turtle()
bob.penup()
bob.goto(-150, -100)
bob.pendown()
bob.speed(100)
bob.pencolor(112, 40, 90)
idx: int = 0
while (idx < 100):
    bob.forward(side_length)
    bob.left(123)
    side_length *= 0.97
    idx += 1

done()