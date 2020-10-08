a = int(input())
b = int(input())
h = int(input())
if a <= h <= b:
	print('Normal')
elif h > b:
	print("Excess")
else:
	print("Deficiency")