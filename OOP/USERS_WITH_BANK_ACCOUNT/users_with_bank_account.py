class BankAccount:
    bank_name = "SouthWest National Bank"

    def __init__ (self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self

    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient funds: Charging a $5 fee")
            self.balance = (self.balance - amount - 5)
            return self
        else:
            self.balance = self.balance - amount
            return self

    def display_account_info(self):
        print(f"Balance: $ {self.balance}")
        return self

Checkings = BankAccount(.1,0)
Savings = BankAccount(.1,0)

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(.1,0)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        print(self.account.balance)
        return self

    def make_withdraw(self, amount):
        self.account.withdraw(amount)
        print(self.account.balance)
        return self

    def display_user_balance(self):
        self.account.display_account_info()
        print(self.account.balance)
        return self

Kiwi = User("Kiwi", "berry@msn.com")

Kiwi.make_deposit(25)
Kiwi.make_withdraw(10)
Kiwi.display_user_balance()

