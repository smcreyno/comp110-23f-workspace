"""Test my zip function."""
__author__ = "730642974"

from lessons.zip import zip


def test_diff_len() -> None:
    """Lists of different lengths should return {}."""
    test_list1: list[str] = ["a", "b", "c"]
    test_list2: list[int] = [1, 2]
    assert zip(test_list1, test_list2) == {}


def test_empty_list() -> None:
    """Two empty lists should return {}."""
    test_list1: list[str] = []
    test_list2: list[int] = []
    assert zip(test_list1, test_list2) == {}


def test_list_len_3() -> None:
    """Two lists of length 3 will return a dict."""
    test_list1: list[str] = ["a", "b", "c"]
    test_list2: list[int] = [1, 2, 3]
    assert zip(test_list1, test_list2) == {"a": 1, "b": 2, "c": 3}