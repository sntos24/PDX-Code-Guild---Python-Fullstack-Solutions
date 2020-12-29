'''
Lab 12: Blackjack Advice by Marc Santos
'''

cards = {
    'A': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'J': 10,
    'Q': 10,
    'K': 10
}

card_one = input('What is your first card?: ')   
card_two = input('What is your second card?: ')    
card_three = input('What is your first card?: ')  

card_total = cards[card_one] + cards[card_two] + cards[card_three]

if card_total < 17:
    print(f'{card_total}. Hit!')
elif card_total >= 17 and card_total < 21:
    print(f'{card_total}. Stay!')
elif card_total == 21:
    print(f'{card_total}. BLACKJACK!')
else:
    print('Already busted!')
    
    