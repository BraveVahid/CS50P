months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

while True:
    date = input("Date: ").strip()

    try:
        if "/" in date:
            month, day, year = date.split("/")
            month = int(month)
            day = int(day)
            year = int(year)

        elif "," in date:
            month_day, year = date.split(", ")
            month, day = month_day.split(" ")
            month = months.index(month) + 1
            day = int(day)
            year = int(year)

        else:
            raise ValueError

        if day < 1 or day > 31 or month < 1 or month > 12:
            raise ValueError
        print(f"{year:04}-{month:02}-{day:02}")
        break

    except (ValueError, IndexError):
        print("Invalid date. Please try again.")
