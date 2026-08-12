# Class variables and Instance variables
# Instance variables they belong to an individual object and are usually created with self.
# Class variables belongs to the class itself and is shared by all instances

class Student:
    # class variable
    school = "Dallas High School"
    school_district = "Collin"

    def __init__(self, name, age):
        # instance variables
        self.name = name
        self.age = age


if __name__ == '__main__':
    student1 = Student("John", 40)
    student2 = Student("Mary", 25)
    print(student1.name)
    print(student2.name)
    print(student1.school)
    print(student2.school)
    print(Student.school)

    student1.name = "George"
    # avoid this
    # student1.school = "Richardson Elementary School"
    # do this instead
    Student.school = "Richardson Elementary School"
    print("*" * 50)
    print(student1.name)
    print(student2.name)
    print(Student.school)
