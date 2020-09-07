prime_numbers = [number for number in range(2, 1001) if all(number % n != 0 for n in range(2, number-1))]

#print(prime_numbers)