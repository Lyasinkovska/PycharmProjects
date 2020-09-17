# the object_list has already been defined
# write your code here
from collections.abc import Hashable


#object_list = [1, 397, 27468, -95, 1309, 397, -539874, -240767, -95, 397]
object_dict = {}
for obj in object_list:
	if isinstance(obj, Hashable):
		if obj not in object_dict.keys():
			object_dict[obj] = 1
		else:
			object_dict[obj] += 1
counter = 0
for value in object_dict.values():
	if value > 1:
		counter += value
print(counter)

