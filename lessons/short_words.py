"""Short words."""

__author__ = "730642974"


def short_words(a_list: list[str]) -> list[str]:
    """Return list of words that are shorter than 5 characters."""
    new_list: list[str] = []
    for elem in a_list:
        if len(elem) < 5:
            new_list.append(elem)
        else:
            print(f"{elem} is too long!")
    return new_list