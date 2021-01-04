"""
Write a function that takes in two numbers from the user via input(), call the numbers a and b,
and then returns the value of squared a divided by b, construct a try-except block which raises an exception
if the two values given by the input function were not numbers, and if value b was zero (cannot divide by zero).
"""


def square_division_of_two_numbers():
    try:
        a, b = map(int, (input('enter a: '), input('enter b: ')))
        return a**2 / b
    except ZeroDivisionError:
        return "Division by zero is forbidden."
    except ValueError:
        return 'ValueError: could not convert string to integer.'


print(square_division_of_two_numbers())
