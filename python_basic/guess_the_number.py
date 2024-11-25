import guess_the_number_art
from random import randint

EASY_LEVEL_TRUNS = 10
HARD_LEVEL_TRUNS = 5

def check_answer(user_guess, actual_answer, turns):
    """Checks answer against guess, returns the number of turns remaining."""
    if user_guess > actual_answer:
        print("Too high.")
        return turns-1
    elif user_guess < actual_answer:
        print("Too low.")
        return turns-1
    else:
        print(f"You got it! The answer was {actual_answer}.")

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TRUNS
    else:
        return HARD_LEVEL_TRUNS

def game():   
    print(guess_the_number_art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    # level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    number = randint(1, 100)

    # if level == 'hard':
    #     attempt_number = 5
    # else:
    #     attempt_number = 10

    turns = set_difficulty()
    
    guess = 0
    while guess != number:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, number, turns)
        if turns == 0:
            print("You've run out of guesses. you lose!")
            return
        elif guess != number:
            print("Guess again.")


    # while attempt_number != 0:
    #     print(f"You have {attempt_number} attempts remaining to guess the number.")
    #     guess_number = int(input("Make a guess: "))

    #     if guess_number == number:
    #         print(f"You got it! The answer was {number}.")
    #         break
    #     elif guess_number > number:
    #         print("Too high.")
    #     elif guess_number < number:
    #         print("Too low.")

    #     attempt_number = attempt_number - 1

    # if attempt_number == 0:
    #     print("You've run out of guesses. Refresh the page to run again.")
    # else:
    #     print("Guess again.")

game()