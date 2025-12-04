import random
import ascii_art

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    # Display the snowman stage for the current number of mistakes.
    print(ascii_art.STAGES[mistakes])
    # Build a display version of the secret word.
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)
    print("\n")


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    print("Welcome to Snowman Meltdown!")
    while True:
        display_game_state(mistakes, secret_word, guessed_letters)
        guess = input("Guess a letter: ").lower()
        if guess in secret_word:
            guessed_letters.append(guess)
            print("You guessed:", guess)
        else:
            mistakes += 1
            print()

        word_complete = True
        for letter in secret_word:
            if letter not in guessed_letters:
                word_complete = False
                break
        if word_complete:
            print("You have won!")
            break

        if mistakes == len(ascii_art.STAGES) - 1:
            print(ascii_art.STAGES[mistakes])
            print("You lost!")
            break
