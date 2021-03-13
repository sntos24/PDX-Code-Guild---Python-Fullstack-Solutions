import string

letters = string.ascii_lowercase + string.ascii_lowercase


user_input = input('Please enter a letter: ').lower()

user_rotation_input = int(input('Enter in the amount for rotations: '))

processed_outcome = ''

entry = len(user_input)



for i in range(entry):
        value = user_input[i]  
        index = letters.find(value)  
        final_rotation = index + user_rotation_input 
        processed_outcome += letters[final_rotation] 
        
        
print(processed_outcome)
        


 

    
    
    


