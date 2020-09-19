n = int(input())

my_stack = list()
while len(my_stack) < n:
	my_stack.append(input())
while len(my_stack) > 0:
	print(my_stack.pop())