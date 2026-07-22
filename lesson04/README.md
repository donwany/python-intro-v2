
### Student Information
```python
import sys

if len(sys.argv) != 4:
    print("Usage:")
    print("python student.py name age major")
    sys.exit()

name = sys.argv[1]
age = sys.argv[2]
major = sys.argv[3]

print(f"Student Name : {name}")
print(f"Age          : {age}")
print(f"Major        : {major}")

```

### File Reader
```python
import sys

if len(sys.argv) != 2:
    print("Usage: python reader.py filename")
    sys.exit()

filename = sys.argv[1]

try:
    with open(filename) as f:
        print(f.read())
except FileNotFoundError:
    print("File does not exist.")
    sys.exit(1)

```

### Command Line Calculator
```python
import sys

if len(sys.argv) != 4:
    print("Usage:")
    print("python calc.py number operator number")
    sys.exit()

a = float(sys.argv[1])
operator = sys.argv[2]
b = float(sys.argv[3])

if operator == "+":
    print(a + b)
elif operator == "-":
    print(a - b)
elif operator == "*":
    print(a * b)
elif operator == "/":
    print(a / b)
else:
    print("Unknown operator")

```

### File Writer
```python
if len(sys.argv) != 2:
    print("Usage: python file_manager.py <filename.txt>")
else:
    filename = sys.argv[1]
    with open(filename, 'r') as f:
        print(f.read())
    print("File processed successfully!")

print("-" * 50)
filename = input("Enter your file name: ")
with open(filename, 'r') as f:
    print(f.read())
    print("File processed successfully!")

```