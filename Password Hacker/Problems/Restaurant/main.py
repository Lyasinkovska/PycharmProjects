import itertools

menu = zip(itertools.product(main_courses, desserts, drinks), itertools.product(price_main_courses,price_desserts,price_drinks))
for dish, price in menu:
	if sum(price) <= 30:
		print(*dish, sum(price))