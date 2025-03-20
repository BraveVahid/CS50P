nutrition_facts = {
    "apple": 130,
    "avocado": 50,
    "banana": 110,
    "cantaloupe": 50,
    "grapefruit": 60,
    "grapes": 90,
    "honeydew": 50,
    "kiwifruit": 90,
    "lemon": 15,
    "lime": 20,
    "orange": 80,
    "peach": 60,
    "pear": 100,
    "pineapple": 50,
    "plum": 70,
    "strawberry": 50,
    "sweet cherries": 100,
    "tangerine": 50,
    "watermelon": 80,
}

user_input = input("Item: ").lower()

if user_input in nutrition_facts:
    print(f"Calories: {nutrition_facts[user_input]}")
