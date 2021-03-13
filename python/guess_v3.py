''' Guess the Number Lab '''

import random

while True:
    guesses = 1
    player_choice = random.randint(1, 10)
    player = None
    while user != player_choice:

        user = input("Pick a number between 1-10: ")


        if user < player_choice:
            guesses += 1
            print("Too low, try again.")
        else:
            guesses += 1
            print("Too high, guess again")
    else:
        print("You guessed correctly!")
        print(f"It took you {guesses} tries!")

        play_again = input("Would you like to play again? ").lower()
        valid_choices = ['y', 'yes']
        if play_again not in valid_choices:
            break 
        