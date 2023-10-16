"""Calling with two arguments."""

def contains(needle: int, haystack: list[int]) -> bool:
    """Searching for needle in the haystack."""
    list_idx: int = 0
    found: bool = False
    while (list_idx <= len(haystack) - 1) and not(found is True):
        if needle == haystack[list_idx]:
            found = True
        elif needle != haystack[list_idx]:
            found = False
        list_idx += 1
    return found