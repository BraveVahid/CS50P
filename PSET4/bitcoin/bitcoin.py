import requests
import sys


def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        user_input = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    current_price = get_btc_price()
    print(get_btc_amount(user_input, current_price))


def get_btc_price():
    url = "https://api.coincap.io/v2/assets/bitcoin"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    price = data["data"]["priceUsd"]
    return price


def get_btc_amount(amount, price):
    return f"${amount * float(price):,.4f}"


if __name__ == "__main__":
    main()
