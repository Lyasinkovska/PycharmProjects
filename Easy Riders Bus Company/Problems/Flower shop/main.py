import itertools
#flower_names = ['rose', 'tulip', 'sunflower', 'daisy']
if len(flower_names) >= 3:
	for i in range(1, 4):
		for a in itertools.combinations(flower_names, i):
			print(a)
else:
	for i in range(1, len(flower_names)+1):
		for a in itertools.combinations(flower_names, i):
			print(a)


