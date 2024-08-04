#Hang Man Game
import random

# List of words
words = [
    "apple", "bread", "chair", "house", "juice", "light", "mouse", "pen", "tree", "water",
    "bicycle", "castle", "elephant", "giraffe", "garden", "puzzle", "rocket", "soccer", 
    "telephone", "umbrella", "acoustic", "bizarre", "compass", "dinosaur", "exercise", 
    "horizon", "juxtapose", "kaleidoscope", "mysterious", "obstacle"
]
hangman_stages = [
    """
     ------
     |    |
          |
          |
          |
          |
    """,
    """
     ------
     |    |
     O    |
          |
          |
          |
    """,
    """
     ------
     |    |
     O    |
     |    |
          |
          |
    """,
    """
     ------
     |    |
     O    |
    /|    |
          |
          |
    """,
    """
     ------
     |    |
     O    |
    /|\\   |
          |
          |
    """,
    """
     ------
     |    |
     O    |
    /|\\   |
    /     |
          |
    """,
    """
     ------
     |    |
     O    |
    /|\\   |
    / \\   |
    """,
]


# Select a random word from the list
key = random.choice(words)
word_length = len(key)
guessed_letters = set()
attempts_left = 6

# Display initial game state
print("Guess the Word: You have 6 Chances")
print("_ " * word_length)

# Function to display the current state of the word
def display_word():
    # Initialize the display list
display = []

# Iterate over each letter in the key (word)
for letter in key:
    # If the letter has been guessed, add it to the display list
    if letter in guessed_letters:
        display.append(letter)
    # Otherwise, add an underscore to the display list
    else:
        display.append('_')

# Convert the list to a string and print it
    print(" ".join(display))

# Game loop
while attempts_left > 0:
    userguess = input("Guess a letter: ").lower()
    
    # Check if the input is a single letter
    if len(userguess) != 1 or not userguess.isalpha():
        print("Please enter a single letter.")
        continue
    
    # Check if the letter has been guessed before
    if userguess in guessed_letters:
        print("You've already guessed that letter.")
        continue
    
    # Add the guessed letter to the set of guessed letters
    guessed_letters.add(userguess)
    
    # Check if the guessed letter is in the word
    if userguess in key:
        print("Safe")
        display_word()
    else:
        attempts_left -= 1
        print(f"Wrong guess. You have {attempts_left} chances left.")
        print(hangman_stages[6-attempts_left])
    
    # Check if the user has guessed all letters
    if all(letter in guessed_letters for letter in key):
        print("Congratulations! You've guessed the word.")
        break
else:
    print(f"Game Over! The word was '{key}'.")