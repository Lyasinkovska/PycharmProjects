column = int(input())
row = int(input())
if column == 1:
	if row == 1 or row == 8:
		print(3)
	else:
		print(5)
elif column == 8:
	if row == 1:
		print(3)
	elif row == 8:
		print(3)
	else:
		print(5)
elif row == 1:
	if column == 1 or column == 8:
		print(3)
	else:
		print(5)
elif row == 8:
	if column == 1 or column == 8:
		print(3)
	else:
		print(5)
else:
	print(8)
