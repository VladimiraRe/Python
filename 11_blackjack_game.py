import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""


def get_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def game():

    print(logo)

    user_cards = []
    computer_cards = []

    for _ in range(2):
        user_cards.append(get_card())
        computer_cards.append(get_card())

    def score(list_of_card):
        """Take a list of cards and return the score calculated from the cards"""
        total = sum(list_of_card)
        if total == 21 and len(list_of_card) == 2:
            total = 0
        elif total > 21 and 11 in list_of_card:
            list_of_card.remove(11)
            list_of_card.append(1)
        return total

    def compare(user_score, computer_score):
        if user_score > 21:
            return "You went over. You lose."
        elif user_score == computer_score:
            return "It's a draw."
        elif computer_score == 0:
            return "Lose, opponent has Blackjack."
        elif user_score == 0:
            return "Win with a Blackjack!"
        elif computer_score > 21:
            return "Opponent went over. You win."
        elif user_score > computer_score:
            return "You win!"
        else:
            return "You lose."

    end_game = False
    while not end_game:
        user = score(user_cards)
        computer = score(computer_cards)
        print(f"Your cards: {user_cards}")
        print(f"Computer first card: {computer_cards[0]}")
        if computer == 0 or user == 0 or user > 21:
            end_game = True
        else:
            go_on = input("Type 'y' to get another card, type 'n' to pass: ")
            if go_on == "y":
                user_cards.append(get_card())
            else:
                end_game = True

    while computer != 0 and computer < 17:
        computer_cards.append(get_card())
        computer = score(computer_cards)

    print(f"Your final hand: {user_cards}")
    print(f"Computer's final hand: {computer_cards}")
    print(compare(user, computer))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    game()


