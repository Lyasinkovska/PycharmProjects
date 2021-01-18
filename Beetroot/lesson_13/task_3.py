"""
Write a function called `choose_func` which takes a list of nums and 2 callback functions. If all nums inside the list
are positive, execute the first function on that list and return the result of it. Otherwise, return the result of the
second one

# Assertions
assert choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25]
assert choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5]
"""


def choose_func(nums: list, func1, func2):
    is_all_positive = all(map(lambda elem: elem > 0, nums))
    if is_all_positive:
        return func1(nums)
    return func2(nums)


def square_nums(nums):
    return [num ** 2 for num in nums]


def remove_negatives(nums):
    return [num for num in nums if num > 0]


if __name__ == '__main__':
    nums1 = [1, 2, 3, 4, 5]
    nums2 = [1, -2, 3, -4, 5]
    x = choose_func
    print(x(nums1, square_nums, remove_negatives))
    y = choose_func(nums2, square_nums, remove_negatives)
    print(y)
