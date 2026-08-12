class Employee:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def work(self):
        print(f"{self.name} is working...")


class Developer(Employee):
    def __init__(self, name, email, language):
        super().__init__(name, email)   # calls the parent class __init__() method
        self.language = language

    def write_code(self):
        print(f"{self.name} is writing python code...")


class Manager(Employee):
    def conduct_meeting(self):
        print(f"{self.name} is conducting a meeting...")


if __name__ == '__main__':
    developer = Developer("John", "john@example.com", "Python")
    manager = Manager("Mary", "mary@example.com")

    developer.work()
    developer.write_code()
    print(developer.name)
    print(developer.email)

    print("*" * 50)

    manager.work()
    manager.conduct_meeting()
    print(manager.name)
    print(manager.email)
