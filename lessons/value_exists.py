"""Value exists function."""

__author__ = "730642974"


def value_exists(value_dict: dict[str, int], val: int) -> bool:
    """Does the value exist in the dict?"""
    for elem in value_dict:
        if value_dict[elem] == val:
            return True
    return False