# primitive data types 
# int, float, bool, str

my_int = 5
my_float = 3.14
my_bool = True
my_str = "Hello, World!"
name = "Alice"
char = 'A'


print(my_int)
print(my_float)
print(my_bool)
print(my_str)
print(name)
print(char)


# checking data types - type(), print()
print(type(my_int)) # <class 'int'>
print(type(my_float)) # <class 'float'>
print(type(my_bool)) # <class 'bool'>
print(type(my_str)) # <class 'str'>
print(type(name)) # <class 'str'>
print(type(char)) # <class 'str'>

print("*" * 20)

cash = 100.50
print(cash * 3) # 301.5
print(type(cash)) # <class 'float'>
money = str(cash) # convert float to string
print(type(money)) # <class 'str'>
print(money) # "100.5"
print(money * 3) # "100.5100.5100.5"

money_v2 = int("123") # convert string to int
print(money_v2) # 123


print(type(money_v2)) # <class 'int'>
print(type(float(money))) # <class 'float'>
print(float(money)) # 100.5

# dictionary (key:value) pairs, with dictionaries use square brackets [] to access the values
person = {"name": "Alice","age": 30, "city": "New York", "is_active": False, "height": 5.5}
print(person) # {'name': 'Alice', 'age': 30, 'city': 'New York', 'is_active': False, 'height': 5.5}
print(type(person)) # <class 'dict'>
print(person["name"]) # Alice
print(person["age"]) # 30
print(person["city"]) # New York
print(person["is_active"]) # False
print(person["height"]) # 5.5
print(type(person["is_active"])) # <class 'bool'>

# age = 99, str(99) -> "99", type(str(99)) -> <class 'str'>
print(person["age"] + 20) # 50
print(f"The person's age is {person['age']} and he lives in {person['city']}")