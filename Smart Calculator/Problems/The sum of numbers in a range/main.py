def range_sum(numbers, start, end):     
    summ = 0
    for number in numbers:
        if number in range(start, end + 1):
            summ += number
    return summ


input_numbers = [int(n) for n in input().split()]
a, b = [int(n) for n in input().split()]
print(range_sum(input_numbers, a, b))

