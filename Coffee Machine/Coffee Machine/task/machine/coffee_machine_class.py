class CoffeeMachine:
	initial_resources = {
		"water": 400, "milk": 540, "beans": 120, "cups": 9, "money": 550
	}

	coffee_ingredients_needed = {
		"espresso": {"water": 250, "milk": 0, "beans": 16, "cups": 1, "price": 4},
		"latte": {"water": 350, "milk": 75, "beans": 20, "cups": 1, "price": 7},
		"cappuccino": {"water": 200, "milk": 100, "beans": 12, "cups": 1, "price": 6}
	}

	def __init__(self):
		self.water = self.initial_resources["water"]
		self.milk = self.initial_resources["milk"]
		self.beans = self.initial_resources["beans"]
		self.cups = self.initial_resources["cups"]
		self.money = self.initial_resources["money"]
		self.state = "choosing an action"
		self.make_coffee()

	def remaining(self, water, milk, beans, cups, money):
		return "The coffee machine has:\n{} of water\n{} of milk\n{} of coffee beans" \
			"\n{} of disposable cups\n{} of money".format(water, milk, beans, cups, money)

	def resources(self, kind):
		if self.initial_resources["water"] < self.coffee_ingredients_needed[kind]["water"]:
			print("Sorry, not enough water!")
		elif self.initial_resources["beans"] < self.coffee_ingredients_needed[kind]["beans"]:
			print("Sorry, not enough coffee beans!")
		elif self.initial_resources["milk"] < self.coffee_ingredients_needed[kind]["milk"]:
			print("Sorry, not enough milk!")
		elif self.initial_resources["cups"] < self.coffee_ingredients_needed[kind]["cups"]:
			print("Sorry, not enough disposable cups!")
		else:
			print("I have enough resources, making you a coffee!")
			self.initial_resources["water"] -= self.coffee_ingredients_needed[kind]["water"]
			self.initial_resources["beans"] -= self.coffee_ingredients_needed[kind]["beans"]
			self.initial_resources["milk"] -= self.coffee_ingredients_needed[kind]["milk"]
			self.initial_resources["cups"] -= self.coffee_ingredients_needed[kind]["cups"]
			self.initial_resources["money"] += self.coffee_ingredients_needed[kind]["price"]

	def buy(self, kind, action):
		kind = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, 4 - go back:\n")
		if kind == "1":
			self.resources("espresso")
		elif kind == "2":
			self.resources("latte")
		elif kind == "3":
			self.resources("cappuccino")
		elif kind == "4":
			self.make_coffee(action)

	def fill(self, water, milk, beans, cups):
		# water = int(input("Write how many ml of water do you want to add:\n"))
		# milk = int(input("Write how many ml of milk do you want to add:\n"))
		# beans = int(input("Write how many grams of coffee beans do you want to add:\n"))
		# cups = int(input("Write how many disposable cups of coffee do you want to add:\n"))
		self.initial_resources["water"] += water
		self.initial_resources["milk"] += milk
		self.initial_resources["beans"] += beans
		self.initial_resources["cups"] += cups

	def take(self, money):
		print("I gave you ${}".format(money))
		self.initial_resources["money"] -= money

	def user_input(self, action):
		return action

	def make_coffee(self, action):
		while True:
			# self.action = input("Write action (buy, fill, take, remaining, exit):\n")
			if action == "buy":
				self.buy(action)
				continue
			elif action == "fill":
				self.fill()
				continue
			elif action == "take":
				self.take(self.money)
				continue
			elif action == "remaining":
				print(self.remaining(self.water, self.milk, self.beans, self.cups, self.money))
				continue
			elif action == "exit":
				break


my_coffee = CoffeeMachine
my_coffee.make_coffee("buy")
