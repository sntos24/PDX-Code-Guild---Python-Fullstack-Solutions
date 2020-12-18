"""
Random Emoticon Lab by Marc Santos
"""
import random

eye = [':', '8', '=', ';']
nose = ['', '^', '-']
mouth = [')', ']', '(', '[']

v_1 = ['', '(', '[']
v_2 = ['^', '-', '*']
v_3 = ['_', '.']
v_4 = ['', ')', ']']

while True:
    print(random.choice(eye) + random.choice(nose) + random.choice(mouth)) 
    print(random.choice(v_1) + random.choice(v_2) + random.choice(v_3) + random.choice(v_2) + random.choice(v_4)) 
    print(random.choice(eye) + random.choice(nose) + random.choice(mouth)) 
    print(random.choice(v_1) + random.choice(v_2) + random.choice(v_3) + random.choice(v_2) + random.choice(v_4)) 
    print(random.choice(eye) + random.choice(nose) + random.choice(mouth)) 
    
    break
    