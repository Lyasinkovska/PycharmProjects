# Write your code here
import random


def menu():
	print("1. Create an account\n2. Log into account\n0. Exit")
	choice = int(input())
	return choice

def balance():
	balance = 0
	return f"Balance: {balance}"

def choice():
	choice = menu()
	card_number = card_number_generation()
	pin = pin_generation()
	if choice == 1:
		return account_creation(card_number, pin)
	elif choice == 2:
		print(card_number, pin)
		card_number_verification = int(input("Enter your card number:\n"))
		pin_verification = int(input("Enter your PIN:\n"))

		if card_number_verification == card_number and pin_verification == pin:
			print("You have successfully logged in!")
			print("1. Balance\n2. Log out\n0. Exit")
			return balance()
		else:
			return "Wrong card number or PIN!"
	#elif choice == 0:


def account_creation(card_number, pin):
	return "Your card has been created\nYour card number:\n{}\nYour card PIN:\n{}".format(card_number, pin)


def card_number_generation():
	random.seed()
	iin = "400000"
	card_number = int(iin + str(random.randint(0000000000, 9999999999)))
	return card_number


def pin_generation():
	random.seed()
	pin = random.randint(0000, 9999)
	return pin


while True:
	print(choice())
