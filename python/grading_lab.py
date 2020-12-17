"""
Grading Lab by Marc Santos      
"""

number = input('''Welcome to the Grade Converter thingy.
Please enter your number grade: ''')

number = int(number)

if number <= 100 and number >= 90:
    if number >= 90 and number <= 92:
        print('You got an A-! Awesome!')
    else:
        print('You got an A! Excellent job!')
elif number >= 80 and number <= 89:
    if number >= 87 and number <= 89:
        print('You got a B+! Nice!')
    elif number >= 83 and number <= 86:
        print('You got a B! Yes!')
    else:
        print('You got a B-! Still great!')
elif number >= 70 and number <= 79:
    if number >= 77 and number <= 79:
        print('You got a C+! Great!')
    elif number >= 73 and number <= 76:
        print('You got a C! Still good!')
    else:
        print('You got a C-! Try to study a little more!')
elif number >= 60 and number <= 69:
    if number >= 67 and number <= 69:
        print('You got a D+! Something wrong?!')
    elif number >= 63 and number <= 66:
        print('You got a D! Why?!')
    else:
        print('You got a D-! Uhhhhh....')
else:
    print('Yeah. You know I do not have to tell you what you got...')