# Parent Class
from datetime import datetime


class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            current_date_time = datetime.now()
            return print(
                f"{current_date_time} **** Deposited ${amount:.2f}. New balance: ${self.balance:.2f}"
            )
        return print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            current_date_time = datetime.now()
            return print(
                f" {current_date_time} **** Withdrew ${amount:.2f}. Remaining balance: ${self.balance:.2f}"
            )
        return print("Insufficient balance or invalid amount.")

    def get_balance(self):
        return print(f"Current balance: ${self.balance:.2f}")

    def display_account_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: ${self.balance}")


class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0.0, interest_rate=0.02):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest added : ${interest}. New Balance : ${self.balance}")


class CheckingAccount(BankAccount):
    def __init__(
        self, account_number, account_holder, balance=0.0, over_draft_limit=100
    ):
        super().__init__(account_number, account_holder, balance)
        self.over_draft_limit = over_draft_limit

    def withdraw(self, amount):
        if amount > self.balance + self.over_draft_limit:
            print("Overdraft limit exceeded.")
        else:
            self.balance -= amount
            print(f"Withdrawn Amount : ${amount}. New Balance : ${self.balance}")


# Usage
s = SavingsAccount("123456789A", "Arash", 500)
s.deposit(1000)
s.get_balance()
s.add_interest()

print("*****Account Statement*********")
s.display_account_info()


samAccoutn = SavingsAccount("123456789A", "Sam", 100)
samAccoutn.deposit(900)
samAccoutn.deposit(500)
samAccoutn.deposit(400)
samAccoutn.withdraw(500)
samAccoutn.deposit(100)
samAccoutn.get_balance()
samAccoutn.add_interest()

print("*****Account Statement*********")
samAccoutn.display_account_info()
print("*****Account Statement Ends*********")


kAccount = CheckingAccount("123456789B", "Kennedy", 400, 200)
kAccount.get_balance()
kAccount.deposit(600)
kAccount.withdraw(1200)
kAccount.withdraw(10)
kAccount.get_balance()

print("*****Account Statement*********")
kAccount.display_account_info()
