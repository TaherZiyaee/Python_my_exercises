from random import randrange


class BankAccount:
    """
    Bank Account class with fields and methods.
    """
    all_account_numbers = list()
    last_account_number=10000

    def __init__(self, name: str) -> None:
        BankAccount.last_account_number+=1
        BankAccount.all_account_numbers.append(BankAccount.last_account_number)
        self.name: str = name
        self.balance: float = 0
        self.acc_number: int = BankAccount.last_account_number
        # while self.acc_number == 0:
        #     if (an := randrange(10000, 100000)) is not BankAccount.all_account_numbers:
        #         BankAccount.all_account_numbers.append(an)
        #         self.acc_number = an

    def display(self) -> None:
        print(f"Name: {self.name}\nBalance: {self.balance} T\nAccount Number: {self.acc_number}")
        print('-' * 20)

    def balance_display(self) -> None:
        print(f"Hi {self.name}\nYour balance is {self.balance}")
        print('-' * 20)

    def deposit(self) -> None:
        """
        Deposit to balance value.
        """
        amount = float(input("Please enter amount to deposit: "))
        self.balance += amount
        self.balance_display()

    def withdraw(self) -> None:
        """
        Withdraw from balance value.
        """
        amount = float(input("Please enter amount to withdraw: "))
        if amount > self.balance:
            print("Your balance is not enough!")
        else:
            self.balance -= amount
        self.balance_display()


def main() -> None:
    acc1 = BankAccount("Taher Ziayee")
    acc1.deposit()
    acc1.withdraw()
    acc2 = BankAccount("Noyan Ziayee")
    acc2.balance = 10000000
    acc1.display()
    acc2.display()
    print(BankAccount.all_account_numbers)
    # print(help(BankAccount))


if __name__ == "__main__":
    main()
