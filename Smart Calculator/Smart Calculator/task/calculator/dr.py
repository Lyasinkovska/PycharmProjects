from collections import deque


class Calculator:

	def __init__(self):
		self.data = dict()
		self.user_input = input("Enter a string:\n")
		self.infix_stack = list()
		self.postfix_stack = deque()
		self.exceptions = {1: "Invalid expression", 2: "Unknown variable", 3: "Invalid assignment",
						   4: 'Unknown command', 5: "Invalid identifier"}
		self.check_exceptions(self.user_input)

	def check_command(self, user_input):
		if user_input.strip("/") == "help":
			print('The program evaluates the expression.')
		elif user_input.strip("/") == "exit":
			print("Bye!")
			exit()
		else:
			print(self.exceptions[4])

	def check_brackets(self, user_input):
		brackets = deque()
		for element in user_input:
			if "(" in element:
				brackets.appendleft("(")
			elif ")" in element:
				if len(brackets) > 0:
					brackets.pop()
				else:
					print(self.exceptions[1])

	def check_operator(self, user_input):
		for element in user_input.split():
			if element == len(element) * "*" and len(element) > 1:
				print(self.exceptions[1])
			elif element == len(element) * "/" and len(element) > 1:
				print(self.exceptions[1])

	def check_exceptions(self, user_input):
		if user_input.startswith("/"):
			self.check_command(user_input)
		elif "(" in user_input or ")" in user_input:
			self.check_brackets(user_input)
		else:
			self.check_operator(user_input)


calculator = Calculator()
