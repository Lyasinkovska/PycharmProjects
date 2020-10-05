with open('name.txt', 'r',  encoding='utf-8') as f1, \
	open('surname.txt', 'r',  encoding='utf-8') as f2, \
	open('full_name.txt', 'w',  encoding='utf-8') as f3:
	f3.write(f1.read() + ' ' + f2.read())