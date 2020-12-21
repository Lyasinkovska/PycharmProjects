import copy


def solve(obj):
    new_obj = copy.deepcopy(obj)
    return id(new_obj) != id(obj)
