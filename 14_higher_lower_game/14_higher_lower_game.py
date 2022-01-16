from random import choice
from higher_lower_game_data import data
import higher_lower_art


def generate_account():
    return choice(data)


def format_account(account):
    return f"{account['name']}, a {account['description']}, from {account['country']}"


def is_correct(a_account, b_account, user_guess):
    if a_account['follower_count'] > b_account['follower_count']:
        return user_guess == "a"
    elif a_account['follower_count'] < b_account['follower_count']:
        return user_guess == "b"


def game():
    print(higher_lower_art.logo)
    score = 0
    b = generate_account()
    game_should_continue = True

    while game_should_continue:
        a = b
        b = generate_account()

        while a == b:
            b = generate_account()

        print(f"Compare A: {format_account(a)}")
        print(higher_lower_art.vs)
        print(f"Against B: {format_account(b)}")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        if is_correct(a, b, guess):
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")


game()
