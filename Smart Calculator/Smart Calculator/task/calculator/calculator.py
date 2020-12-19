from collections import deque


def calculator():
	data = dict()
	while True:
		user_input = input()
		if user_input == "":
			continue
		elif user_input.startswith("/"):
			commands_check(user_input)
		elif "=" in user_input:
			data_assignment(user_input, data)
		elif len(user_input.split()) == 1:
			check_variable(user_input, data)
		elif "**" in user_input or "***" in user_input or "****" in user_input or "*****" in user_input:
			print("Invalid expression")
		elif "//" in user_input or "///" in user_input or "////" in user_input or "/////" in user_input:
			print("Invalid expression")
		elif "(" in user_input or ")" in user_input:
			if brackets_check(user_input):
				input_list = [replacement(number.strip(), data) for number in user_input.split()]
				# print(input_list)
				calculations(input_list)
		else:
			input_list = [replacement(number.strip(), data) for number in user_input.split()]
			#print(input_list)
			calculations(input_list)


def check_variable(user_input, data):
	if user_input in data.keys():
		print(data.get(user_input))
	else:
		print("Unknown variable")


def data_assignment(user_input, data):
	key = user_input.split("=", 1)[0].strip()
	value = user_input.split("=", 1)[1].strip()
	if not key.isalpha():
		print("Invalid identifier")
	if value.isnumeric():
		data[key] = int(value)
	else:
		if value in data.keys():
			data[key] = data.get(value)
		else:
			print("Invalid assignment")


def commands_check(user_input):
	if user_input.strip("/") == "help":
		print('The program evaluates the sum of numbers.')
	elif user_input.strip("/") == "exit":
		print("Bye!")
		exit()
	else:
		print("Unknown command")


def replacement(element, data):
	if element in data.keys():
		return str(data.get(element))
	elif element == "+++" or element == len(element)*"+":
		return "+"
	elif element == len(element)*"-" and len(element) % 2 == 0:
		return "+"
	elif element == len(element)*"-" and len(element) % 2 != 0:
		return "-"

	else:
		return element


def operations(operator, number2, number1):
	if operator == "+":
		return number1 + number2
	elif operator == "-":
		return number1 - number2
	elif operator == "*":
		return number1 * number2
	elif operator == "/":
		return round(number1 / number2)


def infix_postfix(stack, operators, input_list):
	result = list()
	for i in range(len(input_list)):
		if input_list[i].isnumeric():
			result.append(input_list[i])
		elif "(" in input_list[i]:
			result.append(input_list[i].strip("("))
		elif ")" in input_list[i]:
			result.append(input_list[i].strip(")"))
		elif input_list[i] in operators.keys():
			if stack == deque():
				stack.append(input_list[i])
			elif "(" in input_list[i-1]:
				stack.append(input_list[i])
			elif operators[stack[-1]] < operators[input_list[i]]:
				stack.append(input_list[i])
			elif operators[stack[-1]] >= operators[input_list[i]]:
				while len(stack) > 0:
					result.append(stack.pop())
				stack.append(input_list[i])
	while len(stack) > 0:
		result.append(stack.pop())
	#print(result)
	return result


def postfix_result(stack, postfix_list, operators):
	for elem in postfix_list:
		if elem.isnumeric():
			stack.append(int(elem))
		elif elem in operators.keys():
			new_elem = operations(elem, stack.pop(), stack.pop())
			stack.append(new_elem)

	print(stack[0])


def brackets_check(string):
	brackets = deque()
	for element in string:
		if "(" in element:
			brackets.appendleft("(")
		elif ")" in element:
			if len(brackets) > 0:
				brackets.pop()
			else:
				print("Invalid expression")

	if len(brackets) == 0:
		return True
	else:
		print("Invalid expression")


def calculations(input_list):
	operators = {"-": False, "+": False, "*": True, "/": True}
	stack = deque()
	result = infix_postfix(stack, operators, input_list)
	postfix_result(stack, result, operators)


def check_operator(element):
	if element == len(element)*"*" and len(element) > 1:
		return "Invalid expression"
	elif element == len(element)*"/" and len(element) > 1:
		return "Invalid expression"

calculator()
