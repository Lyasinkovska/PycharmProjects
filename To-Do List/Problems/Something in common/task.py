def calculate_linear(k, b, x):
    y = k * x + b
    return y


def calculate_quadratic(a, b, c, x):
    y = (a * x * x) + (b * x) + c
    return y


# create function common_part
def common_part(y):
    print("Value of the function equals", y)
