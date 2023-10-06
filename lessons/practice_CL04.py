"""Practice writing functions."""
def mimic_letter(my_words: str, letter_idx: int) -> str:
    """Outputs the character of my_words at index letter_idx."""
    if len(my_words) > letter_idx:
        return my_words[letter_idx]
    else:
        return "Index too high."
print(mimic_letter("hello", 5))

"""While loop memory diagram."""
xs: str = "123"
ys: str = "45"

x_idx: int = 0
while x_idx < len(xs):
    y_idx: int = 0
    while y_idx < len(ys):
        print(f"({xs[x_idx]}, {ys[y_idx]})")
        y_idx = y_idx +1
    x_idx = x_idx + 1