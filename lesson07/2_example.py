from bank import BankAccount
from employee import Employee
from cart import ShoppingCart

if __name__ == '__main__':
    # create an instance of the bank class
    account = BankAccount(owner="Donald Trump", balance=150.99)
    # deposit
    account.deposit(amount=250.00)
    # withdraw
    account.withdraw(amount=100.00)
    # check our balance
    print(account.check_balance())

    print("*" * 50)
    employee = Employee(name="Donald Trump", salary=10000.00)
    print(employee.name)
    print(employee.salary)
    employee.give_raise(amount=12.00)
    employee.display()

    print("*" * 50)
    cart = ShoppingCart()
    cart.add_items("Laptop")
    cart.add_items("Mouse")
    cart.add_items("KeyBoard")
    cart.print_cart()
    cart.remove_item("Mouse")
    cart.print_cart()