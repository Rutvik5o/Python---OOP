import sys

class Bank:

    def __init__(self, name, balance=0.0):

        self.name = name

        self.balance = balance

    def deposit(self, amount):

        self.balance += amount

        return self.balance

    def withdrawals(self, amount):

        if amount > self.balance:
            print("Low balance!! , cannot withdraw")    

        else:
            self.balance -= amount

        return self.balance

name = input('Enter Name=> ')

b = Bank(name)

while True:
    print("\nFor Deposit: d/D \nFor Withdrawal: w/W \nFor Exit: e/E")

    choice = input("Enter your choice-> ")

    if choice == 'e' or choice == 'E':

        sys.exit()

    elif choice == 'D' or choice == 'd':
        
        amount = float(input("Enter amount-> "))

        print("Balance after deposit: ", b.deposit(amount))

    elif choice == 'w' or choice == 'W':

        amount = float(input("Enter amount-> "))

        print("Balance after withdrawal: ", b.withdrawals(amount))
