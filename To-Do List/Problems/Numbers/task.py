# put your python code here
def multiply(product=1, *numbers):
    for i in range(len(numbers)):
        product = product*numbers[i]
    return product
