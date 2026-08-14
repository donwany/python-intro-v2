## Object-Oriented Programming
 - Abstraction
 - Polymorphism
 - Inheritance
 - Encapsulation


## Breakdown
 - define a `class` called `Person`
 - a class is like a `blueprint` for creating objects
 - a class = template(like a form)
 - an object = a filled-out form or Object = `instance of` a class
 - `class Person` - this will create a blueprint called `Person`
 -  `def __init__(self, name, age):`
    -  this a special function called a `constructor`
    -  it runs `automatically` when you create a new object
    -  it is used to `initialize` (set up) the object
    -  `self.name = name` - saves the `name` inside the object
    -  `self.age = age` - saves the `age` inside the object
 - `self` (most important part)
   - it means `this specific object`
   - every time you create a new object, `self` refers to that particular one
   - without `self` python wouldn't know `where to store the data`
 - `person1 = Person("Alice", 25)` and `person2 = Person("Bob", 30)`
 - `person1.name = Alice` and `person2.name = Bob`
 - `self` ensures each object keeps `its own data`
 - `def introduce(self)` - a function that belongs to the class (called a `method`), and it uses `self` to access that object's data.
 - `print(f"Hi, I'm {self.name} and I'm {self.age} years old.")`. It prints the name and age stored in that specific object.

## Usage
 - creates a new object
 - automatically calls `__init__`
 - `self = person1`
 - calls the method
 - `self` again refers to `person1`
```python
person1 = Person("Alice", 25)
person1.introduce()

person2 = Person("Bob", 30)
person2.introduce()
```

## Analogy
 - Think of `self` like a `label` on a box 📦
 - Each box (object) has its own label:
   - Box 1 → name: Alice, age: 25
   - Box 2 → name: Bob, age: 30
 - `self` = "this box right here"

## Practice Exercise
 - create a class called `Car` with:
 - `brand` and `year` fields
 - add a method `describe()` that prints "This car is a Toyota from 2020".
 - Create multiple car objects and call the method on each.
 - What happens if you don’t use `self`?


## An object: BankAccount, Car, Student, Order, Purchases, Animal ...
 - each object has its own attribute/fields
 - each object has its functions
 -  attributes: BankAccount (name, account_number, balance, routing_number, ...)
 -  functions of a BankAccount (saving, payment, deposit, withdraw, check_balance, ...)

## Inheritance: homework
```python
class AIModel:

    def load_model(self):
        print("Loading model")

    def predict(self, data):
        print(f"Making prediction on: {data}")

class LLM(AIModel):

    def generate(self, prompt):
        print(f"Generating response for: {prompt}")

llm = LLM()

llm.load_model()
llm.predict("Customer data")
llm.generate("Explain inheritance")

```

## Using @property homework
```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    @property
    def fahrenheit(self):
        return (self._celsius * 9 / 5) + 32

temperature = Temperature(25)
print(temperature.fahrenheit) # automatically calls temperature.fahrenheit()

class Employee:
    def __init__(self, monthly_salary):
        self.monthly_salary = monthly_salary
    @property
    def annual_salary(self):
        return self.monthly_salary * 12

employee = Employee(5000)
print(employee.annual_salary)

class Circle:
    def __init__(self, radius):
        self.radius = radius
    @property
    def diameter(self):
        return self.radius * 2

circle = Circle(radius=5)
circle.radius = 50
print(circle.diameter)

class Employee:
    def __init__(self, hourly_rate, hours_worked):
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
    @property
    def weekly_pay(self):
        return self.hourly_rate * self.hours_worked

employee = Employee(30, 40)
print(employee.weekly_pay)
employee.hours_worked = 45
print(employee.weekly_pay)
```