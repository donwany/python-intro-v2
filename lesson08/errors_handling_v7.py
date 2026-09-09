
if __name__ == '__main__':

    # File handling example
    try:
        with open("data.txt", "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("File not found. Please check the filename.")
    except PermissionError:
        print("You don't have permission to open this file.")