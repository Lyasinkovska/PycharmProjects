""""
def sdvig(inval: int,  num: int = 1) -> int:
   pass

assert sdvig(123) == 312
assert sdvig(120) == 12
assert sdvig(120, 2) == 201
assert sdvig(543210, 3) == 210543
"""


def digits_shift(number: int, step: int = 1) -> int:
    if number < 10:
        return number

    tens = 0
    result = number

    while number > 9:
        number = number // 10
        tens += 1

    while step:
        result = (result % 10) * (10 ** tens) + result // 10
        step -= 1
    return result


if __name__ == '__main__':
    assert digits_shift(1) == 1
    assert digits_shift(123) == 312
    assert digits_shift(120) == 12
    assert digits_shift(120, 2) == 201
    assert digits_shift(543210, 3) == 210543
