# use the function blackbox(lst) that is already defined
lst = [1, 2, 3]
new_lst = blackbox(lst)
if id(lst) == id(new_lst):
	print("modifies")
else:
	print("new")