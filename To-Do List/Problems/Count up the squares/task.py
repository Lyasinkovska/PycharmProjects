zero_sum = 0
square_sum = 0
while True:
	line = input()
	if line.strip("-").isnumeric():
		zero_sum += int(line)
		square_sum += int(line)**2
		if zero_sum == 0:
			print(square_sum)
			break
		else:
			continue
	else:
		break
