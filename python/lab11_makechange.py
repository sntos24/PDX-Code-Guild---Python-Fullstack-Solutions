''' Make Change Lab '''

coins = [
    ('half_dollar', 50),
    ('quarter', 25),
    ('dime', 10),
    ('nickel', 5),
    ('pennies', 1)
]



coin_actual = []

coin_amount = input("Please enter in your dollar amount:  ")
coin_amount = float(coin_amount)


coin_amount *= 100


coin_amount = int(coin_amount)



for coin in coins:
    name = coin[0]
    value = coin[1]
    quantity = (name, coin_amount // value)
    coin_amount -= value * quantity[1]
    coin_actual.append(quantity)



for coin in coin_actual:
    print(f"{coin[0]}: {coin[1]}")