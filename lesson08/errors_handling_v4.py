# put try: except blocks around the code below
# possibly turn this into a reusable function
# Reference: https://docs.python.org/3/library/exceptions.html

with open("students.txt", "r") as file:
    contents = file.read()

print(contents)

# another example
student = {"name": "John", "age": 20}
print(student["major"])

if __name__ == '__main__':
    ...