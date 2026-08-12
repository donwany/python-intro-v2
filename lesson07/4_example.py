# Inheritance: a concept where one class inherits `attributes` and `methods` from another class
# Designed purposely for code reusability and helps create a relationship between classes
# Without inheritance, you might repeat the same code
# Animal is the `Parent class` and Dog is the `child class`

class Animal:
    def eat(self):
        print("The animal is eating...")

    def sleep(self):
        print("The animal is sleeping...")


class Dog(Animal):
    def bark(self):
        print("The dog is barking")


class Cat(Animal):
    def meow(self):
        print("The cat said meow")


if __name__ == '__main__':
    dog = Dog()
    dog.eat()    # inherited from Animal class
    dog.sleep()  # inherited from Animal class
    dog.bark()   # defined in Dog class
    print("*" * 50)
    cat = Cat()
    cat.sleep()
    cat.eat()
    cat.meow()
