while True:
    fraction = input("Fraction: ").strip()

    try:
        x, y = fraction.split("/")

        x = int(x)
        y = int(y)

        if y == 0:
            raise ZeroDivisionError
        if x > y:
            raise ValueError

        result = round((x / y) * 100)

        if result <= 1:
            print("E")
            break
        elif result >= 99:
            print("F")
            break
        else:
            print(f"{result}%")
            break

    except (ValueError, ZeroDivisionError):
        pass
