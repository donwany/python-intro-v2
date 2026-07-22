import sys


print(sys.version)
print(sys.version_info)
print(sys.version_info.major)
print(sys.version_info.minor)

print(sys.argv) # entire thing here is a list
print(len(sys.argv))

if len(sys.argv) != 4:
    print("Usage: uv run 1_example.py <name> <age> <state>")
    sys.exit(1) # means Failure
    # sys.exit(0) means successful execution

print(f"Program: {sys.argv[0]}")
print(f"Name: {sys.argv[1]}")
print(f"Age: {sys.argv[2]}")
print(f"State: {sys.argv[3]}")