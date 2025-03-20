def main():
    user_input = input("Input: ")
    shortened_text = shorten(user_input)
    print(f"Output: {shortened_text}")


def shorten(word):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    for i in word:
        if i in vowels:
            word = word.replace(i, "")
    return word


if __name__ == "__main__":
    main()
