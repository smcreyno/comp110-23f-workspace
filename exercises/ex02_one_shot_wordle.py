"""EX02 One-Shot Wordle."""

__author__ = "730642974"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
secret: str = "python"
guess: str = input(f"What is your {str(len(secret))}-letter guess? ")
secret_idx: int = 0
guess_emoji: str = ""
alt_idx: int = 0
while len(guess) != len(secret):
    # when the length of the guess word isn't the same as the length of the secret word
    print(f"That was not {str(len(secret))} letters! Try again: ")
    guess = str(input())
    # prompt for new guess that is the length of the secret word
while secret_idx < len(secret):
    # when the index of the secret word is less than the length of the secret:
    if guess[secret_idx] == secret[secret_idx]:
        # if the character of the guess is the same as the character of the secret in that index, print a green box.
        guess_emoji = guess_emoji + GREEN_BOX
    else:
        close_guess: bool = False
        while not (close_guess is True) and (alt_idx < len(secret)):
            # when you don't have a correct character out of place AND the index of the guess is less than the length of the secret word:
            if secret[alt_idx] == guess[secret_idx]:
                # if the alternate character of the secret word is the same as the character of the guess, you have a close guess
                close_guess = True
            elif secret[alt_idx] != guess[secret_idx]:
                # else, if the alternate charcter of secret is not the same as the guess character, check the next index
                alt_idx = alt_idx + 1
        if alt_idx >= len(secret):
            # if the alternate index is at least the length of the secret word, reset it to zero and reevaluate for letters in prior positions that the first loop may have missed.
            alt_idx = int(0)  
            while not (close_guess is True) and (alt_idx < len(secret)):
                if secret[alt_idx] == guess[secret_idx]:
                    close_guess = True
                else:
                    alt_idx = alt_idx + 1
        if (close_guess is True):
            # if you have a close guess, print a yellow box, and if not, print a white box.
            guess_emoji = guess_emoji + YELLOW_BOX
        else:
            guess_emoji = guess_emoji + WHITE_BOX
    secret_idx = secret_idx + 1
    # proceed to increase the index to evaluate the next character
if secret != guess:
    # if you guessed wrong, print your emojis to show what characters were right, and exit
    print(str(guess_emoji))
    print("Not quite. Play again soon!")
else:
    # if you didn't get it wrong, you got it right! You will have a string of green boxes as your trophy.
    print(str(guess_emoji))
    print("Woo! You got it!")