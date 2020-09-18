def startswith_capital_counter(names):

    counter = 0
    for name in names:
        if not names:
            return -1
        elif name[0] != name[0].lower():
            counter += 1
    return counter