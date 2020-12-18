import re

file_path = input()
with open(file_path) as file:
    consecutive_empty_lines = 0
    for i, line in enumerate(file, start=1):
        line = line.rstrip()
        if not line:
            consecutive_empty_lines += 1
            continue

        if len(line) > 79:
            print(f'Line {i}: S001 Too long')
        if line.startswith(' ') and re.search(r'^ +', line).span()[1] % 4 != 0:
            print(f'Line {i}: S002 Indentation is not a multiple of four')
        if re.search(r'^[^#]*;\s*(#.*)?$', line):
            print(f'Line {i}: S003 Unnecessary semicolon')
        if re.search(r'^[^#]*\S ?#.*$', line):
            print(f'Line {i}: S004 At least two spaces'
                  'before inline comment required')
        if re.search(r'^[^#]*#.*[Tt][Oo][Dd][Oo].*$', line):
            print(f'Line {i}: S005 TODO found')
        if consecutive_empty_lines > 2:
            print(f'Line {i}: S006 More than two blank lines'
                  'used before this line')
            consecutive_empty_lines = 0