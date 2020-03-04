available_resources = {"water": 400, "milk": 540, "beans": 120, "cups": 9, "money": 550}


coffee_ingredients_needed = {
    "espresso": {"water": 250, "milk": 0, "beans": 16, "cups": 1, "price": 4},
    "latte": {"water": 350, "milk": 75, "beans": 20, "cups": 1, "price": 7},
    "cappuccino": {"water": 200, "milk": 100, "beans": 12, "cups": 1, "price": 6}
}


def get_remaining_resources(water, milk, beans, cups, money):
    return "The coffee machine has:\n{} of water\n{} of milk\n{} of coffee beans" \
           "\n{} of disposable cups\n{} of money".format(water, milk, beans, cups, money)


def resources_check(product_type):
    if available_resources["water"] < coffee_ingredients_needed[product_type]["water"]:
        notify_user("Sorry, not enough water!")
    elif available_resources["beans"] < coffee_ingredients_needed[product_type]["beans"]:
        notify_user("Sorry, not enough coffee beans!")
    elif available_resources["milk"] < coffee_ingredients_needed[product_type]["milk"]:
        notify_user("Sorry, not enough milk!")
    elif available_resources["cups"] < coffee_ingredients_needed[product_type]["cups"]:
        notify_user("Sorry, not enough disposable cups!")
    else:
        notify_user("I have enough resources, making you a coffee!")
        available_resources["water"] -= coffee_ingredients_needed[product_type]["water"]
        available_resources["beans"] -= coffee_ingredients_needed[product_type]["beans"]
        available_resources["milk"] -= coffee_ingredients_needed[product_type]["milk"]
        available_resources["cups"] -= coffee_ingredients_needed[product_type]["cups"]
        available_resources["money"] += coffee_ingredients_needed[product_type]["price"]


def buy():
    selected_option = get_response_from_user("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, 4 - go back:\n")
    if selected_option == "1":
        resources_check("espresso")
    elif selected_option == "2":
        resources_check("latte")
    elif selected_option == "3":
        resources_check("cappuccino")
    elif selected_option == "4":
        return


def fill():
    water = int(get_response_from_user("Write how many ml of water do you want to add:\n"))
    milk = int(get_response_from_user("Write how many ml of milk do you want to add:\n"))
    beans = int(get_response_from_user("Write how many grams of coffee beans do you want to add:\n"))
    cups = int(get_response_from_user("Write how many disposable cups of coffee do you want to add:\n"))
    available_resources["water"] += water
    available_resources["milk"] += milk
    available_resources["beans"] += beans
    available_resources["cups"] += cups


def take_money():
    money = available_resources["money"]
    notify_user("I gave you ${}".format(money))
    available_resources["money"] -= money


def get_response_from_user(message):
    return input(message)


def notify_user(message):
    print(message)


def coffee_machine():
    while True:
        water = available_resources["water"]
        milk = available_resources["milk"]
        beans = available_resources["beans"]
        cups = available_resources["cups"]

        action = get_response_from_user("Write action (buy, fill, take, remaining, exit):\n")

        if action == "buy":
            buy()
            continue
        elif action == "fill":
            fill()
            continue
        elif action == "take":
            take_money()
            continue
        elif action == "remaining":
            notify_user(get_remaining_resources(water, milk, beans, cups, money))
            continue
        elif action == "exit":
            break


coffee_machine()
