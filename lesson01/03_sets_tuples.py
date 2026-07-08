# sets 
fruits = {"apple", "banana", "cherry"}
print(fruits)
# print(fruits[0]) # doesnt work

print(list(fruits)[0])
# print(fruits.pop())

print("*" * 20)

# loop over the set 
for fruit in fruits:
    print(fruit)

# remove element 
fruits.remove("banana")
print(fruits)

# add element 
fruits.add("mango")
print(fruits)

# team a 
team_a = {"Alice", "Bob", "Charlie"}

# team b 
team_b = {"David", "Eve", "Alice"}

# union of two sets
team_c = team_a.union(team_b)
print(team_c)

# intersection of two sets
team_d = team_a.intersection(team_b)
print(team_d)

# difference of two sets
team_e = team_b.difference(team_a)
print(team_e)

# if two sets are disjoint 
print(team_a.isdisjoint(team_b))

# add an element to a set
team_a.add("David")
print(team_a)

# remove an element from a set
team_a.remove("David")
print(team_a)


# check if an element is in a set
print("Alice" in team_a)

for name in team_a:
    if "Alice" in team_a:
        print("Found Alice in the set!")
    else:
        print("Alice not found in the set.")


# --------------------
# tuples
# --------------------

# create a tuple
coordinates = (40.7128, -74.0060, 40.7128)
print(coordinates)

latitude = coordinates[0]
longitude = coordinates[1]

# tuple unpacking
latitude, longitude, _ = coordinates

print(f"Latitude: {latitude}, Longitude: {longitude}")

# access elements in a tuple
print(coordinates[0])
print(coordinates[1])

# tuples are immutable
# coordinates[0] = 41.8781  # This will raise an error
# print(coordinates)

# count the number of occurrences of an element in a tuple
print(coordinates.count(40.7128))

# index of an element in a tuple
print(coordinates.index(40.7128))

person = ("Alice", 30, "Engineer")
print(person)

# access elements in a tuple
print(person[0])
print(person[1])
print(person[2])

print(f"Name: {person[0]}, Age: {person[1]}, Occupation: {person[2]}")

# tuple unpacking
name, age, occupation = person
print(f"Name: {name}, Age: {age}, Occupation: {occupation}")

# string formating
print("Name: {}, Age: {}, Occupation: {}".format(name, age, occupation))

print("Name: {0}, Age: {1}, Occupation: {2}".format(name, age, occupation))

print("Name: {name}, Age: {age}, Occupation: {occupation}".format(name=name, age=age, occupation=occupation))

print("The person age is: ", age)
print(f"The person age is: {age}")

# more on tuples 
my_server = ("192.168.1.1", 8080, "Ubuntu")
print(my_server)

# access elements in a tuple
print(my_server[0])
print(my_server[1])
print(my_server[2])

# tuple unpacking
ip, port, os = my_server
print(f"IP: {ip}, Port: {port}, OS: {os}")

# a list with tuples inside 
servers = [
    ("192.168.1.1", 8080, "Ubuntu"),
    ("192.168.1.2", 8081, "CentOS"),
    ("192.168.1.3", 8082, "Debian")
]
print(servers)

# access elements in the list
print(servers[0])
print(servers[1])
print(servers[2])

# tuple unpacking in a loop
for ip, port, os in servers:
    print(f"IP: {ip}, Port: {port}, OS: {os}")

# a tuple with a list inside
person_info = ("John", [25, "Engineer", "New York"])
print(person_info)

# access elements in the tuple
print(person_info[0])
print(person_info[1])

# access elements in the list inside the tuple
print(person_info[1][0]) # 25
print(person_info[1][1]) # Engineer
print(person_info[1][2]) # New York

name, person_details = person_info
print(f"Name: {name}, Age: {person_details[0]}, Occupation: {person_details[1]}, City: {person_details[2]}")


# a list with dictionary inside
users = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]
print(users)
print(users[1]['age']) # 25

# a list with tuple inside
coordinates_list = [
    (10.0, 20.0),
    (30.0, 40.0),
    (50.0, 60.0)
]
print(coordinates_list[1][1]) # 40.0

# a list inside a list
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[1][2]) # 6



data = [
    {
        "role": "user",
            "content": [
                {
                    "type": "input_text",
                    "text": "What teams are playing in this image?",
                },
                {
                    "type": "input_image",
                    "image_url": "https://api.nga.gov/iiif/a2e6da57-3cd1-4235-b20e-95dcaefed6c8/full/!800,800/0/default.jpg"
                },
                {
                    "type": "input_text",
                    "text": "What teams are playing in this image?"
                }
        ]
    }
]

print(data[0]['content'][1]['image_url'])


messages = {
    "message1": {"ghana": ["Hello, how are you?", "timestamp", "2024-06-01 10:00:00"]},
    "message2": {"usa": ["I'm good, thanks!", "timestamp", "2024-06-01 10:01:00"]},
    "message3": {"canada": ["What about you?", "timestamp", "2024-06-01 10:02:00"]}
}
print(messages["message2"]['usa'][2])

