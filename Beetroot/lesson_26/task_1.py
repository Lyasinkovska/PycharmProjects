"""
A bubble sort can be modified to “bubble” in both directions. The first pass moves “up” the list and the second
pass moves “down.” This alternating pattern continues until no more passes are necessary. Implement this variation
and describe under what circumstances it might be appropriate.
"""


# recursive Bubble Sort

def bubble_sort_both_sides(iterable):
    size = len(iterable) - 1

    swapped = False

    for i in range(size):
        if iterable[i] > iterable[i + 1]:
            iterable[i], iterable[i + 1] = iterable[i + 1], iterable[i]
            swapped = True

    for i in range(size, 0, -1):
        if iterable[i] < iterable[i - 1]:
            iterable[i], iterable[i - 1] = iterable[i - 1], iterable[i]
            swapped = True

    if not swapped:
        return iterable

    return bubble_sort_both_sides(iterable)


if __name__ == '__main__':
    unsorted_list = [1, 21, 35, 7, 25, 9, 0, 42, 6, 8, 6]
    print(bubble_sort_both_sides(unsorted_list))
