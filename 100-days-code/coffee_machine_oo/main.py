from menu import MenuItem, Menu
from coffe_machine import CoffeMachine
from money_machine import MoneyMachine


if __name__ == "__main__":
    print("Welcome to the Coffee Machine")
    money_machine = MoneyMachine()
    coffee_machine = CoffeMachine()
    menu = Menu()
    is_online = True

  
    while is_online:
        options = menu.get_items()
        choise = input(f"What would you like? ({options}): ")
        if choise == "off":
            is_online = False
        elif choise == "report":
            money_machine.report()
            coffee_machine.report()
        else:
            drink = menu.find_drink(choise)
            if coffee_machine.is_resources_sufficiente(drink) and money_machine.make_payment(drink.cost):
                coffee_machine.make_coffee(drink)