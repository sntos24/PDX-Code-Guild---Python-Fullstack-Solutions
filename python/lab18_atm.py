''' ATM Lab '''


class Atm:

    def __init__(self):
        self.account_balance = 0
        self.interest = 0.001
        self.trans = []

    def balance(self): 
        return self.account_balance
    
    def deposit(self, amount):
        self.account_balance += amount
    
    
    def check_withdrawal(self, amount):
        if self.account_balance - amount < 0:
            return False
        else:
            return True
    
    def withdraw(self, amount):
        self.account_balance -= amount


    def calc_interest(self):
        interest = self.interest * self.account_balance
        interest = self.account_balance - interest
        return interest

    def print_transactions(self, amount):
        list_of_transactions = []
        trans = f'User deposited {amount}'
        list_of_transactions.append(self.trans)

        
        

atm = Atm() # create an instance of our class
print('Welcome to the ATM')
while True:

    
    command = input('Enter a command: ')
    if command == 'balance':
        balance = atm.balance() # call the balance() method
        print(f'Your balance is ${balance}')
        

    elif command == 'deposit':
        amount = float(input('How much would you like to deposit? '))
        atm.print_transactions(amount)
        atm.deposit(amount) # call the deposit(amount) method
        print(f'Deposited ${amount}')
        
    elif command == 'withdraw':
        amount = float(input('How much would you like to withdraw? '))
        if atm.check_withdrawal(amount): # call the check_withdrawal(amount) method
            atm.withdraw(amount) # call the withdraw(amount) method
            print(f'Withdrew ${amount}')
        else:
            print('Insufficient funds')
    elif command == 'interest':
        amount = atm.calc_interest() # call the calc_interest() method
        atm.deposit(amount)
        print(f'Accumulated ${amount} in interest')
    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('history - check list of transaction')
        print('exit     - exit the program')
    elif command == 'history':
        print(list_of_transactions)
    
    elif command == 'exit':
        break
    else:
        print('Command not recognized')