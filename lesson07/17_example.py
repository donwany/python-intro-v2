# static methods: is a method that belongs toa class but does not need access to the objects data

# class Calculator:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def add(self):
#         return self.a + self.b

class Calculator:
    @staticmethod
    def add(a, b):
        return a + b


class Temperature:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9 / 5) + 32


class Student:
    @staticmethod
    def is_valid_age(age):
        return age >= 18


if __name__ == '__main__':
    # calc = Calculator(50, 40)
    # print(calc.add())     # object.method()

    calc = Calculator()
    print(calc.add(50, 40))

    result = Calculator.add(50, 40)
    print(result)

    fah = Temperature.celsius_to_fahrenheit(celsius=25)
    print(fah)

    print(Student.is_valid_age(20))     # class.method()
