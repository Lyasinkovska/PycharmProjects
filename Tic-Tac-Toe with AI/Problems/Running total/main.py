numbers = [int(elem) for elem in input()]
new_l = []
for i in range(len(numbers)):
	new_l.insert(0, sum(numbers))
	numbers.pop()
print(new_l)