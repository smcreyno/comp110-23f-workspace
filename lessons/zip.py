"""Combining two lists into a dictionary."""

__author__ = "730642974"


def zip(list1: list[str], list2: list[int]) -> dict[str, int]:
    """Produce a dictionary where keys are items of list1 and values are items at the same index of list2."""
    if len(list1) != len(list2):
        return dict()
    else:
        my_dict: dict[str, int] = {}
        idx1: int = 0
        idx2: int = 0
        while idx1 < len(list1):
            my_dict[list1[idx1]] = list2[idx2]
            idx1 += 1
            idx2 += 1
    return my_dict