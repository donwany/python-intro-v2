import argparse

parser = argparse.ArgumentParser(description="student information program")
parser.add_argument(
    "--name", "-n", required=False, default="Alex", type=str, help="student name"
)
parser.add_argument(
    "--age", "-a", required=False, default=100, type=int, help="student age"
)
parser.add_argument(
    "--color",
    "-c",
    required=False,
    choices=["blue", "green", "red"],
    default="red",
    type=str,
    help="student color",
)
args = parser.parse_args()


def print_student_info(name: str, age: int):
    print(f"Student information: name={name} and age={age}")


if __name__ == "__main__":
    # name = args.name
    # age = args.age
    print(args.color)
    print_student_info(args.name, args.age)
