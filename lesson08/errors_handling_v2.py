# custom exceptions
class InsufficientFundsError(Exception):
    pass


def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError("Not enough money")
    return balance - amount


if __name__ == '__main__':
    try:
        balance = withdraw(100, 150)
        print(balance)
    except InsufficientFundsError as ex:
        print(f"Transaction failed: {ex}")
