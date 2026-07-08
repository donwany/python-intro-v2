# num1, num2, num3 = 10, 5, 50
num1 = 10
num2 = 5
num3 = 50
num4 = 20

count = 4

total = num1 + num2 + num3 + num4
average = total / count
print(f"Average: {average}")

# method 1:
def average_v1(num1, num2, num3, num4):
    total = num1 + num2 + num3 + num4
    n = 4
    results = total / n
    return results


def average_v2(num1, num2, num3, num4):
    total = num1 + num2 + num3 + num4
    results = total / 4
    return results

def average_v3(num1, num2, num3, num4):
    total = num1 + num2 + num3 + num4
    return total / 4

def average_v4(num1:float, num2:float, num3:float, num4:float) -> float:
    return (num1 + num2 + num3 + num4) / 4


def average_v5(num1: int, num2: int, num3: int, num4: int) -> float:
    return (num1 + num2 + num3 + num4) / 4


# heights
results = average_v4(5.0, 6.0, 5.0, 7.0)
print(f"Average height: {results}")

# ages
average_ages = average_v5(50, 60, 59, 78)
print(f"Average age: {average_ages}")

print(f"Average v4: {average_v4(num1, num2, num3, num4)}")
print(f"Average v4: {average_v4(50, 60, 59, 78)}")


# advance method 
def average_v6(numbers: list) -> float:
    total = sum(numbers)
    count = len(numbers)
    return total / count

def average_v7(numbers: list) -> float:
    return sum(numbers) / len(numbers)

ages = [50, 60, 59, 78]
print(f"Average v6: {average_v6(ages)}")
print(f"Average v7: {average_v7(ages)}")