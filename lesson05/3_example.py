import csv

# write rows to a new csv file 
data = [
    ["name", "age", "city"],
    ["Alice", 25, "New York"],
    ["George", 101, "Dallas"]
]

with open("person.csv", mode="w") as person:
    writer = csv.writer(person, delimiter=",")
    writer.writerows(data)


# write one row at a time 
with open("stock.csv", mode="w", newline="") as stock:
    writer = csv.writer(stock, delimiter=",")
    # write column names 
    writer.writerow(["StockName", "StockPrice"])

    # write column values
    writer.writerow(["AAPL", 230])
    writer.writerow(["MICROSOFT", 158])
    writer.writerow(["TESLA", 699])


FILE_NAME = "stock_v2.csv"
COL_NAMES = ["StockName", "StockPrice"]

data = [
    ["AAPL", 25],
    ["MICROSOFT", 101],
    ["TESLA", 699]
]

# write csv file using csv.writer()
with open(FILE_NAME, mode="w", newline="") as stock:
    writer = csv.writer(stock, delimiter=",")
    # write column names 
    writer.writerow(COL_NAMES)

    # write column values
    writer.writerows(data)


# read csv file using csv.reader()
with open(FILE_NAME, mode="r", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row[0], row[1])

print("*"*100)

# read csv as Dictionary using csv.DictReader()
with open(FILE_NAME, mode="r", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row['StockName'], row['StockPrice'])