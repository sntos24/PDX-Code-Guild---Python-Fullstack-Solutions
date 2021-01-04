'''
Password Generator by Marc Santos
'''

import random
import string

characters = string.ascii_lowercase + string.ascii_uppercase + string.digits # Pulls all the possible options for characters

user_input = input('Please enter the length of the password: ') 
user_input = int(user_input)

password = ''
x = 0

while x < user_input:
    x += 1
    password += random.choice(characters)

print(f'Your random password is: {password}')
