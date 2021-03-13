''' API Lab '''

import string
import requests


response = requests.get('http://www.gutenberg.org/files/64217/64217-0.txt')
response.encoding = 'utf-8' 
text = response.text


ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}



text = text.replace('\n', '')

title_begins = text.find('Title: ') + 7
author_begins = text.find('Author: ')
title = text[title_begins:author_begins].replace("\n", '').replace("\r", '')


def single_letters(text):
    for char in string.punctuation:
        text = text.replace(char, '') 
        text = text.replace(" ", "")
        single = list(text)
    return single
    
def words_length(text):
    for char in string.punctuation:
        text = text.replace(char, '')
        words = text.split()
    return words



def sentences_length(text):
    sentences = text.split('.')
    return sentences



ari_result = round(4.71 * (len(single_letters(text)) / len(words_length(text))) + 0.5 * (len(words_length(text)) / len(sentences_length(text))) - 21.43)


if ari_result in ari_scale:
    grade = ari_scale[ari_result]['grade_level']
    age = ari_scale[ari_result]['ages']



print(f'''
---------------------------------------------------------
The ARI for {title} is {ari_result}
This corresponds to a {grade} of difficulty
that is suitable for an average person {age} years old.    
---------------------------------------------------------
''')
