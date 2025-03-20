import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"^(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)$"
    match = re.match(pattern, s)
    if not match:
        raise ValueError("Invalid time format")

    start_hour, start_minute, start_period, end_hour, end_minute, end_period = match.groups()

    start = convert_to_24h(start_hour, start_minute, start_period)
    end = convert_to_24h(end_hour, end_minute, end_period)

    return f"{start} to {end}"


def convert_to_24h(hour, minute, period):
    if minute is None:
        minute = "00"
    if not 0 <= int(minute) < 60:
        raise ValueError("Invalid minute")

    hour = int(hour)
    if not 1 <= hour <= 12:
        raise ValueError("Invalid hour")

    if period == "PM" and hour != 12:
        hour += 12
    elif period == "AM" and hour == 12:
        hour = 0

    return f"{hour:02}:{minute}"


if __name__ == "__main__":
    main()
