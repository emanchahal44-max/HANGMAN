import random
from game.wordlist import choose_word
from ui.display import display_word

def play_game():
    categories = ["animals", "fruits", "english", "science"]
    category = input(f"Categories: {', '.join(categories)}\nChoose a category (or leave empty for random): ").strip().lower()
    if not category or category not in categories:
        category = random.choice(categories)

    word = choose_word(category)
    word_lower = word.lower()
    display = ["_" if ch.isalpha() else ch for ch in word_lower]

    guessed = []
    wrong_guesses = []
    remaining_attempts = 6
    points = 0

    print(f"\nWord: {' '.join(display)}")
    print("Guessed letters:")
    print(f"Remaining wrong guesses: {remaining_attempts}\n")

    guesses_log = []

    while remaining_attempts > 0 and "_" in display:
        guess = input("Enter your guess (single, multiple, or full word): ").strip().lower()

        if not guess:
            print(" Please enter a guess.\n")
            continue

        if guess in guessed:
            print("You already guessed that sequence.")
            continue

        guessed.append(guess)

        # --- FULL WORD GUESS ---
        if guess == word_lower:
            display = list(word_lower)
            points += 100
            guesses_log.append((guess, "Full word correct!"))
            print("\n You guessed the full word correctly!")
            break

        # --- MULTIPLE LETTERS (like le, pla, etc.) ---
        elif len(guess) > 1:
            found = False
            for i in range(len(word_lower) - len(guess) + 1):
                segment = word_lower[i:i+len(guess)]
                if segment == guess:
                    display[i:i+len(guess)] = list(guess)
                    found = True
            if found:
                print("\n Some letters matched!")
                guesses_log.append((guess, "Some letters matched"))
                points += 20
            else:
                remaining_attempts -= 1
                wrong_guesses.append(guess)
                guesses_log.append((guess, "Wrong"))
                print(f" Wrong guess! Remaining attempts: {remaining_attempts}")
            print()
        
        # --- SINGLE LETTER GUESS ---
        else:
            if guess in word_lower:
                for i, ch in enumerate(word_lower):
                    if ch == guess:
                        display[i] = guess
                print("\n Correct sequence found!")
                guesses_log.append((guess, "Correct"))
                points += 10
            else:
                remaining_attempts -= 1
                wrong_guesses.append(guess)
                guesses_log.append((guess, "Wrong"))
                print(f" Wrong guess! Remaining attempts: {remaining_attempts}")
            print()

        # --- Update display ---
        print(f"Word: {' '.join(display)}")
        print(f"Guessed so far: {', '.join(guessed)}")
        print(f"Remaining wrong guesses: {remaining_attempts}\n")

    # --- Final Result ---
    won = "_" not in display
    if won:
        print(f"\n You win! The word was: {word}")
        points += 50
    else:
        print(f"\n You lost! The word was: {word}")

    print(f"Points earned this round: {points}\n")


    return {
        "category": category,
        "word": word,
        "won": won,
        "points": points,
        "guesses": guesses_log,
        "wrong_guesses": wrong_guesses,
        "remaining_attempts": remaining_attempts
    }




