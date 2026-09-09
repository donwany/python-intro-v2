

if __name__ == '__main__':
    try:
        age = int(input("enter your age: "))
        print(f"you will be {age + 5} in 5 years.")
    except ValueError as e:
        print("Invalid input!, Please enter a number")
    finally:
        print("Thank you for using our app!")
