"""Making a wordle."""

__author__ = "730642974"


def contains_char(searched_word: str, one_character: str) -> bool:
    """Searches for the character in the word."""
    assert len(one_character) == 1
    searched_idx: int = 0
    contained_char: bool = False
    # When the index is less than the length of the searched word and the word doesn't contain the searched-for character:
    while not (contained_char is True) and (len(searched_word) > searched_idx):
        # If the character is the same as the character in that index of the searched word, return True, saying the word does contain the character
        if one_character == searched_word[searched_idx]:
            contained_char = True
            return True
        # If the character isn't in that index of the word, move to the next index.
        elif one_character != searched_word[searched_idx]:
            searched_idx += 1
    # If you reach the end of the word and haven't matched the character to a character in teh wrod, return False to say the character isn't in the word.
    return False


def emojified(guess: str, secret: str) -> str:
    """Emoji string determines contains_char accuracy."""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    secret_idx: int = 0
    guess_emoji: str = ""
    # While you haven't reached the end of the word:
    while secret_idx < len(secret):
        # If the index of the guess is the same as the index of the secret, add a green box emoji to the emoji string.
        if guess[secret_idx] == secret[secret_idx]:
            guess_emoji += GREEN_BOX
        # If the index of the guess isn't the same as the index of the secret:
        elif guess[secret_idx] != secret[secret_idx]:
            # If the secret word contains the character of the guess in that index, add a yellow box to the emoji string to show the character is in the secret, but in the wrong spot.
            if contains_char(secret, guess[secret_idx]) is True:
                guess_emoji += YELLOW_BOX
            # If the secret word doesn't contain the character of the guess in that index, add a while box to show the character isn't in the word.
            elif contains_char(secret, guess[secret_idx]) is False:
                guess_emoji += WHITE_BOX
        # Move to the next index and run it again.
        secret_idx += 1
    # After you reach the end of the word, return the resulting emoji string indicating what characters are in the correct/incorrect places.
    return guess_emoji


def input_guess(expected_len: int) -> str:
    """Prompts user to input a guess of expected length."""
    # Ask the user to input a guess word the length of the secet word.
    guess: str = input(f"Enter a {str(expected_len)} character word: ")
    # If the length of the guess isn't the length of the secret, tell them it wasn't the right length and prompt them to try again.
    while len(guess) != expected_len:
        print(f"That wasn't {str(expected_len)} chars! Try again: ")
        guess = str(input())
    # Return their inputted guess.
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    numguesses: int = 1
    secret: str = "codes"
    max_tries: int = 6
    win: bool = False
    # while you haven't won and you haven't run out of guesses, print the turn number, prompt for input, and initialize the resulting emoji string to show how accurate the guess was.
    while not (win is True) and (numguesses <= max_tries):
        print(f"=== Turn {numguesses}/{max_tries} ===")
        guesses: str = input_guess(len(secret))
        emojis: str = emojified(guesses, secret)
        # If you guessed the secret, set win to be True
        if guesses == secret:
            win = True
        # Increase your number of guesses by one, and print the emojis to show the user if they've done well or not.
        numguesses += 1
        print(emojis)
    # If you've won, print how many guesses it took to win and exit the program.
    if (win is True):
        print(f"You won in {numguesses - 1}/{max_tries} turns!")
    # If you didn't win and you're out of guesses, tell them to try again tomorrow and exit the program.
    elif (win is False):
        print(f"X/{max_tries} - Sorry, try again tomorrow! ")


if __name__ == "__main__":
    main()