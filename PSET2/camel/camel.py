user_input = input("camelCase: ")

result = str()
for i in user_input:
    if i.isupper():
        result += "_" + i.lower()
    else:
        result += i

print(result)
