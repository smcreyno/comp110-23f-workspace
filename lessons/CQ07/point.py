"""Creating a point class with both an x and a y attribute."""

from __future__ import annotations

__author__ = "730642974"


class Point:
    """This is my class to represent Point."""
    x: float
    y: float

    def __init__(self, x_init: float = 0.0, y_init: float = 0.0):
        """Constructor."""
        self.x = x_init
        self.y = y_init
        # returns self
    
    def scale_by(self, factor: int) -> None:
        """Mutates a point."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int) -> Point:
        """Creates a new point."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point
    
    def __str__(self) -> str:
        """Returning the Point as a string."""
        p_string: str = f"x: {self.x}; y: {self.y}"
        return p_string
    
    def __mul__(self, factor: int | float) -> Point:
        """Returning a new point from mul."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point
    
    def __add__(self, amount: int | float) -> Point:
        """Returning a new point from add."""
        new_point: Point = Point(self.x + amount, self.y + amount)
        return new_point