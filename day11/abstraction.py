#
# Abstract base class
from abc import ABC, abstractmethod
from datetime import datetime


class BankAccount(ABC):
    def __init__(self, account_number, account_holder, balance=0):
        self._account_number = account_number
        self._account_holder = account_holder
        self._balance = balance

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    def get_balance(self):
        return print(
            f"Account Holder : {self._account_holder}, Balance: ${self._balance:.2f}"
        )

        # return print(f"Account Holder : {self.account_holder}, Balance: ${self.balance:.2f}")


class SavingsAccount(BankAccount):

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            current_date_time = datetime.now()
            return print(
                f"{current_date_time} **** Deposited ${amount:.2f}. New balance: ${self._balance:.2f}"
            )
        return print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            current_date_time = datetime.now()
            return print(
                f" {current_date_time} **** Withdrew ${amount:.2f}. Remaining balance: ${self._balance:.2f}"
            )
        return print("Insufficient balance or invalid amount.")


account = SavingsAccount("1234566A", "CJ", 100)
account.deposit(200)
account.withdraw(50)
account.get_balance()
# print()
