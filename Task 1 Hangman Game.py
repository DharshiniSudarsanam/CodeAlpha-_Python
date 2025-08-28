import random

def hangman():
    # Predefined list of words
    words = ["python", "code", "alpha", "task", "hangman"]
    word = random.choice(words)  # Randomly choose a word
    guessed = ["_"] * len(word)  # Underscore for each letter
    attempts = 6
    guessed_letters = []

    print("Welcome to Hangman Game!")
    print("Word to guess:", " ".join(guessed))

    while attempts > 0 and "_" in guessed:
        guess = input("\nEnter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabet.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed[i] = guess
        else:
            attempts -= 1
            print(f"Wrong guess! '{guess}' is not in the word.")
            print(f"Attempts left: {attempts}")

        print("Word to guess:", " ".join(guessed))

    if "_" not in guessed:
        print("\n🎉 Congratulations! You guessed the word:", word)
    else:
        print("\n❌ Out of attempts! The word was:", word)

# Run the game
hangman()
