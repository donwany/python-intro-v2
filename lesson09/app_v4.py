import argparse


def search(name: str):
    print(f"searching for information ... {name}")


def show_info(info: str):
    print(f"showing information ...{info}")


def get_data():
    print("getting data ...")


def get_weather(city: str):
    # implement weather API
    print(f"Getting weather data from: {city}")


parser = argparse.ArgumentParser(description="Data Analysis Tool")
parser.add_argument("--version", "-V", default="0.0.1", help="version information")

subparsers = parser.add_subparsers(dest="command", required=True)

# ------ search ------
search_parser = subparsers.add_parser(name="search", help="search for dataset information")
search_parser.add_argument("--name", help="search for information by name")
search_parser.add_argument("--age", help="search for information by age")
search_parser.add_argument("--height", help="search for information by height")

# ------- show info ----
show_parser = subparsers.add_parser(name="show", help="show dataset information")
show_parser.add_argument("--name", help="show information by name")
show_parser.add_argument("--age", help="show information by age")
show_parser.add_argument("--height", help="show information by height")
show_parser.add_argument("--filename", help="show information by filename")

# ---- get data ----
get_parser = subparsers.add_parser(name="get", help="get dataset information")
get_parser.add_argument("--name", help="get information by name")
get_parser.add_argument("--age", help="get information by age")

# --- weather information ----
weather_parser = subparsers.add_parser(name="weather", help="get weather information")
weather_parser.add_argument("--city", help="get weather by city name")

args = parser.parse_args()

if __name__ == '__main__':
    if args.command == "search":
        search(args.name)
    elif args.command == "show":
        show_info(args.age)
    elif args.command == "get":
        get_data()
    elif args.command == "weather":
        get_weather(args.city)
