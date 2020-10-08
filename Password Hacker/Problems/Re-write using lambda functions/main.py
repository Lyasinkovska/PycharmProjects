result = (lambda a, b, c: (a + b) * c)(1, 2, 3)

x_list = [1, 2, 3, 4]
y_list = [10, 11, 12, 13]
print(x_list+y_list)
result = list(map(lambda x, y: x + y, x_list, y_list))
print(result)