import itertools
a = [1, 2, 3]
b = [2, 3, 4]
c = [4, 5, 6]
abc = [a, b, c]



def rSubset(arr, r):
	return list(itertools.combinations(arr, r))

z = set()
for el in rSubset(abc, 2):
	z.update(set(el[0]) & set(el[1]))
print(z)