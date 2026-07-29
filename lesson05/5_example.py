import csv

fieldnames = ["product", "price"]

products = [
        ("Laptop", 1200),
        ("Mouse", 25),
        ("Keyboard", 75),
    ]

with open("products.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

    # using the forloop 
    for product, price in products:
        # print(product)
        writer.writerow({"product": product, "price": price})