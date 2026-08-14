# method overloading: multiple methods with the same name but different parameters
# Does python support method overloading? Answer: Python does not support traditional
# method overloading like Java, C++.
# If you have multiple methods having the same name, the last one overrides the previous one.

class Calculator:
    def add(self, a: int, b: int) -> int:
        return a + b

    def add(self, a: int, b: int, c: int) -> int:
        return a + b + c


if __name__ == '__main__':
    calc = Calculator()
    # print(calc.add(2, 5))  # 7
    print(calc.add(2, 5, 10))   # 17