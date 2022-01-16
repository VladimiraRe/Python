import random
from hangman_art import logo, stages
from hangman_words import word_list

print(logo)

life = len(stages) - 2
chosen_word = random.choice(word_list)

display = []
for i in range(len(chosen_word)):
    display += "_"

while "_" in display:
    if life < 0:
        print("You lose")
        break
    else:
        guess = input("Guess a letter: ").lower()
        if guess in chosen_word:
            if guess in display:
                print(f"You've already guessed {guess}.")
                print(" ".join(display))
            else:
                for i in range(len(chosen_word)):
                    if chosen_word[i] == guess:
                        display[i] = guess
                print(" ".join(display))
        else:
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            print(" ".join(display))
            print(stages[life])
            life -= 1
if "_" not in display:
    print("You win!")




