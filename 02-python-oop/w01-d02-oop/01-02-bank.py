class BankAccount:
    all_BankAccount = []
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
        self.int_rate = int_rate
        self.balance = balance
        
    def deposit(self, amount):
        # your code here
        self.balance+=amount
        return self
    def withdraw(self, amount):
        self.balance-=amount
        if (self.balance) <5:
            print("Insufficient funds: Charging a $5 fee")
        return self
        # your code here
    def display_account_info(self):
        print(f"this new balance : {self.balance}")

        # your code here
    def yield_interest(self):
        self.balance += self.balance*self.int_rate
        return self
        # your code here


john = BankAccount(0.01, 100 )
alex = BankAccount(0.01,100)
john.deposit(10).deposit(10).deposit(10).withdraw(5).yield_interest().display_account_info()
alex.deposit(10).deposit(10).withdraw(5).withdraw(5).withdraw(5).withdraw(5).yield_interest().display_account_info()

print(BankAccount.all_BankAccount)