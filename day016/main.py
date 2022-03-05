from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from os import system, name


# HINT: You can call clear() to clear the output in the console.

# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


#
# print(coffee_maker.report())

def coffee_app():
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    real_menu = menu.get_items().split("/")
    real_menu.remove("")

    user_input = ""
    display_menu = menu.menu

    while user_input != 'off':
        clear()
        print("Welcome! Please make your selection from the below choices:")
        for item in display_menu:
            print(f"{item.name}: ${item.cost:.2f}")
        user_input = input(f"Enter {menu.get_items()}:  ")

        if user_input == 'report':
            coffee_maker.report()
        elif user_input == 'profit':
            print(f"Money: ${money_machine.profit:.2f}.")
        elif user_input == 'refill':
            coffee_maker.resources = CoffeeMaker().resources
        elif menu.find_drink(user_input):
            menu_item = menu.find_drink(user_input)
            if money_machine.make_payment(menu_item.cost):
                if coffee_maker.is_resource_sufficient(menu_item):
                    coffee_maker.make_coffee(menu_item)
                # print(menu.find_drink(user_input))
        user_input = input("Press 'Enter' to complete your order:")


coffee_app()
