import random

# List of predefined words
words = ["python", "apple", "coding", "laptop","apoorva", "hangman"]

# Randomly choose a word
chosen_word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Number of wrong attempts allowed
attempts = 6

print("Welcome to Hangman Game!")
print("Guess the word one letter at a time.")

# Main game loop
while attempts > 0:

    # Display the word with blanks
    display_word = ""

    for letter in chosen_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check if player guessed the full word
    if "_" not in display_word:
        print("🎉 Congratulations! You guessed the word correctly.")
        break

    # Take user input
    guess = input("Enter a letter: ").lower()

    # Check input validity
    if len(guess) != 1 or not guess.isalpha():
        print("⚠ Please enter only one alphabet.")
        continue

    # Check repeated guesses
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    # Add guess to guessed letters
    guessed_letters.append(guess)

    # Correct or wrong guess
    if guess in chosen_word:
        print("✅ Correct Guess!")
    else:
        attempts -= 1
        print("❌ Wrong Guess!")
        print("Attempts left:", attempts)

# If attempts become 0
if attempts == 0:
    print("\n💀 You lost!")
    print("The word was:", chosen_word)