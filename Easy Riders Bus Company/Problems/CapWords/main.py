word = input()
if "_" in word:
	result = ''.join(w.lower().capitalize() for w in word.split('_'))
	print(result)
else:
	print(word.lower().capitalize())
