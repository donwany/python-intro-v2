# encapsulation: information hiding (attributes and methods). Or restricting direct access to data.
# Access type: public (self.name) , protected (self._name), private (self.__name)
# Benefits:
# 1. Data protection 2. controlled access 3. maintainable

# without encapsulation
class BankAccount:
    def __init__(self, balance):
        self.balance = balance  # public attribute


class Account:
    def __init__(self, balance):
        self.__balance = balance  # private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance


class Employee:
    def __init__(self, name, salary):
        self.name = name  # public
        self._salary = salary  # protected


class Manager(Employee):
    def give_bonus(self, bonus):
        self._salary += bonus


if __name__ == '__main__':
    account = BankAccount(balance=1000)
    print(account.balance)  # 1000
    # modify the balance: anyone can modify it directly
    account.balance = -500
    print(account.balance)

    print("*" * 100)
    acct = Account(balance=250)
    acct.deposit(500)
    acct.withdraw(300)
    print(acct.get_balance())
    acct._Account__balance = -500
    print(acct._Account__balance)
    print(acct.__dict__)

    print("*" * 100)
    manager = Manager("John", 5000)
    manager.give_bonus(5000)
    manager._salary = 50
    print(manager._salary)
    print(manager.__dict__)
