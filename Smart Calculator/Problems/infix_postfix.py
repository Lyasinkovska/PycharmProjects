from collections import deque


var = "10 + 2 * 8 - 3 * ( 4 - 4 )" # 10 2 8 * + 3 -
#var = "10 + 2 - 8 + 3"  # 10 2 + 8 – 3 +

def operations(operator, number2, number1):
	if operator == "+":
		return number1 + number2
	elif operator == "-":
		return number1 - number2
	elif operator == "*":
		return number1 * number2
	elif operator == "/":
		return number1 / number2


def infix_postfix(stack, operators):
	result = list()
	for elem in var.split():
		if elem.isnumeric():
			result.append(elem)
		elif elem in operators.keys():
			if stack == deque():
				stack.append(elem)
			elif operators[stack[-1]] < operators[elem]:
				stack.append(elem)
			else:
				while len(stack) > 0 and operators[stack[-1]] >= operators[elem]:
					result.append(stack.pop())
				stack.append(elem)
	result.append(stack.pop())
	print(result)
	return result


def postfix_result(stack, postfix_list, operators):
	for elem in postfix_list:
		if elem.isnumeric():
			stack.append(int(elem))
		elif elem in operators.keys():
			new_elem = operations(elem, stack.pop(), stack.pop())
			stack.append(new_elem)
	print(stack[0])


def calculations():
	operators = {"-": False, "+": False, "*": True, "/": True}
	stack = deque()
	result = infix_postfix(stack, operators)
	postfix_result(stack, result, operators)


calculations()

