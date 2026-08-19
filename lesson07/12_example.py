# Method chaining:
# tavily = TavilyClient()
# tavily.search()

# without method chaining
class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            print("Cannot deposit negative amounts")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def check_balance(self):
        print(f"Your current balance is: ${self.balance}")


# with method chaining
class Account:
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            print("Cannot deposit negative amounts")
        self.balance += amount
        return self  # goes with method chaining

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")
        return self  # goes with method chaining

    def check_balance(self):
        print(f"Your current balance is: ${self.balance}")


if __name__ == '__main__':
    account = BankAccount("George", 350.00)
    account.deposit(50)
    account.deposit(100)
    account.withdraw(35)
    account.check_balance()

    print("*" * 100)
    acct = Account("John", 350.00)
    acct.deposit(50).deposit(100).withdraw(35).check_balance()
