# from utils import add, subtract, multiply, divide
# from utils import add
from utils import *


addition = add(10., 5.)
subtraction = subtract(10., 5.)
multiplication = multiply(10., 5.)
division = divide(10., 5.)

print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")

print("\nNow using explicit variable names in the function calls:")

# explicit about the variable
addition = add(a=10., b=5.)
subtraction = subtract(a=10., b=5.)
multiplication = multiply(a=10., b=5.)
division = divide(a=10., b=5.)

print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")