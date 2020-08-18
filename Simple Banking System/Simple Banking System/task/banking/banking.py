import random


class CardCredentials:

	def __init__(self, card_number, pin):
		self.card_number = card_number
		self.pin = pin


class Account:

	def __init__(self):
		self.menu = ["1. Create an account\n2. Log into account\n0. Exit\n","1. Balance\n2. Log out\n0. Exit\n"]
		self.credentials = dict()
		self.choice()


	def user_choice(self, action):
		return int(input(action))

	def credentials(self):
		self.credentials[self.card_number] = self.pin
		print()

	def card_number_generation(self):
		random.seed(random.random())
		iin = "400000"
		self.card_number = int(iin + str(random.sample(range(00000000000, 99999999999),1)[0]))
		return self.card_number

	def pin_generation(self):
		random.seed(random.random())
		self.pin = random.sample(range(0000, 9999),1)[0]
		return self.pin

	def add_credentials(self):
		self.credentials[self.card_number] = self.pin


	def account_creation(self):
		self.card_number = self.card_number_generation()
		self.pin = self.pin_generation()

		print("Your card has been created\nYour card number:\n{}\nYour card PIN:\n{}"\
			.format(self.card_number, self.pin))

	def log_in(self):
		self.input_card_number = self.user_choice("Enter your card number:\n")
		self.input_pin = self.user_choice("Enter your PIN:\n")
		self.verification()

	def balance(self):
		self.balance = 0
		print(f"Balance: {self.balance}\n")

	def verification(self):

		if self.input_pin in self.credentials.values(): #and self.credentials[self.input_card_number] == self.input_pin:
			print("You have successfully logged in!\n")
			while True:
				action = self.user_choice(self.menu[1])
				if action == 1:
					self.balance()
					continue
				elif action == 2:
					print("You have successfully logged out!\n")
					break
				elif action == 0:
					print("Bye!")
					exit()
		else:

			print("Wrong card number or PIN!\n")

	def choice(self):
		while True:
			action = self.user_choice(self.menu[0])

			if action == 1:
				self.account_creation()
				self.add_credentials()
				print(self.credentials)

			elif action == 2:
				self.log_in()

			elif action == 0:
				exit()


my_account = Account()
