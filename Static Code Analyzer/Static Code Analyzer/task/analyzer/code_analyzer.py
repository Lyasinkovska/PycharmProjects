import re


errors = {'S001': 'Too long',
		  'S002': 'Indentation is not a multiple of four',
		  'S003': 'Unnecessary semicolon',
		  'S004': 'At least two spaces before inline comments required',
		  'S005': 'TODO found',
		  'S006': 'More than two blank lines used before this line'
		  }


def main():
	with open('file.txt', 'r') as file: # 'file.txt'
		counter = 0
		for n, line in enumerate(file, start=1):
			long(line, n)
			indentation(line, n)
			semicolon(line, n)
			two_spaces(line, n)
			todo(line, n)
			if not line.strip():
				counter += 1

			else:
				if counter > 2:
					two_blank_lines(line, n)
				counter = 0


def long(line, n, error='S001'):
	if len(line) > 79:
		print(f'Line {n}: {error} {errors.get(error)}')


def indentation(line, n, error='S002'):
	if line.find(' ') == 0:
		if (len(line) - len(line.lstrip())) % 4 != 0:
			print(f'Line {n}: {error} {errors.get(error)}')


def semicolon(line, n, error='S003'):

	if ';' in line:
		if "'" in line:
			line.split("'")
		if '#' in line:
			line1, line2 = line.split('#')
			if ';' in line1:
				print(f'Line {n}: {error} {errors.get(error)}')



def two_spaces(line, n, error='S004'):
	template = r'.*\s{2,}$'
	if "#" in line:
		line1, line2 = line.split('#')
		if re.match(template, line1) is None:
			print(f'Line {n}: {error} {errors.get(error)}')


def todo(line, n, error="S005"):
	if "#" in line:
		line, line2 = line.split('#')
		if "todo" in line2.lower():
			print(f'Line {n}: {error} {errors.get(error)}')


def two_blank_lines(line, n, error='S006'):
	print(f'Line {n}: {error} {errors.get(error)}')


main()

