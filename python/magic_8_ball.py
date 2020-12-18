"""
Magic 8 Ball by Marc Santos 
"""
import random

answers = ['yes', 'no', 'yeah, no', 'maybe', 'sure!', 'do not bet on it']



while True:
    question = input('Please enter in your question or type \'done\' to exit: ')
    
    if question == 'done':
        break
    else:
        print(random.choice(answers))
    