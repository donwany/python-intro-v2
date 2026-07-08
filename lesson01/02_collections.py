# collections in Python
# lists, tuples, sets

# list - ordered, changeable, allows duplicates
fruits = ["apple", "banana", "cherry", "apple", "banana", True, 5, 3.14]
print(fruits) # ['apple', 'banana', 'cherry']
print(type(fruits)) # <class 'list'>
print(fruits[0]) # apple
print(fruits[1]) # banana
print(fruits[2]) # cherry
print(fruits[3]) # apple
print(fruits[7]) # 3.14

heights = [5.5, 6.0, 5.8, 6.2, 5.9]
print(heights) # [5.5, 6.0, 5.8, 6.2, 5.9]
print(type(heights)) # <class 'list'>
print(heights[0]) # 5.5
print(heights[1]) # 6.0
print(heights[2]) # 5.8
print(heights[3]) # 6.2
print(heights[4]) # 5.9

countries = ["USA", "Canada", "Mexico", "USA", "Canada"]
print(countries) # ['USA', 'Canada', 'Mexico', 'USA', 'Canada']
print(type(countries)) # <class 'list'>
print(countries[0]) # USA
print(countries[1]) # Canada
print(countries[2]) # Mexico
print(countries[3]) # USA
print(countries[4]) # Canada

print("*" * 20)

# for loops 
for height in heights:
    print(height + 10)

print("*" * 20)

for country in countries:
    print(country)

print("*" * 20)

for fruit in fruits:
    print(fruit)

print("*" * 20)

# range function
for i in range(6):
    print(i)


print("*" * 20)
for i in range(2, 10):
    print(i)

print("*" * 20)

for i in range(2, 10, 3):
    print(i)


print("*" * 20)
person = {"name": "Alice", "age": 30, "city": "New York"}
print(person) # {'name': 'Alice', 'age': 30, 'city': 'New York'}
print(type(person)) # <class 'dict'>
print(person["name"]) # Alice
print(person["age"]) # 30
print(person["city"]) # New York

student  = {} # empty dictionary
student["name"] = "Bob"
student["age"] = 25
student["city"] = "Los Angeles"
print(student) # {'name': 'Bob', 'age': 25, 'city': 'Los Angeles'}

# adding elements to a list 
fruits.append("orange")
print(fruits) # ['apple', 'banana', 'cherry', 'apple', 'banana', True, 5, 3.14, 'orange']

# add multiple elements to a list
fruits.extend(["grape", "kiwi"])
print(fruits) # ['apple', 'banana', 'cherry', 'apple', 'banana', True, 5, 3.14, 'orange', 'grape', 'kiwi']

# adding elements to a dictionary
student["grade"] = "A"
print(student) # {'name': 'Bob', 'age': 25, 'city': 'Los Angeles', 'grade': 'A'}

# creating a new list with the same elements as another list
county = []
for country in countries:
    if country == "USA":
        county.append(country)

print(county) # ['USA']

county.insert(0, "Canada")
print(county) # ['Canada', 'USA']

employees = ['John', 'Jane', 'Bob']
print(employees) # ['John', 'Jane', 'Bob']
employees = employees + ['Alice', 'Charlie', 3.5]
print(employees) # ['John', 'Jane', 'Bob', 'Alice', 'Charlie']

# remove elements in a list
employees.remove('Bob')
print(employees) # ['John', 'Jane', 'Alice', 'Charlie']

# pop elements from a list
popped_employee = employees.pop()
print(popped_employee) # Charlie
print(employees) # ['John', 'Jane', 'Alice']

# zip function in python 
names = ['John', 'Jane', 'Bob', 'Alice']
ages = [25, 30, 35]
zipped = zip(names, ages)
print(list(zipped)) # [('John', 25), ('Jane', 30), ('Bob', 35)]