"""task 1
Получить от пользователя его номер телефона, проверить подходит ли номер под форматы
+380_________ (прочерки - любая цифра)
0_________ (например 0931233232)
0__ ___ __ __ (пробелы именно пробелы и телефон например 095 321 12 21)
Если номер введен верно - похвалите человека. Если нет - поругайте."""
test_numbers = ["+380986455862", "0986455862", "098 645 5862", "098645 58_62",
				"098 645  862", "098 645__662", "098 645 b862", "325 698 55 66"]

while True:
	number = input("Please, enter your phone number in the following format:\n"
				   "+380_________, 0_________, 0__ ___ __ __ (where '_' is a digit)\n>")

	if number.startswith("+380"):
		number = number.strip("+380")
	elif number.startswith("0"):
		number = number[1:].replace(" ", "")

	if number.isnumeric() and len(number) == 9:
		print("The number is correct.")
		break
	else:
		print("The number format is wrong. Please try again.")

"""задание 3
проверить что введенная строка является полиндромом."""
word = input()
if word == word[::-1]:
	print("It is a palindrome.")
else:
	print("It is not a palindrome. ")


"""Задание (із зірочкой):
Задание 2 пример по математике просто решить глядя в код, а что если переменную инициализировать случайным значением?
В первой строке импортируйте модуль рандома
import random
обьявите переменные (случайное целое от 1 до 20 включительно)
var1 = random.randint(1,20)
Теперь сделайте задание 2 но уже со случайными значениями.
"""