# write your code here
with open('users.json', 'r') as file:
	users = json.load(file)
	print(len(users["users"]))