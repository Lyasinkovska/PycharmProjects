import re

template = r"[A-Z][a-zA-Z]+\s?\w+?\s(Avenue|Street|Road|Boulevard)$"

"[A-Z]\w+\s?\w+?\s[AvenueStreetRoadBoulevard]\w+$"


streets = ["bourbon street", "Sesame Street", "Elm", "Prospekt Av.", "Santa Monica Boulevard"]
for street in streets:
	if re.match(template, street) == None:
		print(False)
	else:
		print(True)
