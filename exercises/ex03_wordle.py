"""Making a wordle."""

__author__ = "730642974"


def contains_char(searched_word: str, one_character: str) -> bool:
    """Searches for the character in the word."""
    assert len(one_character) == 1
    searched_idx: int = 0
    contained_char: bool = False
    while not (contained_char is True) and (len(searched_word) > searched_idx):
        if one_character == searched_word[searched_idx]:
            contained_char = True
            return True
        elif one_character != searched_word[searched_idx]:
            searched_idx += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Emoji string determines contains_char accuracy."""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    secret_idx: int = 0
    guess_emoji: str = ""
    while secret_idx < len(secret):
        if guess[secret_idx] == secret[secret_idx]:
            guess_emoji += GREEN_BOX
        elif guess[secret_idx] != secret[secret_idx]:
            if contains_char(secret, guess[secret_idx]) is True:
                guess_emoji += YELLOW_BOX
            elif contains_char(secret, guess[secret_idx]) is False:
                guess_emoji += WHITE_BOX
        secret_idx += 1
    return guess_emoji


def input_guess(expected_len: int) -> str:
    """Prompts user to input a guess of expected length."""
    guess: str = input(f"Enter a {str(expected_len)} character word: ")
    while len(guess) != expected_len:
        print(f"That wasn't {str(expected_len)} chars! Try again: ")
        guess = str(input())
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    numguesses: int = 1
    secret: str = "codes"
    max_tries: int = 6
    win: bool = False
    while not (win is True) and (numguesses <= max_tries):
        print(f"=== Turn {numguesses}/{max_tries} ===")
        guesses: str = input_guess(len(secret))
        emojis: str = emojified(guesses, secret)
        if guesses == secret:
            win = True
        numguesses += 1
        print(emojis)
    if (win is True):
        print(f"You won in {numguesses - 1}/{max_tries} turns!")
    elif (win is False):
        print(f"X/{max_tries} - Sorry, try again tomorrow! ")


if __name__ == "__main__":
    main()