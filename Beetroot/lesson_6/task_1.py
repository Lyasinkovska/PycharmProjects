"""
Make a program that has some sentence (a string) on input and returns a dict containing all unique words as keys
and the number of occurrences as values.
"""
unique_words = {}
user_input = input("Enter a sentence: ").strip().split()
for word in user_input:
	if word not in unique_words:
		unique_words[word] = 1
	else:
		unique_words[word] += 1
print(unique_words)