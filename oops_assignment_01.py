"""
Concept: Classes and Objects
Q1.Create a class BankAccount with attributes:account_number, owner_name,balance
Add methods to:deposit,withdraw,check_balance
"""
class BankAccount:
    def __init__(self,account_number, owner_name,balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance
    # for deposit
    def deposit(self,amount):
        if (amount <= 0):
            print("Insufficient funds...")
        else:
            self.balance += amount
            print(self.balance)
            print(f"The New Balance is = {self.balance}")
    # for withdraw
    def withdraw(self,amount):
        if (amount <= 0):
            print("Insufficient funds...")
        elif (amount > self.balance):
            print("Insufficient funds...")
        else:
            self.balance -= amount
            print(self.balance)
              
    def show_balance(self):
        print(f"Balance = {self.balance}")
acc1 = BankAccount(999,"Prakash",400_000)
print(acc1.account_number,acc1.owner_name,acc1.balance)
acc1.show_balance()
acc2 = BankAccount(666,"Shankar",900_000)
acc2.show_balance()
print(acc2.account_number,acc2.owner_name,acc2.balance)
acc1.deposit(50_000)
acc1.show_balance()
acc1.withdraw(500000)