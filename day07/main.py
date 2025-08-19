import random

word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.
word = random.choice(word_list)
print(word)

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
user_letter = input("Please choose a letter: ")
user_letter = user_letter.lower()
print(f"You chose: {user_letter}")

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
#  is, "Wrong" if it's not.

is_correct = ""
if user_letter in word:
    is_correct = "Right"
else:
    is_correct = "Wrong"
print(is_correct)
