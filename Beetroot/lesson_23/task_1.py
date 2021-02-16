"""
Write a program that reads in a sequence of characters and prints them in reverse order,
using your implementation of Stack.
"""
from collections import deque


def print_stack_items(chars: str = '') -> None:
    if not isinstance(chars, str):
        try:
            chars = str(chars)
        except TypeError:
            raise TypeError("Input must be string")

    my_stack = deque()
    for char in chars:
        my_stack.append(char)
    while my_stack:
        print(my_stack.pop())


if __name__ == '__main__':
    print_stack_items('Hello my dear friend.')
    print_stack_items(123)
    print_stack_items([1, 5, 8])
