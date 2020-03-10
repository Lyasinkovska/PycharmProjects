mit_girls = [girl.get("name") for girl in girls if girl.get("education") == "MIT" and girl.get("about") != ""]
print('{}'.format(", ".join(mit_girls)))
