'''
Unit Converter Lab by Marc Santos
'''


units = {
    'ft': 0.3048,
    'mi': 1609.34,
    'm': 1,
    'km': 1000,
    'yard': 0.9144,
    'in': 0.0254


}

user_input = input('Please enter the distance to be converted: ')
user_input = int(user_input)

starting_unit = input('Please enter the starting unit(ex. foot = ft, mile = mi): ')
final_unit = input('Please enter the final unit(ex. foot = ft, mile = mi): ')


conversion_meters = units[f'{starting_unit}'] * user_input # Converting starting unit into meters
conversion_meters = conversion_meters / units[f'{final_unit}'] # Converting meters into final unit

print(f'{user_input} {starting_unit} is {conversion_meters} {final_unit}!')