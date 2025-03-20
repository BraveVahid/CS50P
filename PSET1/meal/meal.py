def main():
    time = input("What time it is? ").strip()
    hours = convert(time)
    if 7 <= hours <= 8:
        print("breakfast time")
    elif 12 <= hours <= 13:
        print("lunch time")
    elif 18 <= hours <= 19:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    return float(hours) + float(minutes) / 60


if __name__ == "__main__":
    main()
