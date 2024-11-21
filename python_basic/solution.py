import random

word_list = ["aardvark", "baboon", "camel"]

# TODO-1
chosen_word = random.choice(word_list)
print(chosen_word)

# TODO-2
guess = input("Guess a letter: ").lower()
print(guess)

# TODO-3
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")