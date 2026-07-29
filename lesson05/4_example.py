import csv

employees = [
    {"id": 1, "name": "Alice", "department": "Engineering"},
    {"id": 2, "name": "Bob", "department": "Marketing"},
    {"id": 3, "name": "Charlie", "department": "Finance"},
]

# read csv as Dictionary using csv.DictWriter()
employees_csv = "employees.csv"
column_names = ["id", "name", "department"]

with open(employees_csv, "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=column_names)

    writer.writeheader() # write column names
    writer.writerows(employees) # write multiple rows

    print("CSV file created successfully!")


# one row at a time 
with open(employees_csv, "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=column_names)

    writer.writeheader() # write column names
    writer.writerow({"id": 1, "name": "Alice", "department": "Engineering"})
    writer.writerow({"id": 2, "name": "Bob", "department": "Marketing"})
    writer.writerow({"id": 3, "name": "Charlie", "department": "Finance"})

    print("CSV file created successfully!")


# using for loops 
with open(employees_csv, "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=column_names)

    writer.writeheader() # write column names

    for employee in employees:
        writer.writerow(employee)

    print("CSV file created successfully!")