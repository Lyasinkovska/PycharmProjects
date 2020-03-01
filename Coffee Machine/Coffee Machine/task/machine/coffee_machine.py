# Write your code here
'''print('Starting to make a coffee\nGrinding coffee beans'
      '\nBoiling water\nMixing boiled water with crushed coffee '
      'beans\nPouring coffee into the cup\nPouring some '
      'milk into the cup\nCoffee is ready!')
'''

coffee = {"machine": {"water": 400, "milk": 540, "beans": 120, "cups": 9, "money": 550},
          "espresso": {"water": 250, "milk": 0, "beans": 16, "cups": 1, "price": 4},
          "latte": {"water": 350, "milk": 75, "beans": 20, "cups": 1, "price": 7},
          "cappuccino": {"water": 200, "milk": 100, "beans": 12, "cups": 1, "price": 6}}


def remaining(water, milk, beans, cups, money):
    return "The coffee machine has:\n{} of water\n{} of milk\n{} of coffee beans" \
                "\n{} of disposable cups\n{} of money".format(water, milk, beans, cups, money)


def espresso():
    if coffee["machine"]["water"] < coffee["espresso"]["water"]:
        print("Sorry, not enough water!")
    elif coffee["machine"]["beans"] < coffee["espresso"]["beans"]:
        print("Sorry, not enough coffee beans!")
    elif coffee["machine"]["milk"] < coffee["espresso"]["milk"]:
        print("Sorry, not enough milk!")
    elif coffee["machine"]["cups"] < coffee["espresso"]["cups"]:
        print("Sorry, not enough disposable cups!")
    else:
        print("I have enough resources, making you a coffee!")
        coffee["machine"]["water"] -= coffee["espresso"]["water"]
        coffee["machine"]["beans"] -= coffee["espresso"]["beans"]
        coffee["machine"]["milk"] -= coffee["espresso"]["milk"]
        coffee["machine"]["cups"] -= coffee["espresso"]["cups"]
        coffee["machine"]["money"] += coffee["espresso"]["price"]


def latte():
    if coffee["machine"]["water"] < coffee["latte"]["water"]:
        print("Sorry, not enough water!")
    elif coffee["machine"]["beans"] < coffee["latte"]["beans"]:
        print("Sorry, not enough coffee beans!")
    elif coffee["machine"]["milk"] < coffee["latte"]["milk"]:
        print("Sorry, not enough milk!")
    elif coffee["machine"]["cups"] < coffee["latte"]["cups"]:
        print("Sorry, not enough disposable cups!")
    else:
        print("I have enough resources, making you a coffee!")
        coffee["machine"]["water"] -= coffee["latte"]["water"]
        coffee["machine"]["beans"] -= coffee["latte"]["beans"]
        coffee["machine"]["milk"] -= coffee["latte"]["milk"]
        coffee["machine"]["cups"] -= coffee["latte"]["cups"]
        coffee["machine"]["money"] += coffee["latte"]["price"]


def cappuccino():
    if coffee["machine"]["water"] < coffee["cappuccino"]["water"]:
        print("Sorry, not enough water!")
    elif coffee["machine"]["beans"] < coffee["cappuccino"]["beans"]:
        print("Sorry, not enough coffee beans!")
    elif coffee["machine"]["milk"] < coffee["cappuccino"]["milk"]:
        print("Sorry, not enough milk!")
    elif coffee["machine"]["cups"] < coffee["cappuccino"]["cups"]:
        print("Sorry, not enough disposable cups!")
    else:
        print("I have enough resources, making you a coffee!")
        coffee["machine"]["water"] -= coffee["cappuccino"]["water"]
        coffee["machine"]["beans"] -= coffee["cappuccino"]["beans"]
        coffee["machine"]["milk"] -= coffee["cappuccino"]["milk"]
        coffee["machine"]["cups"] -= coffee["cappuccino"]["cups"]
        coffee["machine"]["money"] += coffee["cappuccino"]["price"]


def buy():
    buy = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, 4 - go back:\n")
    if buy == "1":
        espresso()
    elif buy == "2":
        latte()
    elif buy == "3":
        cappuccino()
    elif buy == "4":
        print(action)


def fill():
    water_fill= int(input("Write how many ml of water do you want to add:\n"))
    milk_fill = int(input("Write how many ml of milk do you want to add:\n"))
    beans_fill = int(input("Write how many grams of coffee beans do you want to add:\n"))
    cups_fill = int(input("Write how many disposable cups of coffee do you want to add:\n"))
    coffee["machine"]["water"] += water_fill
    coffee["machine"]["milk"] += milk_fill
    coffee["machine"]["beans"] += beans_fill
    coffee["machine"]["cups"] += cups_fill


def take(money):
    print("I gave you ${}".format(money))
    coffee["machine"]["money"] -= money


def coffee_machine():
    while True:
        water = coffee["machine"]["water"]
        milk = coffee["machine"]["milk"]
        beans = coffee["machine"]["beans"]
        cups = coffee["machine"]["cups"]
        money = coffee["machine"]["money"]

        action = input("Write action (buy, fill, take, remaining, exit):\n")

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


coffee_machine()