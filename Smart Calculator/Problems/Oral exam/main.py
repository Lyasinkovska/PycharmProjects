from collections import deque

students = deque()
for i in range(int(input())):
	command = input()
	if command.split()[0] == "READY":
		students.append(command.split()[1])
	elif command.split()[0] == "EXTRA":
		students.append(students.popleft())
	else:
		print(students.popleft())

