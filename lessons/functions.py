"""Demonstrates functions."""
# must import from python library, can use this to find functions to use
from random import randint

# A function doesn't necessarily have to return something, it just has to do something.
y: str = print("Hello!")
print(y)
# None is printed because the value of y is none

x: int = round(10.25)
print(x)

z: int = randint(1,7)
print(z)
# every time you run it, it returns a new random integer
# Unlike in math, one function does not return one output for each input