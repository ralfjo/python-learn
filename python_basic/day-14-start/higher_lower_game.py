import higher_lower_game_art
import higher_lower_game_data
import random


def get_data(g_data):
    s_data = random.choice(g_data)
    return s_data

def compare(a_data, b_data):

    print(f"Compare A: {a_data['name']}, a {a_data['description']}, from {a_data['country']}")
    print(higher_lower_game_art.vs)
    print(f"Compare B: {b_data['name']}, a {b_data['description']}, from {b_data['country']}")
    select_data = input("Who has more followers? Type 'A' or 'B': ").upper()

    if select_data == "A" and a_data['follower_count'] > b_data['follower_count']:
        return True
    elif select_data == "B" and a_data['follower_count'] < b_data['follower_count']:
        return True
    else:
        return False


def game():
    print(higher_lower_game_art.logo)
    game_data = higher_lower_game_data.data
    game_score = 0
    is_right = True
    compare_a = get_data(game_data)
    game_data.remove(compare_a)

    while is_right == True:
        compare_b = get_data(game_data)
        game_data.remove(compare_b)

        is_right = compare(compare_a, compare_b)
        if is_right:
            game_score += 1
            compare_a = compare_b
            print(higher_lower_game_art.logo)
            print(f"You're right! Current score: {game_score}.")
        else:
            print(higher_lower_game_art.logo)
            print(f"Sorry, that's wrong. Final score: {game_score}.")


# 1. display art
# 2. generate a random account from the game data
# 3. format the account data into printable format
# 3. ask user for a guess
# 4. check if user is correct.
# 5. give user feedback on their guess
# 6. score keeping.
# 7. make the game repeatable.
# 8. making account at position B become the next account at position A.

game()
