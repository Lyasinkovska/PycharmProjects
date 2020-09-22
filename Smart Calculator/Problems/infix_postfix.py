from collections import deque


var = "8 * 3 + 12 * ( 4 - 2 )".split() # 23
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
	for elem in var:
		if elem.isnumeric():
			result.append(elem)
		elif elem == "(":
			operators["+"] = True
			operators["-"] = True
		elif elem == ")":
			operators["+"] = False
			operators["-"] = False
		elif elem in operators.keys():
			if stack == deque():
				stack.append(elem)
			elif operators[stack[-1]] < operators[elem]:
				stack.append(elem)
			elif operators[stack[-1]] == operators[elem]:
				stack.append(elem)
			elif operators[stack[-1]] > operators[elem]:
				while len(stack) > 0:
					result.append(stack.pop())
				stack.append(elem)
	while len(stack) > 0:
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


def brackets_check(string):
	brackets = deque()
	for element in string:
		if element == "(":
			brackets.appendleft(element)
		elif element == ")":
			if len(brackets) > 0:
				brackets.pop()
			else:
				return False

	if len(brackets) == 0:
		return True
	else:
		return False


def calculations():
	operators = {"-": False, "+": False, "*": True, "/": True}
	stack = deque()
	result = infix_postfix(stack, operators)
	postfix_result(stack, result, operators)


calculations()

