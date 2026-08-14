# @properties - it's a decorator

# without @property
class Student:
    def __init__(self, name):
        self.name = name


# with @property
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

    def perimeter(self):
        ...


if __name__ == '__main__':
    student = Student(name="Trump")
    print(student.name)  # property or attribute

    rect = Rectangle(5, 8)
    print(rect.width)
    print(f"The area of the rectangle is: {rect.area}") # automatically call rect.area()
    print(rect.perimeter())
