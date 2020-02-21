# Write your code here
'''print('Starting to make a coffee\nGrinding coffee beans'
      '\nBoiling water\nMixing boiled water with crushed coffee '
      'beans\nPouring coffee into the cup\nPouring some '
      'milk into the cup\nCoffee is ready!')

water = 200
milk = 50
beans = 15

water_c = int(input("Write how many ml of water the coffee machine has:\n"))
milk_c = int(input("Write how many ml of milk the coffee machine has:\n"))
beans_c = int(input("Write how many grams of coffee beans the coffee machine has:\n"))
cups = int(input("Write how many cups of coffee you will need:\n"))

result = [water_c/water, milk_c/milk, beans_c/beans]
min_res = int((min(result)))

if min_res < cups:
      print("No, I can make only {} cup(s) of coffee".format(min_res))
elif min_res == cups:
      print("Yes, I can make that amount of coffee")
else:
      print("Yes, I can make that amount of coffee (and even {} "
            "more than that)".format(min_res-cups))'''

coffee = {"machine": {"water": 1200, "milk": 540, "beans": 120, "cups": 9, "money": 550},
          "espresso": {"water": 250, "beans": 16, "cups": 1, "price": 4},
          "latte": {"water": 350, "milk": 75, "beans": 20, "cups": 1, "price": 7},
          "cappuccino": {"water": 200, "milk": 100, "beans": 12, "cups": 1, "price": 6}}

water = coffee["machine"]["water"]
milk = coffee["machine"]["milk"]
beans = coffee["machine"]["beans"]
cups = coffee["machine"]["cups"]
money = coffee["machine"]["money"]

machine_state = "The coffee machine has:\n{} of water\n{} of milk\n{} of coffee beans" \
                "\n{} of disposable cups\n{} of money".format(water, milk, beans, cups, money)

print(machine_state)
action = input("Write action (buy, fill, take): ")

if action == "buy":
    buy = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: ")
    print(buy)
    if buy == "1":
        water -= coffee["espresso"]["water"]
        beans -= coffee["espresso"]["beans"]
        cups -= coffee["espresso"]["cups"]
        money += coffee["espresso"]["price"]

