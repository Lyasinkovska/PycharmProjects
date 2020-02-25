# put your python code here

word = input()
new_word = "".join(reversed(word))
if word == new_word:
	print("Palindrome")
else:
	print("Not palindrome")
