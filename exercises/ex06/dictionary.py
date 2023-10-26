"""Practice with dictionary functions."""

__author__ = "730642974"


def invert(my_dict: dict[str, str]) -> dict[str, str]:
    """Invert the keys and values of a given dictionary."""
    check_dict: dict[str, int] = {}
    new_dict: dict[str, str] = {}
    for keys in my_dict:
        if my_dict[keys] in check_dict:
            check_dict[my_dict[keys]] += 1
        else:
            check_dict[my_dict[keys]] = 1
    idx: int = check_dict[my_dict[keys]]
    if idx > 1:
        raise KeyError("Try again: cannot have two identical keys.")
    else:
        for keys in my_dict:
            new_dict[my_dict[keys]] = keys
        return new_dict
        

def favorite_color(color_dict: dict[str, str]) -> str:
    """Takes a dict of favorite colors, returns most popular color."""
    check_dict: dict[str, int] = {}
    for key in color_dict:
        if color_dict[key] in check_dict:
            check_dict[color_dict[key]] += 1
        else:
            check_dict[color_dict[key]] = 1
    new_fav: str = ""
    count: int = 0
    for elem in check_dict:
        if check_dict[elem] > count:
            count = check_dict[elem]
            new_fav = elem
    return new_fav


def count(my_list: list[str]) -> dict[str, int]:
    """Each value is a count of the number of times that key appears."""
    new_dict: dict[str, int] = {}
    for item in my_list:
        if item in new_dict:
            new_dict[item] += 1
        else:
            new_dict[item] = 1
    return new_dict


def alphabetizer(alpha_list: list[str]) -> dict[str, list[str]]:
    """Produce a dictionary where each key is a unique letter and each value is a list of words beginnning with that letter."""
    alpha_dict: dict[str, list[str]] = {}
    first_char: str = ""
    for elem in alpha_list:
        first_char = elem[0]
        first_char = first_char.lower()
        if first_char in alpha_dict:
            alpha_dict[first_char] += [elem]
        else:
            alpha_dict[first_char] = [elem]
    return alpha_dict


def update_attendance(attend_dict: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """Given a dict, mutate and return that dict with new attendance info."""
    for elem in attend_dict:
        if day == elem:
            if not (student in attend_dict[elem]):
                attend_dict[elem] += [student]
    if (day in attend_dict) is False:
        attend_dict[day] = [student]
    return attend_dict