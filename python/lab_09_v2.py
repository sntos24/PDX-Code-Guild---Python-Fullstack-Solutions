import string

letters = string.ascii_lowercase + string.ascii_lowercase


user_input = input('Please enter a letter: ').lower()
user_rotation = int(input('Please enter movement: '))
final_output = ''
n = len(user_input)

for i in range(n):
    c = user_input[i]  
    index = letters.find(c)  # find user_input in letters str
    final_rotation = index + user_rotation # take user_rotation, moving it along the string
    final_output += letters[final_rotation] # add the letters at blank str

print(final_output)


 

    
    
    


