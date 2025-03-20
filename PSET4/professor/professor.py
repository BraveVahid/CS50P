from random import randint


def main():
    level = get_level()
    score = 0

    for i in range(10):
        a, b = generate_integer(level), generate_integer(level)
        c = a + b

        counter = 0
        while counter < 3:
            try:
                question = int(input(f"{a} + {b} = "))
                if question == c:
                    score += 1
                    break
                else:
                    print("EEE")
                    counter += 1
                    continue
            except ValueError:
                counter += 1
                pass
        else:
            print(f"{a} + {b} = {c}")

    print(score)


def get_level():
    while True:
        try:
            level =  int(input("Level: "))
            if level not in [1, 2, 3]:
                continue
            return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return randint(0, 9)
    elif level == 2:
        return randint(10, 99)
    elif level == 3:
        return randint(100, 999)


if __name__ == "__main__":
    main()
