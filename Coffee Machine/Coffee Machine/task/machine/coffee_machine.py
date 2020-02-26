# Write your code here
'''print('Starting to make a coffee\nGrinding coffee beans'
      '\nBoiling water\nMixing boiled water with crushed coffee '
      'beans\nPouring coffee into the cup\nPouring some '
      'milk into the cup\nCoffee is ready!')

result = [water_c/water, milk_c/milk, beans_c/beans]
min_res = int((min(result)))

if min_res < cups:
      print("No, I can make only {} cup(s) of coffee".format(min_res))
elif min_res == cups:
      print("Yes, I can make that amount of coffee")
else:
      print("Yes, I can make that amount of coffee (and even {} "
            "more than that)".format(min_res-cups)) '''

coffee = {"machine": {"water": 1200, "milk": 540, "beans": 120, "cups": 9, "money": 550},
          "espresso": {"water": 250, "milk": 0, "beans": 16, "cups": 1, "price": 4},
          "latte": {"water": 350, "milk": 75, "beans": 20, "cups": 1, "price": 7},
          "cappuccino": {"water": 200, "milk": 100, "beans": 12, "cups": 1, "price": 6}}




def change_filling():
    pass

def remaining(water, milk, beans, cups, money):
    #change_filling(water, milk, beans, cups, money)
    return "The coffee machine has:\n{} of water\n{} of milk\n{} of coffee beans" \
                "\n{} of disposable cups\n{} of money".format(water, milk, beans, cups, money)


def espresso(water, milk, beans, cups, money):
    coffee["machine"]["water"] -= coffee["espresso"]["water"]
    coffee["machine"]["beans"] -= coffee["espresso"]["beans"]
    coffee["machine"]["milk"] -= coffee["espresso"]["milk"]
    coffee["machine"]["cups"] -= coffee["espresso"]["cups"]
    coffee["machine"]["money"] += coffee["espresso"]["price"]
    return water, beans, milk, cups, money


def latte(water, milk, beans, cups, money):
    coffee["machine"]["water"] -= coffee["latte"]["water"]
    coffee["machine"]["beans"] -= coffee["latte"]["beans"]
    coffee["machine"]["milk"] -= coffee["latte"]["milk"]
    coffee["machine"]["cups"] -= coffee["latte"]["cups"]
    coffee["machine"]["money"] += coffee["latte"]["price"]
    return water, beans, milk, cups, money


def cappuccino(water, milk, beans, cups, money):
    coffee["machine"]["water"] -= coffee["cappuccino"]["water"]
    coffee["machine"]["beans"] -= coffee["cappuccino"]["beans"]
    coffee["machine"]["milk"] -= coffee["cappuccino"]["milk"]
    coffee["machine"]["cups"] -= coffee["cappuccino"]["cups"]
    coffee["machine"]["money"] += coffee["cappuccino"]["price"]
    return water, beans, milk, cups, money


def buy(water, milk, beans, cups, money):
    buy = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n")
    print(buy)
    if buy == "1":
        espresso(water, milk, beans,cups, money)
    elif buy == "2":
        latte(water, milk, beans,cups, money)
    elif buy == "3":
        cappuccino(water, milk, beans,cups, money)


def fill(water, milk, beans,cups):
    water_fill= int(input("Write how many ml of water do you want to add:\n"))
    milk_fill = int(input("Write how many ml of milk do you want to add:\n"))
    beans_fill = int(input("Write how many grams of coffee beans do you want to add:\n"))
    cups_fill = int(input("Write how many disposable cups of coffee do you want to add:\n"))
    water += water_fill
    milk += milk_fill
    beans += beans_fill
    cups += cups_fill


def take(water, milk, beans, cups, money):
    print("I gave you ${}".format(money))
    money -= money


def back():
    pass


while True:
    water = coffee["machine"]["water"]
    milk = coffee["machine"]["milk"]
    beans = coffee["machine"]["beans"]
    cups = coffee["machine"]["cups"]
    money = coffee["machine"]["money"]

    action = input("Write action (buy, fill, take, remaining, exit):\n")

    if action == "buy":
        buy(water, milk, beans, cups, money)
        continue
    elif action == "fill":
        fill(water, milk, beans, cups)
        continue
    elif action == "take":
        take(water, milk, beans, cups, money)
        continue
    elif action == "remaining":
        print(remaining(water, milk, beans, cups, money))
        continue
    elif action == "back":
        back()
    elif action == "exit":
        break
