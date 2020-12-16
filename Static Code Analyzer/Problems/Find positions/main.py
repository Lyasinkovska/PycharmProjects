# put your python code here
numbers = enumerate(input().split())
x = input()
result = [position for position, number in numbers if x == number]

if result:
	print(*result)
else:
	print("not found")