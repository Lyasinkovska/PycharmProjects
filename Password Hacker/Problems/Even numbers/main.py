n = int(input())

def even(n):
    even = 0
    for _ in range(n):
        yield even
        even += 2


# Don't forget to print out the first n numbers one by one here
for i in even(n):
    print(i)