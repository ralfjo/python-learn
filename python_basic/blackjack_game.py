import blackjack_game_art
import random

# Deal both user and computer a starting hand of 2 random card values.
# Detect when computer or user has a blackjack. (Ace + 10 value card).
# If computer gets blackjack, then the user loses (even if the user also has a blackjack). If the user gets a blackjack, then they win (unless the computer also has a blackjack).
# Calculate the user's and computer's scores based on their card values.
# If an ace is drawn, count it as 11. But if the total goes over 21, count the ace as 1 instead.
# Reveal computer's first card to the user.
# Game ends immediately when user score goes over 21 or if the user or computer gets a blackjack.
# Ask the user if they want to get another card.
# Once the user is done and no longer wants to draw any more cards, let the computer play. The computer should keep drawing cards unless their score goes over 16.
# Compare user and computer scores and see if it's a win, loss, or draw.
# Print out the player's and computer's final hand and their scores at the end of the game.
# After the game ends, ask the user if they'd like to play again. Clear the console for a fresh start.



def get_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10,10]
    return random.choice(cards)

def chage_a_card(cards):
    index = cards.index(11)
    cards[index] = 1
    return cards

def com_cards_sum():
    com_cards = []
    com_cards.append(get_card())
    com_cards.append(get_card())

    while sum(com_cards) > 21 or sum(com_cards) < 16:
        if sum(com_cards) < 16:
            com_cards.append(get_card())
        elif 11 in com_cards:
            chage_a_card(com_cards)
        else:
            break
    return com_cards    

def player_cards_sum():
    your_cards = []
    your_cards.append(get_card())
    your_cards.append(get_card())
    print(f"Your cards: {your_cards}, current score: {sum(your_cards)}")

    com_cards = com_cards_sum()
    print(f"Computer's first card: {com_cards[0]}")

    while input("Type 'y' to get another card, Type 'n' to pass: ") == "y":
        your_cards.append(get_card())
        print(f"Your cards: {your_cards}, current score: {sum(your_cards)}")
        if sum(your_cards) > 21 and 11 in your_cards:
            chage_a_card(your_cards)
        elif sum(your_cards) > 21:
            break
    
    if sum(your_cards) > 21 and 11 in your_cards:
        chage_a_card(your_cards)
    
    if sum(your_cards) > 21:
        print(f"Your card: {your_cards}, com card: {com_cards}")
        print("You Lose!")
    elif sum(your_cards) > sum(com_cards):
        print(f"Your card: {your_cards}, com card: {com_cards}")
        print("You win!")
    elif sum(com_cards) > 21:
        print(f"Your card: {your_cards}, com card: {com_cards}")
        print("You win!")
    elif sum(your_cards) == sum(com_cards):
        print(f"Your card: {your_cards}, com card: {com_cards}")
        print("Draw!")
    else:
        print(f"Your card: {your_cards}, com card: {com_cards}")
        print("You Lose!")

def play_game():
    print(blackjack_game_art.logo)

    player_cards_sum()
    
    

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    play_game()
