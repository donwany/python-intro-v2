import argparse


def show_info(filename):
    print(f"Showing information for {filename}")


def show_head(filename, rows):
    print(f"Showing first {rows} rows from {filename}")


def search_data(filename, column, value):
    print(
        f"Searching {filename}: "
        f"{column} = {value}"
    )


def main():

    parser = argparse.ArgumentParser(
        description="Command-line data analysis tool"
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True
    )

    # -------------------------
    # INFO
    # -------------------------

    info_parser = subparsers.add_parser(
        "info",
        help="Display dataset information"
    )

    info_parser.add_argument(
        "filename",
        help="Path to dataset"
    )

    # -------------------------
    # HEAD
    # -------------------------

    head_parser = subparsers.add_parser(
        "head",
        help="Display first rows"
    )

    head_parser.add_argument(
        "filename",
        help="Path to dataset"
    )

    head_parser.add_argument(
        "--rows",
        type=int,
        default=5,
        help="Number of rows"
    )

    # -------------------------
    # SEARCH
    # -------------------------

    search_parser = subparsers.add_parser(
        "search",
        help="Search dataset"
    )

    search_parser.add_argument(
        "filename",
        help="Path to dataset"
    )

    search_parser.add_argument(
        "--column",
        required=True,
        help="Column to search"
    )

    search_parser.add_argument(
        "--value",
        required=True,
        help="Value to search for"
    )

    args = parser.parse_args()

    # -------------------------
    # COMMAND DISPATCH
    # -------------------------

    if args.command == "info":
        show_info(args.filename)

    elif args.command == "head":
        show_head(
            args.filename,
            args.rows
        )

    elif args.command == "search":
        search_data(
            args.filename,
            args.column,
            args.value
        )


if __name__ == "__main__":
    main()