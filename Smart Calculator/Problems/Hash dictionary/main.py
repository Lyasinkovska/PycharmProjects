# create your dictionary here
from collections.abc import Hashable


objects_dict = dict()
for obj in objects:
	if isinstance(obj, Hashable):
		objects_dict[obj] = obj.__hash__()
	else:
		continue