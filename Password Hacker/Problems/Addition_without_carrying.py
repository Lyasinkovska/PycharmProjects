#For param1 = 456 and param2 = 1734, the output should be
#additionWithoutCarrying(param1, param2) = 1180.

def additionWithoutCarrying(param1, param2):
	param1, param2 = map(str, (param1, param2))
	result = []
	for n1, n2 in zip(param1[::-1], param2[::-1]):
		result.append(str(int(n1) + int(n2))[-1])

	if len(param1) > len(param2):
		diff = len(param1) - len(param2)
		result.append(param1[0:diff])
	elif len(param1) < len(param2):
		diff = len(param2) - len(param1)
		result.append(param2[0:diff])
	return int(''.join(result[::-1]))

print(additionWithoutCarrying(99999, 0))