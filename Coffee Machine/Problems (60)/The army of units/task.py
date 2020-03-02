number = int(input())
if number < 1:
	print("no army")
elif 1 <= number <= 9:
	print("few")
elif 10 <= number <= 49:
	print("pack")
elif 50 <= number <= 499:
	print("horde")
elif 500 <= number <= 999:
	print("swarm")
elif number >= 1000:
	print("legion")