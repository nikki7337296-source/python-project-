import random

# List of words
words = ["python", "computer", "keyboard",
         "programming", "monitor", "internet"]

# Select random word
word = random.choice(words)

# Shuffle letters
letters = list(word)
random.shuffle(letters)

# Convert list to string
scrambled_word = ''.join(letters)

print("Unscramble the word:")
print(scrambled_word)

# User guess
guess = input("Enter your guess: ")

# Check answer
if guess.lower() == word:
    print("Correct! 🎉")
else:
    print("Wrong answer!")
    print("The correct word was:", word)