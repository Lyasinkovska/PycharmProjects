import random

"""task 1
За 10 попыток получить максимальное рендомное число. 
Количество попыток запрашивать у пользователя."""

while True:
	try:
		max_attempts = int(input("Enter quantity of attempts: "))
		start = int(input("Enter min number: "))
		stop = int(input("Enter max number: "))
		result = None
		while max_attempts > 0:
			number = random.randint(start, stop)
			if result is None or result < number:
				result = number
			max_attempts -= 1
		print(result)
		break
	except ValueError:
		print("You should enter a number!")

"""task 2
написать цикл получения строки по определенному формату (число) 
пока не введет число и мучаем его"""

attempts = 5
while attempts > 0:
	valid_number = input()  # "+38 (098) 614 45 86"
	space_pos = [i for i, symbol in enumerate(valid_number) if symbol == " "]

	if len(valid_number) == 19 and valid_number.startswith("+38") and valid_number.find("(") == 4 and \
		valid_number.find(")") == 8 and valid_number[5] == "0" and space_pos == [3, 9, 13, 16]:
		valid_number = valid_number.strip("+38").replace("(", "").replace(")", "").replace(" ", "")

	if valid_number.isnumeric():
		print("Valid number")
		break
	else:
		attempts -= 1
		print("Invalid number, try again" if attempts > 0 else "No more attempts")

"""task 3
получить от пользователя 10 чисел и вывести максимальное
"""
attempts = 10
max_number = None
while attempts > 0:
	try:
		number = int(input("Enter any number: "))
		if max_number is None or max_number < number:
			max_number = number
		attempts -= 1
	except ValueError:
		print("You should enter a numerical value!")
print(max_number)

""" task 4
получаем в цикле 
число
действие
второе число
пишем промежутчный результат
запрашиваем действие 
и снова число
действие...
если вместо числа или действия введено Q выходим"""


def add(a, b):
	return a + b


def subtract(a, b):
	return a - b


def multiply(a, b):
	return a * b


def get_number():
	while True:
		user_input = input("Enter number: ")
		if user_input.isnumeric():
			return int(user_input)
		elif user_input == "Q":
			print("Good bye.")
			quit()
		else:
			print("Wrong number format.")
			continue


actions = {"+": add, "-": subtract, "*": multiply}
total = get_number()

while True:
	action = input("Enter action: ")
	if action == "Q":
		print("Good bye.")
		quit()
	elif action not in actions.keys():
		print("Wrong action.")
		continue
	else:
		number = get_number()
		total = actions[action](total, number)
		print(f"The result is: {total}. If you want to quit enter Q.")
