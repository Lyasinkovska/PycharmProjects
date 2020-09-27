import re

# define regex template
template = '[0-9a-fA-F][0-9a-fA-F]?'
hexadecimals = ['AA', '1', '6f', 'd9', '3E', 'c1', '9']
"""for n in hexadecimals:
	print(bool(re.match(template, n)))"""