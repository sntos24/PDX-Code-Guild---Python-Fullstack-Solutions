import random

choice = random.randint(1,10)

while True:
    player = input('Guess a number between 1 and 10: ')
    if player == choice:
        print('You guessed correctly!')
        break
    else:
        if player != choice:
            player = input('Guess again. Choose a number between 1 and 10: ')
            if player == choice:
                print('After 2 guesses, you got it right!')
                break
            else:
                if player != choice:
                    player = input('Guess again. Choose a number between 1 and 10: ')
                    if player == choice:
                        print('After 3 guesses, you got it right!')
                        break
                    else:
                        if player != choice:
                            player = input('Guess again. Choose a number between 1 and 10: ')
                            if player == choice:
                                print('After 4 guesses, you got it right!')
                                break
                            else:
                                if player != choice:
                                    player = input('Guess again. Choose a number between 1 and 10: ')
                                    if player == choice:
                                        print('After 5 guesses, you got it right!')
                                        break
                                    else:
                                        if player != choice:
                                            player = input('Guess again. Choose a number between 1 and 10: ')
                                            if player == choice:
                                                print('After 6 guesses, you got it right!')
                                                break
                                            else:
                                                if player != choice:
                                                    player = input('Guess again. Choose a number between 1 and 10: ')
                                                    if player == choice:
                                                        print('After 7 guesses, you got it right!')
                                                        break
                                                    else:
                                                        if player != choice:
                                                            player = input('Guess again. Choose a number between 1 and 10: ')
                                                            if player == choice:
                                                                print('After 8 guesses, you got it right!')
                                                                break
                                                            else:
                                                                if player != choice:
                                                                    player = input('Guess again. Choose a number between 1 and 10: ')
                                                                    if player == choice:
                                                                        print('After 9 guesses, you got it right!')
                                                                        break
                                                                    else:
                                                                        if player != choice:
                                                                            player = input('Guess again. Choose a number between 1 and 10: ')
                                                                            if player == choice:
                                                                                print('After 10 guesses, you got it right!')
                                                                                break
                                                                            else:
                                                                                print('You lose!')
                                                                                break
                                                                                                            
                                                
                                                


                                        
