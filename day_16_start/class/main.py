"""This is the starting point of the program."""
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffeemaker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()


COFFEE_MACHINE_ON = True

while COFFEE_MACHINE_ON:
    choice = input(f" What would you like? ({menu.get_items()}): ").lower()
    if choice == "off":
        COFFEE_MACHINE_ON = False
    # Print report.
    elif choice == "report":
        coffeemaker.report()
        money_machine.report()
    else:
        # Check resources sufficient?
        drink = menu.find_drink(choice)
        if coffeemaker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffeemaker.make_coffee(drink)
            