''' Word Count Lab '''

import string
import requests

response = requests.get('http://www.gutenberg.org/files/64217/64217-0.txt')
response.encoding = 'utf-8' 
text = response.text

text = text.lower()

for char in string.punctuation:
    text = text.replace(char, '')

text = text.split()

words = {}

for word in text:
    if word not in words:
        words[word] = 1
    else:
        words[word] += 1

words = list(words.items()) # .items() returns a list of tuples

words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count

for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])