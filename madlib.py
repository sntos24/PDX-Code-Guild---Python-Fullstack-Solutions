"""
Mad Lib Lab by Marc Santos
"""

welcome = input('Welcome to the Mad Lib Lab. Please enter your name: ')
location = input('Where is somewhere you never have been too?: ')
year = input('Please enter the year you were born: ')
sibling = input('Who is your favorite sibling?: ')

final = (f"""Welcome to the program, Captian {welcome}! We have to relocate to 
{location} and recruit all individuals that were born in {year} and named {sibling}!
I know this does not make sense, and that is the point!
""")

print(final)