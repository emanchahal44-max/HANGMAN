
def display_word(word, guessed_letters):
    """Display the word with underscores for unguessed letters."""
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    print("\nWord:", display.strip())


def display_welcome():
    print("Welcome to Hangman!")
    print("------------------")


def display_result(word, won):
    if won:
        print(f"🎉 Congratulations! You guessed the word: {word.upper()}")
    else:
        print(f"💀 Game over! The word was: {word.upper()}")