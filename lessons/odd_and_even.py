"""Odd and even."""

__author__ = "730642974"


def odd_and_even(num_list: list[int]) -> list[int]:
    """Return a new list containing elems that are odd and have an even index."""
    new_list: list[int] = []
    i: int = 0
    while i < len(num_list):
        if (i % 2 == 0) and (num_list[i] % 2 == 1):
            new_list.append(num_list[i])
        i += 1
    return new_list