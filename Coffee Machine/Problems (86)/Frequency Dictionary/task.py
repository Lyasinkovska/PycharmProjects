# put your python code here
words = input().lower().split()
words_dictionary = dict()
for word in words:
	if word not in words_dictionary:
		words_dictionary[word] = 1
	else:
		words_dictionary[word] += 1
for key, value in words_dictionary.items():
	print(key, value)
