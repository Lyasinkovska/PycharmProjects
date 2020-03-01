income = int(input())
percent = 0
if 0 <= income <= 15527:
	percent = 0
elif 15528 <= income <= 42707:
	percent = 15
elif 42708 <= income <= 85414:
	percent = 22
elif 85415 <= income <= 132406:
	percent = 26
elif income >= 132407:
	percent = 28
print(f"The tax for {income} is {percent}%. That is {percent * income / 100:.2f} dollars!")
