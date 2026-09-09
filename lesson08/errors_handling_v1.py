def division(num1: int, num2: int):
    try:
        # code that might cause an exception
        result = num1 / num2
        ages = [4905, 38, 30]
        print(ages[3])
        print(result)
    except IndexError as ex:
        print(f"Index: {ex}")
    except ZeroDivisionError as ex:
        # what to do if an exception occurs
        print(f"You cannot divide by zero: {ex}")
    except (ValueError, TypeError) as ex:
        print("Some errors")
    except Exception as ex:
        print(f"Zero division error: {ex}")
    finally:
        # it will always run: mostly graceful shutdown messages
        print("Application shutting down ...")


def open_file(file_name: str):
    try:
        file = None
        file = open(file_name, "r")
        data = file.read()
        print(data)
    except FileNotFoundError as ex:
        print(f"Invalid input: {ex}")
    finally:
        if file:
            file.close()
        print("Program finished ...")


def calculate_square_root(number: int):
    if number < 0:
        raise ValueError("Number must be non-negative")
    return number ** 0.5


def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient funds")
    return balance - amount


if __name__ == '__main__':
    division(100, 0)
    division(200, 100)
    open_file("data.txt")
    print(calculate_square_root(25))
    # print(calculate_square_root(-25))

    try:
        balance = withdraw(100, 150)
        print(balance)
    except ValueError as error:
        print(f"Transaction failed: {error}")

