import random

rock = 'rock'
paper = 'paper'
scissors = 'scissors'



computer_choice = ['rock', 'paper', 'scissors']
computer_choice = random.choice(computer_choice)

player_choice = input('Please enter your choice: ')

# Outcome 
if player_choice == computer_choice:
    print('Looks like it was a tie!')
elif player_choice == 'rock' and computer_choice == 'paper':
    print('You chose rock! Computer chose paper. You win!')
elif player_choice == 'rock' and computer_choice == 'scissors':
    print('You chose rock! Computer chose scissors. You lose!')
elif player_choice == 'paper' and computer_choice == 'scissors':
    print('You chose paper! Computer chose scissors. You lose!')
elif player_choice == 'paper' and computer_choice == 'rock':
    print('You chose paper! Computer chose rock. You win!')
elif player_choice == 'scissors' and computer_choice == 'paper':
    print('You chose scissors! Computer chose paper. You win!')
elif player_choice == 'scissors' and computer_choice == 'rock':
    print('You chose scissors! Computer chose rock. You win!')


