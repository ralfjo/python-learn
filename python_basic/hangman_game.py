import random
from hangman_arts import stages
from hangman_words import word_list

# TODO-1
chosen_word = random.choice(word_list)
print(chosen_word)
lives = 6

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()

    # TODO-2

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
        
    print(display)

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You Lose.")

    if "_" not in display:
        game_over = True
        print("You win.")

    print(stages[lives])
