def division(a, b):
    try:
        if b != 0:
            return a / b
    except ZeroDivisionError as e:
        print(f"Cannot divide by zero: {e}")
    finally:
        print("Thanks for using this application!!!")
        print("Goodbye")


if __name__ == '__main__':

    # results = division(10, 0)
    # print(f"results: {results}")

    try:
        # str(7) = str("abcd")
        print(10 + '10')
    except SyntaxError as e:
        print(f"syntax error: {e}")
    except TypeError as e:
        print(f"an error occurred: {e}")


    # try:
    #     print(division(10, 2))
    # except ZeroDivisionError as e:
    #     print(f"You are dividing zero with another number: {e}")
    # except ArithmeticError as e:
    #     print(f"Arithmetic error occurred: {e}")
    # except Exception as e:
    #     print(f"Cannot divide by zero: {e}")
    # finally:
    #     print("Thanks for using this application!!!")
    #     print("Goodbye")
