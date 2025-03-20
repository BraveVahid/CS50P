import sys


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python lines.py filename.py")

    filename = sys.argv[1]

    if not filename.endswith(".py"):
        sys.exit("Not a Python file")

    try:
        with open(filename, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        sys.exit("File does not exist")

    print(count_lines(lines))


def count_lines(lines):
    count = 0
    for line in lines:
        stripped_line = line.strip()
        if stripped_line and not stripped_line.startswith("#"):
            count += 1
    return count


if __name__ == "__main__":
    main()
