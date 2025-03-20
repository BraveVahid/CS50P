import re


def main():
    print(parse(input("HTML: ")))


def parse(html):
    pattern = r'<iframe.*?src="https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)".*?>'
    match = re.search(pattern, html)
    if match:
        return f"https://youtu.be/{match.group(1)}"
    return None


if __name__ == "__main__":
    main()
