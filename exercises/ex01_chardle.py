"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730642974"

word: str = input("Enter a 5-character word: ")
if len(word) != 5:
    print("Error: Word must contain 5 characters ")
    exit()
character: str = input("Enter a single character: ")
if len(character) != 1:
    print("Error: Character must be a single character. ")
    exit()
print("Searching for " + character + " in " + word)

if word[0] == character:
    print(character + " found at index 0")
if word[1] == character:
    print(character + " found at index 1")
if word[2] == character:
    print(character + " found at index 2")
if word[3] == character:
    print(character + " found at index 3")
if word[4] == character:
    print(character + " found at index 4")

num_of_matches: int = 0
if word[0] == character:
    num_of_matches = num_of_matches + 1
if word[1] == character:
    num_of_matches = num_of_matches + 1
if word[2] == character:
    num_of_matches = num_of_matches + 1
if word[3] == character:
    num_of_matches = num_of_matches + 1
if word[4] == character:
   num_of_matches = num_of_matches + 1
if num_of_matches == 0:
    print("No instances of " + character + " found in " + word)
if num_of_matches == 1:
    print("1 instance of " + character + " found in " + word)
if num_of_matches >= 2:
    print(str(num_of_matches) + " instances of " + character + " found in " + word)
