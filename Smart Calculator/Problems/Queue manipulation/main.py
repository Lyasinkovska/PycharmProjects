from collections import deque

n = int(input())
qu = deque()
for i in range(n):
	command = input()
	if command == "DEQUEUE":
		qu.popleft()
	else:
		qu.append(command.split()[1])
for el in qu:
	print(el)