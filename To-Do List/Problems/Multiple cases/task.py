def f1(x):
    return(x**2)+1


def f2(x):
    return 1/(x**2)


def f3(x):
    return(x**2)-1


def f(x):
    if x <= 0:
        y = f1(x)
    elif 0 < x < 1:
        y = f2(x)
    else:
        y = f3(x)
    return y