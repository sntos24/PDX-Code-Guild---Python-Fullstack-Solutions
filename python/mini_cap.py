'''
Mini Capstone Project by Marc Santos 
'''
import random, requests, json, time

    


url_characters = 'https://rickandmortyapi.com/api/character'


response = requests.get(url_characters)
data = json.loads(response.text)

result = data['results']


population = []

def new_quote():
    url_random = 'https://api.whatdoestrumpthink.com/api/v1/quotes/random'
    response_2 = requests.get(url_random)
    data_2 = json.loads(response_2.text)
    quote = data_2['message']
    print(quote)


# creates a new character
class NewChar:
    def __init__(self):
        character = random.choice(result)
        self.name = character['name']
        self.status = character['status']
        self.species = character['species']
        self.gender = character['gender']
        self.location = character['location']['name']       
        self.episode = character['episode']
        self.origin = character['origin']['name']
        self.image = character['image']



# intro      
user_input = input('''Welcome to the Random Rick and Morty database!
You can learn about a handful of different chracters from the show.
If you want to continue, type yes to contine or no to quit: ''').lower()

while user_input == 'yes':
    main_menu = input('''Main Menu-----
    1. Populate New Character.
    2. Move Character into population.
    3. Learn about the Character
    4. Check population
    5. Something random
    6. 'exit' to quit
    Please enter an option: ''')

    if main_menu == '1':
        character_new = NewChar()
        print('Give me a few of seconds to populate your specimen...')
        time.sleep(2)
        print('Just a little more longer.......')
        time.sleep(2)
        print(f'''
        ***The name of your new character is {character_new.name}.
        The known status of {character_new.name} is {character_new.status}.
        {character_new.name} is a {character_new.species}.***
        ''')
    elif main_menu == '2':
        population.append(character_new.name)
        print(f'{character_new.name} has been moved to general population.')
        time.sleep(3)
    elif main_menu == '3':
        print(f'''
        ***{character_new.name} has been in a total of {len(character_new.episode)} episode/s.
        They are also from {character_new.location} but originated from {character_new.origin}.***
        ''')
        time.sleep(4)
    elif main_menu == '4':
        print('Let us see how many poor souls are in the population.')
        time.sleep(3)
        print(f'There are currently {len(population)} individuals.')
        time.sleep(3)
    elif main_menu == '5':
        answer = input('''
        Well well well, Looks like we have someone who lives life dangerously.
        If that is the case, I hope you enjoy this random quote...
        >''')
        time.sleep(2)
        new_quote()
        time.sleep(3)
        print('- Donald J. Trump.')
        time.sleep(3)
    elif main_menu == 'exit':
         print('Goodbye loser!')
         break