def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not (2 <= len(s) <= 6):
        return False

    if not s[:2].isalpha():
        return False

    for char in s:
        if not char.isalnum():
            return False
    has_number = False

    for i in range(len(s)):
        if s[i].isdigit():
            if not has_number and s[i] == '0':
                return False
            has_number = True
        elif has_number:
            return False
    return True


if __name__ == "__main__":
    main()
