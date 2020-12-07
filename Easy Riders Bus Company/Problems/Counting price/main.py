def price_string(func):
    def wrapper(arg):
        return "£" + str(func(arg))

    return wrapper  

@price_string
def new_price(price):
    return float(int(price)*0.9)


