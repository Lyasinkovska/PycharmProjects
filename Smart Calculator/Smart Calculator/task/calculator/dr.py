# write your code here
def replacement(element):
	if element == "+++" or element == len(element)*"+":
		return "+"
	elif element == len(element)*"-" and len(element) % 2 == 0:
		return "+"
	elif element == len(element)*"-" and len(element) % 2 != 0:
		return "-"
	else:
		return element


def sum_of_elements(list_of_elements):
	new_numb = [list_of_elements[0]]
	for i in range(1, len(list_of_elements), 2):
		new_numb.append(list_of_elements[i] + list_of_elements[i + 1])
	return sum([int(numb) for numb in new_numb])


def check_command(user_input):
	if user_input == "/help":
		print('The program evaluates the sum of numbers.')
	elif user_input == "/exit":
		print("Bye!")
		exit()
	else:
		print("Unknown command")


def exceptions(user_input):
	if len (user_input) == 1:
		if user_input[0] == "-":
			print (user_input)
		elif user_input[0] == "+":
			print (user_input.lstrip ("+"))
		elif user_input[-1] == "+" or user_input[-1] == "-" or user_input.isalpha():
			print ("Invalid expression")
	elif "+" or "-" not in user_input.split ():
		print ("Invalid expression")
	elif any (user_input.split().isalpha()):
		print ("Invalid expression")


def data_dictionary(user_input, input_data):
	if check_variable(user_input):
		if check_value(user_input, input_data):
			input_data[user_input.split("=", 1)[0].strip()] = int(check_value(user_input, input_data))
		else:
			print("Invalid assignment")


def data_return(user_input, input_data):
	if user_input.strip() in input_data.keys():
		print(input_data[user_input.strip()])
	else:
		print("Unknown variable")


def check_variable(user_input):
	if user_input.split("=", 1)[0].strip().isalpha():
		return True
	else:
		print("Invalid identifier")


def check_value(user_input, input_data):
	if user_input.split("=", 1)[1].strip().isnumeric():
		return user_input.split("=", 1)[1].strip()
	elif user_input.split("=")[1].strip() in input_data.keys():
		return input_data.get(user_input.split("=", 1)[1].strip())


def check_expression(user_input, input_data):
	try:
		# print(sum_of_elements([replacement(number) for number in user_input.split()]))
		if "=" in user_input:
			data_dictionary(user_input, input_data)

		else:
			data_return(user_input, input_data)
	except:
		exceptions(user_input)


def calculator():
	input_data = dict()
	while True:
		user_input = input()
		if user_input.startswith("/"):
			check_command(user_input)
		elif user_input == "":
			continue
		else:
			check_expression(user_input, input_data)


calculator()
