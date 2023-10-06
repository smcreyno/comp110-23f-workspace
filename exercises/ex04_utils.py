"""List Utility Functions."""

__author__ = "730642974"


def all(your_set: list[int], your_num: int) -> bool:
    """Shows if the whole list is the same as the int."""
    set_idx: int = 0
    if len(your_set) == 0:
        return False
    while (len(your_set) - 1 >= set_idx):
        if your_set[set_idx] != your_num:
            return False
        elif your_set[set_idx] == your_num:
            set_idx += 1
    return True


def max(int_list: list[int]) -> int:
    """Return the largest int, or ValueError if empty."""
    if len(int_list) == 0:
        raise ValueError("max() arg is an empty List")
    list_idx: int = 0
    initial_max: int = int(int_list[0])
    while len(int_list) - 1 >= list_idx:
        current_max: int = int(int_list[list_idx])
        if (current_max > initial_max):
            initial_max = current_max
        list_idx += 1
    return initial_max


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Return true if every element at every index is equal."""
    list1_idx: int = 0
    if len(list1) != len(list2):
        return False
    while (list1_idx <= len(list1) - 1):
        if list1[list1_idx] != list2[list1_idx]:
            return False
        list1_idx += 1
    return True