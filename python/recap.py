import requests
import random

response = requests.get('https://raw.githubusercontent.com/PdxCodeGuild/class_owl/master/1%20Python/data/english.txt')


words = response.text

five_or_more = []

for word in words:
    if len(word) > 5:
        five_or_more.append(word)

rand_word = random.choice(five_or_more)
