names = []
values = []
while True:
	cafe = input()
	if cafe == "MEOW":
		break
	else:
		name, value = cafe.split()
		names.append(name)
		values.append(int(value))
print(names[values.index(max(values))])
