# method overriding - means overriding the method inside the parent-class inside the child-class

class Employee:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def work(self):
        print(f"{self.name} is working...")


class Manager(Employee):
    def conduct_meeting(self):
        print(f"{self.name} is conducting a meeting...")

    # class now uses this method instead of the one inside the parent class
    def work(self):
        print(f"{self.name} is a hard working employee")


if __name__ == '__main__':
    manager = Manager("John", "john@gmail.com")
    manager.work()
    manager.conduct_meeting()
