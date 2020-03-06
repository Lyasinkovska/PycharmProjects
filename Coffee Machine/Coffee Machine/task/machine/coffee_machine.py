class CoffeeMachine:

    def __init__(self):
        self.coffee_ingredients_needed = {
            "espresso": {"water": 250, "milk": 0, "beans": 16, "cups": 1, "money": 4},
            "latte": {"water": 350, "milk": 75, "beans": 20, "cups": 1, "money": 7},
            "cappuccino": {"water": 200, "milk": 100, "beans": 12, "cups": 1, "money": 6}
        }

        self.machine_money = 550

        self.machine_resources = {
            "water": 400, "milk": 540, "beans": 120, "cups": 9
        }
        self.make_coffee()

    def remaining(self):
        print("The coffee machine has:\n{} of water\n{} of milk\n{} of coffee beans\n{} of disposable cups\n"
              "{} of money".format(self.machine_resources["water"],
                                   self.machine_resources["milk"],
                                   self.machine_resources["beans"],
                                   self.machine_resources["cups"],
                                   self.machine_money))

    def check_if_enough_resources(self, coffee_variant):
        is_enough_x`resources = True
        for ingredient in self.machine_resources.keys():
            if self.machine_resources[ingredient] < self.coffee_ingredients_needed[coffee_variant][ingredient]:
                is_enough_resources = False
                print("Sorry, not enough {}!".format(ingredient))
        return is_enough_resources

    def decrease_resources(self, coffee_variant):
        for ingredient in self.machine_resources.keys():
            self.machine_resources[ingredient] -= self.coffee_ingredients_needed[coffee_variant][ingredient]

    def resources(self, coffee_variant):
        if self.check_if_enough_resources(coffee_variant):
            print("I have enough resources, making you a coffee!")
            self.decrease_resources(coffee_variant)
            self.machine_money += self.coffee_ingredients_needed[coffee_variant]["money"]

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
        self.machine_resources["water"] += int(self.ask_user("Write how many ml of water do you want to add:\n"))
        self.machine_resources["milk"] += int(self.ask_user("Write how many ml of milk do you want to add:\n"))
        self.machine_resources["beans"] += int(self.ask_user("Write how many grams of coffee beans do you want "
                                                             "to add:\n"))
        self.machine_resources["cups"] += int(self.ask_user("Write how many disposable cups of coffee do you want "
                                                            "to add:\n"))

    def take(self):
        print("I gave you ${}".format(self.machine_money))
        self.machine_money = 0

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
                self.take()
                continue
            elif action == "remaining":
                self.remaining()
                continue
            elif action == "exit":
                break


my_coffee = CoffeeMachine()
