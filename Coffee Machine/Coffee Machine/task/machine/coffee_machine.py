class CoffeeMachine:
    coffee_ingredients_needed = {
        "espresso": {"water": 250, "milk": 0, "beans": 16, "cups": 1, "price": 4},
        "latte": {"water": 350, "milk": 75, "beans": 20, "cups": 1, "price": 7},
        "cappuccino": {"water": 200, "milk": 100, "beans": 12, "cups": 1, "price": 6}
    }

    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550
        self.make_coffee()

    def remaining(self):
        print(f"The coffee machine has:\n{self.water} of water\n{self.milk} of milk\n{self.beans} of coffee beans" \
               f"\n{self.cups} of disposable cups\n{self.money} of money")

    def resources(self, variant):
        if self.water < self.coffee_ingredients_needed[variant]["water"]:
            print("Sorry, not enough water!")
        elif self.beans < self.coffee_ingredients_needed[variant]["beans"]:
            print("Sorry, not enough coffee beans!")
        elif self.milk < self.coffee_ingredients_needed[variant]["milk"]:
            print("Sorry, not enough milk!")
        elif self.cups < self.coffee_ingredients_needed[variant]["cups"]:
            print("Sorry, not enough disposable cups!")
        else:
            print("I have enough resources, making you a coffee!")
            self.water -= self.coffee_ingredients_needed[variant]["water"]
            self.beans -= self.coffee_ingredients_needed[variant]["beans"]
            self.milk -= self.coffee_ingredients_needed[variant]["milk"]
            self.cups -= self.coffee_ingredients_needed[variant]["cups"]
            self.money += self.coffee_ingredients_needed[variant]["price"]

    def buy(self):
        variant = self.ask_user("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, 4 - go back:\n")
        if variant == "1":
            self.resources("espresso")
        elif variant == "2":
            self.resources("latte")
        elif variant == "3":
            self.resources("cappuccino")
        elif variant == "4":
            self.make_coffee()

    def fill(self):
        self.water += int(self.ask_user("Write how many ml of water do you want to add:\n"))
        self.milk += int(self.ask_user("Write how many ml of milk do you want to add:\n"))
        self.beans += int(self.ask_user("Write how many grams of coffee beans do you want to add:\n"))
        self.cups += int(self.ask_user("Write how many disposable cups of coffee do you want to add:\n"))

    def take(self, money):
        print("I gave you ${}".format(money))
        self.money -= money

    def ask_user(self, action):
        return input(action)

    def make_coffee(self):
        while True:
            action = self.ask_user("Write action (buy, fill, take, remaining, exit):\n")
            if action == "buy":
                self.buy()
                continue
            elif action == "fill":
                self.fill()
                continue
            elif action == "take":
                self.take(self.money)
                continue
            elif action == "remaining":
                self.remaining()
                continue
            elif action == "exit":
                break


my_coffee = CoffeeMachine()