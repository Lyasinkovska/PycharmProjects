def translator():
	choosing_language = input(f"Type \"en\" if you want to translate from French into English, "
							  f"or \"fr\" if you want to translate from English into French:\n")

	word_selection = input("Type the word you want to translate:\n")
	result = f"You chose \"{choosing_language}\" as a language to translate \"{word_selection}\""
	print(choosing_language)
	print(word_selection)
	print(result)


translator()
