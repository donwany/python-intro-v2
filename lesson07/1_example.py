# from student import Student
# from bank import BankAccount
# from employee import Employee
# from ensemble import *
from ensemble import BankAccount, Employee, Student, add

if __name__ == '__main__':
    student1 = Student("Alice", 30, "Math", "A")
    student2 = Student("Joh", 99, "Computer", "B")

    print(type(student1))
    print(student1)
    print(student1.name)
    print(student1.age)
    print(student1.major)
    print(student1.grade)

    # calling the method inside the class
    print(student1.introduce())
    print("*" * 50)
    print(Student("Joh", 99, "Computer", "B").introduce())

    print(f"The sum is: {add(48, 54)}")


