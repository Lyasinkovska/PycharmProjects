import random


def card_number_generation():

	random.seed(random.random())
	iin = "400000"
	init_card_number = iin + str(random.sample(range(100000000, 999999999), 1)[0])
	#print(init_card_number)

	odd_digits = [int(digit) * 2 for digit in init_card_number[::2]]
	even_digits = [int(digit) for digit in init_card_number[1::2]]
	luhn_card_1 = odd_digits + even_digits

	luhn_card_2 = [(digit - 9) if digit >= 9 else digit for digit in luhn_card_1]
	#print(sum(luhn_card_2), (sum(luhn_card_2)//10+1)*10)
	if sum(luhn_card_2)%10 == 0:
		last_digit = 0
	else:
		last_digit = (sum(luhn_card_2)//10+1)*10 - sum(luhn_card_2)
	return int(init_card_number + str(last_digit))




print(card_number_generation())

