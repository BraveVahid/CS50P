import csv
import sys
from tabulate import tabulate


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pizza.py filename.csv")

    filename = sys.argv[1]

    if not filename.endswith(".csv"):
        sys.exit("Not a CSV file")

    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            headers = next(reader)
            rows = list(reader)
    except FileNotFoundError:
        sys.exit("File does not exist")

    print(tabulate(rows, headers, tablefmt="grid"))


if __name__ == "__main__":
    main()
