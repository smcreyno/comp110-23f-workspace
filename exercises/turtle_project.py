"""A very cute house colored randomly (using the randint function to determine the RBG color)."""

__author__ = 730642974


from random import randint
from turtle import Turtle, colormode, done
colormode(255)


def main() -> None:
    """The entrypoint of my scene."""
    susan: Turtle = Turtle()
    sun(susan, 225, 350)
    ronald: Turtle = Turtle()
    roof(ronald, 40, 100, 200)
    sybill: Turtle = Turtle()
    square(sybill, 200, 100, 400, 90)
    wayne: Turtle = Turtle()
    window(wayne, 50, 0, 75, 0)
    william: Turtle = Turtle()
    window(william, -100, 0, -75, 0)
    wanda: Turtle = Turtle()
    window(wanda, -100, -150, -75, -150)
    dan: Turtle = Turtle()
    door(dan, 50, -150)
    done()


def roof(the_roof: Turtle, x: float, y: float, line: float) -> None:
    """Draw a roof for the house."""
    the_roof.pencolor(255, 255, 255)
    the_roof.fillcolor(randint(0, 255), randint(0, 255), randint(0, 255))
    the_roof.penup()
    the_roof.goto(x, y)
    the_roof.setheading(0.0)
    the_roof.pendown()
    the_roof.begin_fill()
    the_roof.forward(line)
    the_roof.left(135)
    the_roof.forward(line)
    the_roof.left(45)
    the_roof.forward(line)
    the_roof.left(45)
    the_roof.forward(line)
    the_roof.left(135)
    the_roof.forward(285)
    the_roof.end_fill()
    the_roof.hideturtle()


def square(walls: Turtle, x: float, y: float, width: float, angle: float) -> None:
    """Draw the main body of the house."""
    walls.pencolor(255, 255, 255)
    walls.fillcolor(randint(0, 255), randint(0, 255), randint(0, 255))
    walls.penup()
    walls.goto(x, y)
    walls.setheading(0.0)
    walls.pendown()
    walls.begin_fill()
    i: int = 0
    while (i < 3):
        walls.right(angle)
        walls.forward(width)
        i += 1
    walls.end_fill()
    ground(walls, -500, -300)
    walls.hideturtle()


def ground(line: Turtle, x: float, y: float) -> None:
    """A ground line."""
    line.pencolor(255, 255, 255)
    line.color(randint(0, 255), randint(0, 255), randint(0, 255))
    line.penup()
    line.goto(x, y)
    line.setheading(0.0)
    line.pendown()
    line.begin_fill()
    i: int = 0
    while i < 2:
        line.forward(1000)
        line.right(90)
        line.forward(100)
        line.right(90)
        i += 1
    line.end_fill()


def window(box: Turtle, x: float, y: float, a: float, b: float) -> None:
    """Draw the windows of the house."""
    box.pencolor(255, 255, 255)
    box.fillcolor(randint(0, 255), randint(0, 255), randint(0, 255))
    box.penup()
    box.goto(x, y)
    box.setheading(0.0)
    box.pendown()
    box.begin_fill()
    i: int = 0
    while (i < 4):
        box.forward(50)
        box.right(90)
        i += 1
    if i >= 4:
        box.penup()
        box.goto(a, b)
        box.setheading(0.0)
        box.pendown()
        box.right(90)
        box.forward(25)
        box.right(90)
        box.forward(25)
        box.left(180)
        box.forward(50)
        box.right(180)
        box.forward(25)
        box.left(90)
        box.forward(25)  
    box.end_fill()
    box.hideturtle() 


def door(rec: Turtle, x: float, y: float) -> None:
    """Draw the door to the house and a knob."""
    rec.pencolor(255, 255, 255)
    rec.fillcolor(randint(0, 255), randint(0, 255), randint(0, 255))
    rec.penup()
    rec.goto(x, y)
    rec.setheading(0.0)
    rec.pendown()
    rec.begin_fill()
    i: int = 0
    while i < 2:
        rec.forward(75)
        rec.right(90)
        rec.forward(150)
        rec.right(90) 
        i += 1  
    rec.end_fill()
    handle(rec, 110, -225)  
    rec.hideturtle()


def handle(line: Turtle, x: float, y: float) -> None:
    """An octogonal door handle."""  
    line.fillcolor(randint(0, 255), randint(0, 255), randint(0, 255))
    line.penup()
    line.goto(x, y)
    line.setheading(0.0)
    line.pendown()
    line.begin_fill()
    i: int = 0
    while i < 8:
        line.forward(3)
        line.right(45)
        i += 1
    line.end_fill()
    line.hideturtle()


def sun(circle: Turtle, x: float, y: float) -> None:
    """A pretty sun!"""
    circle.color(randint(0, 255), randint(0, 255), randint(0, 255))
    circle.penup()
    circle.goto(x, y)
    circle.setheading(0.0)
    circle.pendown
    circle.begin_fill()
    i: int = 0
    while i < 36:
        circle.forward(10)
        circle.right(10)
        i += 1
    circle.end_fill()
    circle.hideturtle


if __name__ == "__main__":
    main()
