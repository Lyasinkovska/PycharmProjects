def morning(func):
	def m_grettings(args):
		func(args)
		print("Good morning,", args)

	return m_grettings

@morning
def greetings(name):
	print('Hello,', name)


