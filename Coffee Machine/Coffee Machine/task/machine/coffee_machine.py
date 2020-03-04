'''coffee = {
    "machine": {"water": 400, "milk": 540, "beans": 120, "cups": 9, "money": 550},
    "espresso": {"water": 250, "milk": 0, "beans": 16, "cups": 1, "price": 4},
    "latte": {"water": 350, "milk": 75, "beans": 20, "cups": 1, "price": 7},
    "cappuccino": {"water": 200, "milk": 100, "beans": 12, "cups": 1, "price": 6}
}


def remaining(water, milk, beans, cups, money):
    return "The coffee machine has:\n{} of water\n{} of milk\n{} of coffee beans" \
           "\n{} of disposable cups\n{} of money".format(water, milk, beans, cups, money)


def resources(kind):
    if coffee["machine"]["water"] < coffee[kind]["water"]:
        print("Sorry, not enough water!")
    elif coffee["machine"]["beans"] < coffee[kind]["beans"]:
        print("Sorry, not enough coffee beans!")
    elif coffee["machine"]["milk"] < coffee[kind]["milk"]:
        print("Sorry, not enough milk!")
    elif coffee["machine"]["cups"] < coffee[kind]["cups"]:
        print("Sorry, not enough disposable cups!")
    else:
        print("I have enough resources, making you a coffee!")
        coffee["machine"]["water"] -= coffee[kind]["water"]
        coffee["machine"]["beans"] -= coffee[kind]["beans"]
        coffee["machine"]["milk"] -= coffee[kind]["milk"]
        coffee["machine"]["cups"] -= coffee[kind]["cups"]
        coffee["machine"]["money"] += coffee[kind]["price"]


def buy():
    buy = ask_user("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, 4 - go back:\n")
    if buy == "1":
        resources("espresso")
    elif buy == "2":
        resources("latte")
    elif buy == "3":
        resources("cappuccino")
    elif buy == "4":
        print(action)


def fill():
    water = int(ask_user("Write how many ml of water do you want to add:\n"))
    milk = int(ask_user("Write how many ml of milk do you want to add:\n"))
    beans = int(ask_user("Write how many grams of coffee beans do you want to add:\n"))
    cups = int(ask_user("Write how many disposable cups of coffee do you want to add:\n"))
    coffee["machine"]["water"] += water
    coffee["machine"]["milk"] += milk
    coffee["machine"]["beans"] += beans
    coffee["machine"]["cups"] += cups


def take(money):
    print("I gave you ${}".format(money))
    coffee["machine"]["money"] -= money


def ask_user(message):
    return input(message)


def coffee_machine():
    while True:
        water = coffee["machine"]["water"]
        milk = coffee["machine"]["milk"]
        beans = coffee["machine"]["beans"]
        cups = coffee["machine"]["cups"]
        money = coffee["machine"]["money"]

        action = ask_user("Write action (buy, fill, take, remaining, exit):\n")

        if action == "buy":
            buy()
            continue
        elif action == "fill":
            fill()
            continue
        elif action == "take":
            take(money)
            continue
        elif action == "remaining":
            print(remaining(water, milk, beans, cups, money))
            continue
        elif action == "exit":
            break


coffee_machine()'''

from coffee_machine_class import CoffeeMachine

my_coffee = CoffeeMachine()


