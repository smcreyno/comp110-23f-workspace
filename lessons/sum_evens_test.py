"""Testing my sum of evens function."""

from lessons.sum_evens import sum_evens_of_list

def test_empty_list() -> None:
    """Tests sum_evens_of_list([]) should return 0."""
    assert sum_evens_of_list([]) == 0


def test_sum_one_element() -> None:
    """sum_evens_of_list([2]) = 2."""
    test_list: list[int] = [2]
    assert sum_evens_of_list(test_list) == 2


def test_sum_positives() -> None:
    """sum_evens_of_list of a list of positive numbers."""
    test_list: list[int] = [1, 2, 3, 4]
    assert sum_evens_of_list(test_list) == 6


def test_sum_neg_and_positives() -> None:
    """sum_evens_of_list of a list with negatives and positives."""
    test_list: list[int] = [-1, -2, 3, 4]
    assert sum_evens_of_list(test_list) == 2