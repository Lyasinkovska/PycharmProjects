n = int(input())


def squares(n):
    i = 1
    for _ in range(n):
        yield i**2
        i += 1

# Don't forget to print out the first n numbers one by one here
for w in squares(n):
    print(w)