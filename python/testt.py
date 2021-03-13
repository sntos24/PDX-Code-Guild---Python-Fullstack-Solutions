import string
import requests


response = requests.get('http://www.gutenberg.org/files/64217/64217-0.txt')
response.encoding = 'utf-8' 
text = response.text
title = 'Title: '

for i in text:
    for title in text:
        if title == text:
            print(title)

print(text, title)