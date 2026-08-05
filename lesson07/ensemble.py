class Employee:
    pass


class BankAccount:
    pass


class Student:
    def __init__(self, name: str, age: int, major: str, grade: str):
        self.name = name
        self.age = age
        self.major = major
        self.grade = grade

    def introduce(self):
        print("Im going to introduce myself")
        print(f"My name is {self.name}")
        print(f"I study {self.major}")
        print(f"My age increased today: {self.age + 10}")

    def write(self):
        pass

    def read(self):
        pass


def add(a: int, b):
    return a + b
