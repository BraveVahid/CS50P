user_input = input("Input: ")
vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

for i in user_input:
    if i in vowels:
        user_input = user_input.replace(i, "")

print(f"Output: {user_input}")
