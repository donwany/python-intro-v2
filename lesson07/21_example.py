# Magic (Dunder) methods
# __init__, __str__, __len__, __add__, __eq__, __lt__, __gt__, __ne__,__repr__, __call__

class Student:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        return f"Student(name={self.name}, age={self.age})"

    def __repr__(self):
        return f"Student(name={self.name}, age={self.age})"

    def show_student_info(self):
        print("Student information ...")


class Greeter:
    def __call__(self, name):
        return f"Hello, {name}"


if __name__ == '__main__':
    student1 = Student("John", 99)
    print(student1.__dict__)
    # student1("John", 99) # not callable object

    student2 = Student("John", 99)
    print(student1 == student2)

    print(student1)
    print(student1.name)
    student1.show_student_info()

    greeter = Greeter()
    print(greeter(name="Harrison"))     # __call__ makes an object callable

