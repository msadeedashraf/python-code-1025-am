# Create a bank account class with properties and methods;


class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}"
        return "Deposit amount must be positive."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount:.2f}. Remaining balance: ${self.balance:.2f}"
        return "Insufficient balance or invalid amount."

    def get_balance(self):
        return f"Current balance: ${self.balance:.2f}"

    def display_account_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: ${self.balance}")


# Example usage
jaccount = BankAccount("123456A", "John Doe", 1)
jaccount.display_account_info()

saccount = BankAccount("123456B", "Sam", 100)
saccount.display_account_info()

aiaccount = BankAccount("123456C", "Aimee", 200)
aiaccount.display_account_info()

araccount = BankAccount("123456D", "Arash", 300)
araccount.display_account_info()

kaccount = BankAccount("123456E", "Kennedy", 400)
kaccount.display_account_info()

# print(account.deposit(200))
# print(account.withdraw(100))
# print(account.get_balance())


# Arash's Code
"""
class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
 
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")
 
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ${amount}. New balance: ${self.balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")
 
    def get_balance(self):
        return f"Current balance: ${self.balance}"
 
    def display_account_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: ${self.balance}")
 
 
# Creating an account
account = BankAccount("123456", "John Doe", 500)
 
# Displaying account info
account.display_account_info()
 
# Depositing money
account.deposit(200)
 
# Withdrawing money
account.withdraw(100)
 
# Checking balance
print(account.get_balance())
 
"""


# Sam's example
"""
class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True  # Example of an extra variable

    def deposit(self, amount):
        if not self.is_active:
            print("Account is inactive. Cannot deposit.")
            return
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance is ${self.balance:.2f}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if not self.is_active:
            print("Account is inactive. Cannot withdraw.")
            return
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ${amount:.2f}. New balance is ${self.balance:.2f}.")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        print(f"Account balance for {self.account_holder}: ${self.balance:.2f}")
        return self.balance

    def deactivate_account(self):
        self.is_active = False
        print(f"Account {self.account_number} has been deactivated.")


# Example usage
account = BankAccount("123456789", "Alice Smith", 500.0)
account.check_balance()
account.deposit(150.0)
account.withdraw(200.0)
account.deactivate_account()
account.withdraw(50.0)  # Should not work because it's deactivated
"""
