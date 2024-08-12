from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
coffeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()
menu = Menu()
is_on = True
while is_on:
    sel = input(f"What would you like? ({menu.get_items()}):")
    if sel == "off":
        is_on = False
    elif sel == "report":
        coffeMaker.report()
        moneyMachine.report()
    else:
        drink = menu.find_drink(sel)
        stock = coffeMaker.is_resource_sufficient(drink)
        if stock:
            pay = moneyMachine.make_payment(drink.cost)
            if pay:
                coffeMaker.make_coffee(drink)



