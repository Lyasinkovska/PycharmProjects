# read animals.txt
# and write animals_new.txt
animals = open('animals.txt', 'r')
new_animals = open('animals_new.txt', 'a')
for line in animals.read().split('\n'):
	new_animals.write(line + ' ')
animals.close()
new_animals.close()