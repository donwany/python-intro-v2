# writing data to file

content = "where do you live"
file_path = "purchases.txt"

# write to file
# with open(file_path, mode='w') as file_name:
#     file_name.write(content)


# read it back
# with open(file_path, mode='r') as file_name:
#     content = file_name.read()
#     print(content)

# file_writer
def file_writer(file_path: str, content: str, mode="a"):
    with open(file_path, mode=mode) as file_name:
        file_name.write("\n" + content)

# file_reader
def file_reader(file_path: str, mode='r'):
    with open(file_path, mode=mode) as file_name:
        content = file_name.read()
        print(content)


file_writer(file_path=file_path, content=content)
# file_writer(file_path, content)
file_reader(file_path=file_path)
# file_reader(file_path)
