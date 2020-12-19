# stage 1/6

'''row, column = map(int, input().split())
matrix = list()
for i in range(row):
	matrix.append(list(map(int, input().split())))

row2, column2 = map(int, input().split())
matrix2 = list()
for i in range(row2):
	matrix2.append(list(map(int, input().split())))

new_matrix = list()
if row != row2 or column != column2:
	print("ERROR")
else:
	for line, el in zip(matrix, matrix2):
		x = [(line[i] + el[i]) for i in range(column)]
		print(*x, sep=" ")'''

# stage 2/6
'''row, column = map(int, input().split())
matrix = list()
for i in range(row):
	matrix.append(list(map(int, input().split())))
constant = int(input())
for line in matrix:
	print(*[line[i] * constant for i in range(column)])'''

# stage 3/6


def add_matrices():
	row1, column1 = map(int, input("Enter size of first matrix: > ").split())
	print("Enter first matrix:")
	matrix1 = list()
	for i in range(row1):
		matrix1.append(list(map(float, input().split())))
	row2, column2 = map(int, input("Enter size of second matrix: > ").split())
	print("Enter second matrix:")
	matrix2 = list()
	for i in range(row2):
		matrix2.append(list(map(float, input().split())))
	if row1 != row2 or column1 != column2:
		print("The operation cannot be performed.")
	else:
		print("The result is:")
		for line, el in zip(matrix1, matrix2):
			if line[i].is_integer() and el[i].is_integer():
				x = [(int(line[i]) + int(el[i])) for i in range(column1)]
				print(*x, sep=" ")
			else:
				x = [(float(line[i]) + float(el[i])) for i in range(column1)]
				print(*x, sep=" ")


def multiply_by_constant():
	row, column = map(int, input("Enter size of matrix: > ").split())
	print("Enter matrix:")
	matrix = list()
	for i in range(row):
		matrix.append(list(map(float, input().split())))
	constant = float(input("Enter constant: > "))
	print("The result is:")
	for line in matrix:
		if line[i].is_integer() and constant.is_integer():
			print(*[int(line[i]) * int(constant) for i in range(column)])
		else:
			print(*[line[i] * constant for i in range(column)])


def multiply_matrices():
	row1, column1 = map(int, input("Enter size of first matrix: > ").split())
	print("Enter first matrix:")
	matrix1 = list()
	for i in range(row1):
		matrix1.append(list(map(float, input().split())))
	row2, column2 = map(int, input("Enter size of second matrix: > ").split())
	print("Enter second matrix:")
	matrix2 = list()
	for i in range(row2):
		matrix2.append(list(map(float, input().split())))
	if column1 != row2:
		print("The operation cannot be performed.")
	else:
		for i in range(row1):
			print(*[sum([matrix1[i][k] * matrix2[k][j] for k in range(row2)]) for j in range(column2)])

def main():
	while True:
		print("1. Add matrices\n2. Multiply matrix by a constant\n"
			  "3. Multiply matrices\n4.Transpose matrix\n0. Exit")
		choice = int(input("Your choice: > "))
		if choice == 0:
			exit()
		elif choice == 1:
			add_matrices()
		elif choice == 2:
			multiply_by_constant()
		elif choice == 3:
			multiply_matrices()
		elif choice ==4:
			transpose()


def transpose():
	print("1. Main diagonal\n2. Side diagonal\n3. Vertical line\n4. Horizontal line")
	choice = int(input("Your choice: > "))
	row, column = map(int, input("Enter matrix size: > ").split())
	matrix = list()
	for i in range(row):
		matrix.append(list(map(float, input().split())))
	print("The result is: ")
	if choice == 1:
		main_transpose(matrix, row, column)
	elif choice == 2:
		side_transpose(matrix, row, column)
	elif choice == 3:
		vertical_transpose(matrix, row, column)
	elif choice == 4:
		horizontal_transpose(matrix, row, column)


def main_transpose(matrix, row, column):
	for i in range(column):
		print(*[matrix[j][i] for j in range(row)])


def side_transpose(matrix, row, column):
	for i in range(column-1, -1, -1):
		print(*[matrix[j][i] for j in range(row-1, -1, -1)])


def horizontal_transpose(matrix, row, column):
	for i in range(column-1, -1, -1):
		print(*matrix[i])


def vertical_transpose(matrix, row, column):
	for line in matrix:
		print(*line[::-1])


main()

