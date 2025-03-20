from random import randint


while True:
    try:
        level = int(input("Level: "))
        if level >= 1:
            random_number = randint(1, level)
            break
    except ValueError:
        pass


while True:
    try:
        guess = int(input("Guess: "))
        if guess >= 1:
            if random_number > guess:
                print("Too small!")
            elif random_number < guess:
                print("Too large!")
            else:
                print("Just right!")
                break
    except ValueError:
        pass
