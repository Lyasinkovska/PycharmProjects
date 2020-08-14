#  Posted from EduTools plugin
farm = {"chicken": 23, "goat": 678, "pig": 1296, "cow": 3848, "sheep": 6769}
money = int(input())
affordable_animal = {}
for animal, price in sorted(farm.items(), key=lambda key: key[1], reverse=True):
	if money < min(farm.values()):
		print(None)
		break
	elif money >= price:
		if money // price > 1 and animal != "sheep":
			print(money // price, animal + "s")
		else:
			print(money // price, animal)
		break

	else:

		continue
