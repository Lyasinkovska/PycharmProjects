n = int(input())
operations = list()
for i in range(n):
	operation = input()
	if operation.split()[0] == "PUSH":
		operations.append(int(operation.split()[1]))
	else:
		operations.pop()
while len(operations) > 0:
	print(operations.pop())
