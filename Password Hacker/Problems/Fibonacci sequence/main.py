def fibonacci(n):
	a, b = 0, 1
	counter = 0
	while counter < int(n):
		yield a
		a, b = b, a + b
		counter += 1




