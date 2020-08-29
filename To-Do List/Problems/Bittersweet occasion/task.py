# finish the function
def find_the_parent(child):
    classes = [Drinks, Pastry, Sweets]
    for par_class in classes:
        if issubclass(child, par_class):
            print(par_class.__name__)

