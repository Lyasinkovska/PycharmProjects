class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, I am {self.name}!")


name = input()
me = Person(name)
me.greet()
