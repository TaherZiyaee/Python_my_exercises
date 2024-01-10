from colorama import Fore
from random import randrange


class BankAccount:
    all_account_numbers = set()

    def __init__(self, name):
        while True:
            if (an := randrange(1000, 100000)) not in BankAccount.all_account_numbers:
                BankAccount.all_account_numbers.add(an)
                self.account_number = an
                break
        self.name = name
        self.account_number = 0
        self.balance = 0

    def display(self):
        print('*' * star)
        print(f"\tHi {self.name}\n\tYour current balance: {self.balance} IRT")

    def deposit(self):
        amount = float(input("\tPlease anter amount to deposite: "))
        self.balance += amount
        self.display()

    def withdraw(self):
        amount = float(input("\tPlease anter amount to withdraw: "))
        if amount > self.balance:
            print(Fore.RED,"\tInsufficient balance!",Fore.RESET)
        else:
            self.balance -= amount
        self.display()


# -------- Main --------
star = 70
print('=' * star)
ali = BankAccount("Ali")
ali.balance=70000
# ali.deposit()
ali.withdraw()

print('=' * star)
