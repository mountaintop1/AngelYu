""" Coffee Machine Project"""
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
}

PROFIT = 0

# Todo: 1 create a function to check if the resources are sufficient

def check_resources(drink_name):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in MENU[drink_name]["ingredients"]:
        if MENU[drink_name]["ingredients"][item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

# Todo: 2 create a function to process coins

def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

# Todo: 3 create a function to check if the transaction is successful

def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global PROFIT
        PROFIT += drink_cost
        return True
    print("Sorry that's not enough money. Money refunded.")
    return False


# Todo: 6 create a function to print the report
def report():
    """Prints a report of all resources."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${PROFIT}")

# Todo: 7 create a function to check if the user wants to turn off the machine

COFFEE_MACHINE_ON = True

while COFFEE_MACHINE_ON:
    # Prompt user by asking “ What would you like? (espresso/latte/cappuccino):”
    choice = input(" What would you like? (espresso/latte/cappuccino): ").lower()
    # Turn off the Coffee Machine by entering “ off” to the prompt.
    if choice == "off":
        COFFEE_MACHINE_ON = False
    # Print report.
    elif choice == "report":
        report()
    else:
        # Check resources sufficient?
        drink = MENU[choice]
        if check_resources(choice):
            # Process coins.
            payment = process_coins()
            # Check transaction successful?
            if is_transaction_successful(payment, drink["cost"]):
                # Make Coffee.
                print(f"Here is your {choice} ☕️. Enjoy!")
                for item in drink["ingredients"]:
                    resources[item] -= drink["ingredients"][item]