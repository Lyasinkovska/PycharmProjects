"""
Write a decorator that prints a function with arguments passed to it.
NOTE! It should print the function, not the result of its execution!

For example:
"add called with 4, 5"

def logger(func):
    pass

@logger
def add(x, y):
    return x + y

@logger
def square_all(*args):
    return [arg ** 2 for arg in args]
"""
from functools import wraps


def print_function(func):
    @wraps(func)
    def wrapper(*args):
        func(*args)
        print(func.__name__, 'called', *args)
        return func

    return wrapper


@print_function
def fibonacci_number(index):
    a, b = 0, 1
    for _ in range(index - 2):
        a, b = b, a + b
    return 0 if index == 1 else b


if __name__ == '__main__':
    fibonacci_number(4)
