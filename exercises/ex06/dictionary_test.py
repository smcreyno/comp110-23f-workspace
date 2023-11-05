"""Testing the dictionary utils."""

from exercises.ex06.dictionary import invert
from exercises.ex06.dictionary import favorite_color
from exercises.ex06.dictionary import count
from exercises.ex06.dictionary import alphabetizer
from exercises.ex06.dictionary import update_attendance
import pytest


__author__ = "730642974"


def test_invert_empty() -> None:
    """Inverting an empty list returns an empty list."""
    test_dict: dict[str, str] = {}
    assert invert(test_dict) == {}


def test_invert_alpha() -> None:
    """Inverting an alphabetical dict."""
    test_dict: dict[str, str] = {"a": "z", "b": "y", "c": "x"}
    new_dict: dict[str, str] = {"z": "a", "y": "b", "x": "c"}
    assert invert(test_dict) == new_dict


def test_invert_keyerror() -> None:
    """Raising a KeyError when two values are the same."""
    my_dictionary: dict[str, str] = {}
    with pytest.raises(KeyError):
        my_dictionary = {"michael": "jordan", "kris": "jordan"}
        invert(my_dictionary)


def test_favcolor_empty() -> None:
    """An empty dict returns ""."""
    test_dict: dict[str, str] = {}
    assert favorite_color(test_dict) == ""


def test_same_colors() -> None:
    """Returns first color when there are multiple most common colors."""
    test_dict: dict[str, str] = {"a": "yellow", "b": "blue", "c": "pink", "d": "blue", "e": "pink"}
    assert favorite_color(test_dict) == "blue"


def test_all_same() -> None:
    """A dict of all the same colors will return that color."""
    test_dict: dict[str, str] = {"s": "blue", "b": "blue", "a": "blue"}
    assert favorite_color(test_dict) == "blue"


def test_count_empty() -> None:
    """Returns an empty dict if given an empty list."""
    test_list: list[str] = ()
    assert count(test_list) == {}


def test_count_one_item() -> None:
    """A list of one item returns a dict count of 1."""
    test_list: list[str] = ["apple"]
    assert count(test_list) == {"apple": 1}


def test_count_repeats() -> None:
    """A list of repeating items returns a dict count the length of the list."""
    new_list: list[str] = ["a", "a", "a"]
    assert count(new_list) == {"a": 3}


def test_alpha_empty() -> None:
    """An empty list will return an empty dict."""
    test_list: list[str] = ()
    assert alphabetizer(test_list) == {}


def test_alpha_uppercase() -> None:
    """A capitalized list will return a lowercase dict."""
    test_list: list[str] = ["Apple", "Xylophone", "Big", "Nasty"]
    assert alphabetizer(test_list) == {"a": ["Apple"], "x": ["Xylophone"], "b": ["Big"], "n": ["Nasty"]}


def test_alpha_same_letter() -> None:
    """A list of words beginning with the same letter creates a dict with only one key."""
    test_list: list[str] = ["apple", "ace", "acid"]
    assert alphabetizer(test_list) == {"a": ["apple", "ace", "acid"]}


def test_update_attendance_absent() -> None:
    """No one in attendance will return the same dict as in the beginning."""
    test_dict: dict[str, list[str]] = {"Monday": ["Sam", "Sally"], "Tuesday": ["Sam"]}
    assert update_attendance(test_dict, str(), str()) == {"Monday": ["Sam", "Sally"], "Tuesday": ["Sam"]}


def test_update_attendance_same_day() -> None:
    """A day that already exists in the attendance log will have its names added to the log under the same day key."""
    test_dict: dict[str, list[str]] = {"Monday": ["Sam", "Sally"], "Tuesday": ["Sam"]}
    day: str = "Tuesday"
    student: str = "Sally"
    assert update_attendance(test_dict, day, student) == {"Monday": ["Sam", "Sally"], "Tuesday": ["Sam", "Sally"]}


def test_update_attendance_new_day() -> None:
    """A day not yet in the log will be added as a key with the values as 'student'."""
    test_dict: dict[str, list[str]] = {"Monday": ["Sam", "Sally"], "Tuesday": ["Sam"]}
    day: str = "Wednesday"
    student: str = "Sophia"
    assert update_attendance(test_dict, day, student) == {"Monday": ["Sam", "Sally"], "Tuesday": ["Sam"], "Wednesday": ["Sophia"]}