# built in function open()

# open the file
file_name = open("sales.txt", mode='r')
# read the content of the file
content = file_name.read()
print(content)
# close the file
file_name.close()

print("-" * 50)

# second way of read files 
with open("sales.txt", mode='r') as file_name:
    content = file_name.read()
    print(content)

print("-" * 50)

# third way to read files and print line by line 
with open("sales.txt", mode='r') as file_name:
    for line in file_name:
        print(line)