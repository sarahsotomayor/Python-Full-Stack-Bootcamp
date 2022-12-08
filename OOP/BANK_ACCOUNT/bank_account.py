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

    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance + (self.balance * self.int_rate)
        return self

Checkings = BankAccount(.1,0)
Savings = BankAccount(.5,0)

Checkings.deposit(100).deposit(500).deposit(200).withdraw(50).yield_interest().display_account_info()

Savings.deposit(500).deposit(500).withdraw(300).withdraw(300).withdraw(300).withdraw(300).yield_interest().display_account_info()