MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

def show_resources():
    print(f'''
        Water: {resources["water"]}ml
        Milk: {resources["milk"]}ml
        Coffee: {resources["coffee"]}g
        Money: ${resources["money"]}
    ''')

def enough_resources(ingredients):
    for i, v in ingredients:
        if resources[i] < v:
            print(f"Sorry, there is not enough {i}")
            return False
    return True

def get_coins():
    coins = {
        "quarters": {"value": 0.25, "qnt": 0.0},
        "dimes": {"value": 0.10, "qnt": 0.0},
        "nickles": {"value": 0.05, "qnt": 0.0},
        "pennies": {"value": 0.01, "qnt": 0.0},
    }

    total = 0
    for i in coins:
        coins[i]["qnt"] = float(input(f"How many {i}: "))
        total += coins[i]["value"] * coins[i]["qnt"]
    
    return total

def verify_money(total_inserted, price_coffee):
    if total_inserted < price_coffee:
        print("Sorry that's not enough money. Money refunded.")
        return False

    return True

def verify_change(total_inserted, price_coffee):
    if total_inserted > price_coffee:
        change = total_inserted - price_coffee
        print(f"Here is ${round(change, 2)} dollars in change.")

    return price_coffee

def get_coffee(type):
    ingredients_needed = MENU[type]["ingredients"]

    if enough_resources(ingredients_needed.items()):
        total_inserted = get_coins()

        if verify_money(total_inserted, MENU[type]["cost"]):
            for ingredient, value in ingredients_needed.items():
                resources[ingredient] -= value

            resources["money"] += verify_change(total_inserted, MENU[type]["cost"])

            print(f"Here is your {type}. Enjoy!")

continue_coffee_machine = True

while continue_coffee_machine:
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    if choice == "off":
        continue_coffee_machine = False
    elif choice == "report":
        show_resources()
    else:
        get_coffee(choice)