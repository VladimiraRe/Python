import random

logo = """
 _______                                
|     __|.--.--.-----.-----.-----.      
|    |  ||  |  |  -__|__ --|__ --|      
|_______||_____|_____|_____|_____|      

     __   __                            
    |  |_|  |--.-----.                  
    |   _|     |  -__|                  
    |____|__|__|_____|                  

                       __               
.-----.--.--.--------.|  |--.-----.----.
|     |  |  |        ||  _  |  -__|   _|
|__|__|_____|__|__|__||_____|_____|__|  
"""

EASY_LVL = 10
HARD_LVL = 5


def level():
    lvl = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if lvl == "easy":
        return EASY_LVL
    elif lvl == "hard":
        return HARD_LVL
    else:
        raise NameError("Wrong answer.")


def compare(user_number, comp_number, t):
    """Checks answer against guess. Returns the number of turns remaining."""
    if user_number > comp_number:
        print("Too high.")
        return t - 1
    elif user_number < comp_number:
        print("Too low.")
        return t - 1
    else:
        print(f"You got it! The answer was {comp_number}.")


def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    computer = random.randint(1, 100)
    turns = level()
    user = 0
    while user != computer:
        print(f"You have {turns} attempts remaining to guess the number")
        user = int(input("Make a guess: "))
        turns = compare(user, computer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif user != computer:
            print("Guess again.")


game()
