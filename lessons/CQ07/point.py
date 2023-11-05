"""Creating a point class with both an x and a y attribute."""

from __future__ import annotations

__author__ = "730642974"


class Point:
    """This is my class to represent Point."""
    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
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