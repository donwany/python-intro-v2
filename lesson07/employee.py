class Employee:
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary

    def give_raise(self, amount):
        self.salary += amount

    def display(self):
        print(f"{self.name}: ${self.salary}")

