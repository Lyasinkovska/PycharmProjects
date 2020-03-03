class Patient:
    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age

    def __repr__(self):
        rep = "Object of the class Patient. name: {}, " \
              "last_name: {}, age: {}".format(self.name, self.last_name, self.age)
        return rep

    def __str__(self):
        return f"{self.name} {self.last_name}. {self.age}"

