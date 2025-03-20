from datetime import date
import sys
import inflect

p = inflect.engine()


def main():
    birth_date = input("Date of Birth: ")
    total_minutes = get_total_minutes(birth_date)

    if total_minutes is None:
        sys.exit("Invalid date")

    minutes_in_words = p.number_to_words(total_minutes, andword="").capitalize()
    print(f"{minutes_in_words} minutes")


def get_total_minutes(d):
    try:
        birth_date = date.fromisoformat(d)
        return (date.today() - birth_date).days * 1440
    except ValueError:
        return None


if __name__ == "__main__":
    main()
