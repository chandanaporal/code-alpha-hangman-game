import random

def choose_word():
    words = ["apple", "banana", "orange", "grape", "pineapple", "watermelon"]
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6  # Number of incorrect guesses allowed

    print("Welcome to Hangman!")
    print("Try to guess the word.")
    print(display_word(word, guessed_letters))

    while True:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct!")
        else:
            attempts -= 1
            print("Incorrect guess. Attempts left:", attempts)

        print(display_word(word, guessed_letters))

        if "_" not in display_word(word, guessed_letters):
            print("Congratulations! You guessed the word:", word)
            break

        if attempts == 0:
            print("You ran out of attempts. The word was:", word)
            break

hangman()
