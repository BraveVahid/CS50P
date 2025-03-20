items = dict()

while True:
    try:
        item = input().strip().lower()

        if item in items:
            items[item] += 1
        else:
            items[item] = 1

    except EOFError:
        break

sorted_items = sorted(items)

for i in sorted_items:
    print(f"{items[i]} {i.upper()}")
