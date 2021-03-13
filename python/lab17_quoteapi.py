
''' API Quote Lab '''

import random
import requests
import json


page = 1
keyword = input("Please enter a word to search quotes for: ")

def get_quotes(page):
    url = f'https://favqs.com/api/quotes?page={page}&filter={keyword}'

    headers = {'Authorization': 'Token token="7eb2d1a865d8de74b7024b7d0f51c458"'}

    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    quotes = data['quotes']
    for quote in quotes:
        print(quote['body'])
        print(f"\t--{quote['author']}")

    return text

text = get_quotes(page)

while not(data['last_page']):
    next = input("Do you want to see the next page of results? ").lower()
    if next in ["yes", "yeah", "y", "next"]:
        page += 1
        data = get_quotes(page)
    else:
        break