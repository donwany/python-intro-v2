import csv
from enum import Enum

class FileType(Enum):
    PDF = "pdf"
    CSV = "csv"
    JSON = "json"
    EXCEL = "xlsx"

fieldnames = ["product", "price"]
products = [
        ("Laptop", 1200),
        ("Mouse", 25),
        ("Keyboard", 75),
    ]


def csv_writer(file_name: str):

    with open(file_name, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        # using the forloop 
        for product, price in products:
            # print(product)
            writer.writerow({"product": product, "price": price})

def pdf_reader():
    """"""
    pass


file_type = FileType.CSV

if file_type == FileType.CSV:
    print("Writing to csv file")
    csv_writer(file_name="products.csv")
elif file_type == FileType.PDF:
    print("Read from pdf file")
    pdf_reader()