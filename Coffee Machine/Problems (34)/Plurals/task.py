number = int(input())
word = input()

# write a condition for plurals
if number != 1:
	print(number, word + "s")
else:
	print(number, word)
