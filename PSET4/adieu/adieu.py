from inflect import engine

p = engine()
names = []

while True:
    try:
        name = input("Name: ").strip()
        names.append(name)
    except EOFError:
        break

print(f"Adieu, adieu, to {p.join(names)}")
