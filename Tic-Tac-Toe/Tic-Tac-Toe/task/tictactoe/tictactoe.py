# write your code here
data = input("Enter yor cells: ")  # .replace(u'\xa0', u'_')
#data = "O_OXXO_XX"
cells = []
for elem in data:
	cells.append(elem)

field = "---------\n| {} {} {} |\n| {} {} {} |\n| {} {} {} |\n--------- " \
	.format(cells[0], cells[1], cells[2], cells[3], cells[4], cells[5], cells[6], cells[7], cells[8])


print(len(cells))


