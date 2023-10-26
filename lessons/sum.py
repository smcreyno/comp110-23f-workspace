"""Summing the elements of a list using different loops."""

__author__ = "730642974"


def w_sum(vals: list[float]) -> float:
    """Takes an input of a list of floats and returns the sum of all elements using a while loop."""
    idx: int = 0
    sum: float = 0.0
    while (idx < len(vals)):
        if len(vals) == 0:
            return 0.0
        else:
            sum += vals[idx]
        idx += 1
    return sum


def f_sum(vals: list[float]) -> float:
    """Takes an input of a list and returns the sum using a for loop."""
    sum: float = 0.0
    for elem in vals:
        sum += elem
    return sum


def f_range_sum(vals: list[float]) -> float:
    """Takes an input of a list and returns the sum using a for in range loop."""
    sum: float = 0.0
    for idx in range(0, len(vals)):
        elem: float = vals[idx]
        sum += elem
    return sum