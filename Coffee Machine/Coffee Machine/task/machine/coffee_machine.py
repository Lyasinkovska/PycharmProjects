# Write your code here
'''print('Starting to make a coffee\nGrinding coffee beans'
      '\nBoiling water\nMixing boiled water with crushed coffee '
      'beans\nPouring coffee into the cup\nPouring some '
      'milk into the cup\nCoffee is ready!')

water = 200
milk = 50
beans = 15

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

water = coffee["machine"]["water"]
milk = coffee["machine"]["milk"]
beans = coffee["machine"]["beans"]
cups = coffee["machine"]["cups"]
money = coffee["machine"]["money"]


def machine_state(water = water, milk = milk, beans = beans, cups=cups, money = money):
    return "The coffee machine has:\n{} of water\n{} of milk\n{} of coffee beans" \
                "\n{} of disposable cups\n{} of money".format(water, milk, beans, cups, money)


def buy(water, milk, beans,cups, money):
    buy = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n")
    print(buy)
    if buy == "1":
        water -= coffee["espresso"]["water"]
        beans -= coffee["espresso"]["beans"]
        milk -= coffee["espresso"]["milk"]
        cups -= coffee["espresso"]["cups"]
        money += coffee["espresso"]["price"]
        print(machine_state(water, milk, beans, cups, money))
    elif buy == "2":
        water -= coffee["latte"]["water"]
        beans -= coffee["latte"]["beans"]
        milk -= coffee["latte"]["milk"]
        cups -= coffee["latte"]["cups"]
        money += coffee["latte"]["price"]
        print(machine_state(water, milk, beans, cups, money))
    elif buy == "3":
        water -= coffee["cappuccino"]["water"]
        beans -= coffee["cappuccino"]["beans"]
        milk -= coffee["cappuccino"]["milk"]
        cups -= coffee["cappuccino"]["cups"]
        money += coffee["cappuccino"]["price"]
        print(machine_state(water, milk, beans, cups, money))


def fill(water, milk, beans, cups, money = money):
    water_fill= int(input("Write how many ml of water do you want to add:\n"))
    milk_fill = int(input("Write how many ml of milk do you want to add:\n"))
    beans_fill = int(input("Write how many grams of coffee beans do you want to add:\n"))
    cups_fill = int(input("Write how many disposable cups of coffee do you want to add:\n"))
    water += water_fill
    milk += milk_fill
    beans += beans_fill
    cups += cups_fill
    print(machine_state(water, milk, beans, cups, money))

def take(water, milk, beans, cups, money):
    print("I gave you ${}".format(money))
    money -= money
    print(machine_state(water, milk, beans, cups, money))

print(machine_state())

action = input("Write action (buy, fill, take):\n")

if action == "buy":
    buy(water, milk, beans, cups, money)
elif action == "fill":
    fill(water, milk, beans, cups, money)
elif action == "take":
    take(water, milk, beans, cups, money)
