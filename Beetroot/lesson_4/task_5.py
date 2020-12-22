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
