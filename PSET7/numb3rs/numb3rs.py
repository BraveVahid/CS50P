import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if not re.match(r"^\d+\.\d+\.\d+\.\d+$", ip):
        return False

    parts = ip.split(".")
    for part in parts:
        if not (0 <= int(part) <= 255):
            return False

    return True


if __name__ == "__main__":
    main()
