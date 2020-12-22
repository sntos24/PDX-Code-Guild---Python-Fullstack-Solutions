import random

choice = random.randint(1,10)

while True:
    player = input('Guess a number between 1 and 10: ')
    if player == choice:
        print('You guessed correctly!')
        break
    else:
        False
        print('Guess again!')

