class BankAccount:
    
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


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    # other methods
    
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    	# your code here

    def make_withdraw(self, amount):
        self.account.withdraw(amount)
        return self
    
    def display_user(self):
        self.account.display_account_info()


# class User:
#     def example_method(self):
#         self.account.deposit(100)		# we can call the BankAccount instance's methods
#     print(self.account.balance)		# or access its attributes
john = User("John", "john@gmail.com" )
john.make_deposit(100).display_user()
alex = User("Alex", "Max@gmail.com" )
