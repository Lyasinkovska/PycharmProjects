# put your python code here
from collections import deque

string = input()


def brackets_check(string):
	brackets = deque()
	for element in string:
		if element == "(":
			brackets.appendleft(element)
		elif element == ")":
			if len(brackets) > 0:
				brackets.pop()
			else:
				return "ERROR"

	if len(brackets) == 0:
		return "OK"
	else:
		return "ERROR"


print(brackets_check(string))