'''
Lab 15- Word Count by Marc Santos

'''

import string

with open('death_star.txt', 'r', encoding ='utf-8') as file:
    text = file.read()

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